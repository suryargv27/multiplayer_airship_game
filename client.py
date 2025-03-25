import pygame, sys, pickle
from network import Network

pygame.init()

screen_width = 1000
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Client')
game_font = pygame.font.Font('freesansbold.ttf', 32)

client_number = 0

class scene:
    def __init__(self):
        self.rect = None
        self.ball = None
        self.score = None

class Player():
    def __init__(self, rect, color):
        self.speed = 7
        self.color = color
        self.rect = rect
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width

def redraw_screen(screen, player1, player2, ball):
    screen.fill((255, 255, 255))

    player1.draw(screen)
    player2.draw(screen)
    pygame.draw.ellipse(screen, (0, 0, 0), ball)

    player_text = game_font.render(f'{player1.score}', False, (200, 200, 200))
    screen.blit(player_text, (screen_width/2 - 7, screen_height/2 - 48))
    player_text = game_font.render(f'{player2.score}', False, (200, 200, 200))
    screen.blit(player_text, (screen_width/2 - 7, screen_height/2 + 20))

    pygame.draw.line(screen, (0, 0, 0), (0, screen_height/2), (screen_width, screen_height/2))

    pygame.display.update()

def main():
    net = Network()
    position = net.get_response()

    rect = pickle.loads(position).rect
    player = Player(rect, (23, 127, 117))

    rect2 = rect.copy()
    rect2.top = 20
    player2 = Player(rect2, (68, 114, 148))

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        scene_data = pickle.loads(net.send(pickle.dumps(rect)))
        player2.rect = scene_data.rect
        ball = scene_data.ball
        player.score = scene_data.score[0]
        player2.score = scene_data.score[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        player.move()
        redraw_screen(screen, player, player2, ball)

main()