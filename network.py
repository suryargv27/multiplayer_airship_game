import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP = '192.168.95.146'
        self.port = 14568
        self.addr = (self.IP, self.port)
        self.response = self.connect()
    
    def get_response(self):
        return self.response

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data)
            return self.client.recv(1024)
        except socket.error as error:
            print(error)
