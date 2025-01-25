import socket
import threading

class Network:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', 0))
        self.clientID = self.client.getsockname()[1]
        self.roomData = {}
        self.serverAddress = (self.host, self.port)


    def receiveData(self):
        while True:
            try:
                data, _ = self.client.recvfrom(1024)
                playersData = data.decode('utf-8').split(';')
                self.roomData = {}
                
                for player in playersData:
                    pid, x, y = map(int, player.split(','))
                    if pid != self.playerId:
                        self.roomData[pid] = {'x': x, 'y': y}  
            except:
                break

    def startReceiving(self):
        receiveThread = threading.Thread(target=self.receiveData)
        receiveThread.start()

    def sendData(self, data):
        self.client.sendto(data.encode('utf-8'), self.serverAddress)


