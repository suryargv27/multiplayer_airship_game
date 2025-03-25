import socket, sys, pygame, pickle, random
from threading import Thread

pygame.init()

IP = '192.168.95.146'
port = 14568

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, port))

server.listen(2)
print('[server started]')

screen_width = 1000
screen_height = 750

rect1 = pygame.Rect(screen_width/2 - 50, screen_height - 20, 100, 10)
rect2 = rect1.copy()
rect2.y = 10
position = [rect1, rect2]
score = [0, 0]

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
ball_speed_x = 5
ball_speed_y = 5

current_player = 0
score_time = None

class scene:
    def __init__(self):
        self.rect = None
        self.ball = None
        self.score = None

def handle_client(conn, player):
    global current_player

    send_scene = scene()
    send_scene.rect = position[player]
    send_scene.ball = ball
    conn.send(pickle.dumps(send_scene))
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            position[player] = pickle.loads(data)

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = position[0]
                else:
                    reply = position[1]

            send_scene = scene()
            send_scene.rect = reply
            send_scene.ball = ball
            send_scene.score = score
            send_scene = pickle.dumps(send_scene)
            conn.sendall(send_scene)

            print('Recieved:', data)
            print('Sending:', send_scene)
        except Exception as e:
            print(e)
            break

    current_player -= 1
    print('Lost Connectin')
    conn.close()

def ball_handler():
    global ball_speed_x, ball_speed_y, current_player, score_time

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        if current_player <= 1 or (score_time is not None and pygame.time.get_ticks() - score_time < 3000):
            continue
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.bottom <= 0:
            ball.center = (screen_width/2, screen_height/2)
            ball_speed_x = random.choice((-1, 1)) * ball_speed_x
            ball_speed_y = random.choice((-1, 1)) * ball_speed_y
            score[1] += 1

            score_time = pygame.time.get_ticks()
        elif ball.top >= screen_height:
            ball.center = (screen_width/2, screen_height/2)
            ball_speed_x = random.choice((-1, 1)) * ball_speed_x
            ball_speed_y = random.choice((-1, 1)) * ball_speed_y
            score[0] += 1

            score_time = pygame.time.get_ticks()
        if ball.left <= 0 or ball.right >= screen_width:
            ball_speed_x *= -1

        if ball.colliderect(position[0]) or ball.colliderect(position[1]):
            ball_speed_y *= -1

thread = Thread(target=ball_handler, args=())
thread.start()


while True:
    conn, addr = server.accept()
    print(f"[Connection from {addr}]")

    thread = Thread(target=handle_client, args=(conn, current_player, ))
    thread.start()
    current_player += 1


