import socket
import threading

class Network:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', 0))
        self.playerId = self.client.getsockname()[1]
        self.players = {}
        self.serverAddress = (self.host, self.port)


    def receiveData(self):
        while True:
            try:
                data, _ = self.client.recvfrom(1024)
                playersData = data.decode('utf-8').split(';')
                self.players = {}
                
                for player in playersData:
                    pid, x, y = map(int, player.split(','))
                    if pid != self.playerId:
                        self.players[pid] = {'x': x, 'y': y}  
            except:
                break

    def startReceiving(self):
        receiveThread = threading.Thread(target=self.receiveData)
        receiveThread.start()

    def sendData(self, data):
        self.client.sendto(data.encode('utf-8'), self.serverAddress)
        print('testing')

    def sendConnect(self):
        self.client.sendto(f"connect,{self.playerId}".encode('utf-8'), self.serverAddress)

    def sendDisconnect(self):
        self.client.sendto(f"disconnect,{self.playerId}".encode('utf-8'), self.serverAddress)

