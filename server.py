import socket
import threading


class ChatServer:
    def __init__(self, host='127.0.0.1', port=9999):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []
        self.rooms = {'general': []}  # Dictionary of chat rooms

    def broadcast(self, message, room='general'):
        for client in self.rooms[room]:
            client.send(message)

    def handle(self, client, nickname):
        room = 'general'
        while True:
            try:
                message = client.recv(1024).decode('ascii')

                if message.startswith('/'):
                    if message.startswith('/join '):
                        new_room = message[6:]
                        if new_room in self.rooms:
                            room_clients = self.rooms[room]
                            room_clients.remove(client)
                            room = new_room
                            self.rooms[room].append(client)
                            client.send(f'Joined room {room}'.encode('ascii'))
                        else:
                            client.send('Room does not exist'.encode('ascii'))
                    elif message.startswith('/create '):
                        new_room = message[8:]
                        if new_room not in self.rooms:
                            self.rooms[new_room] = [client]
                            self.rooms[room].remove(client)
                            room = new_room
                            msg = f'Created and joined room {room}'
                            message = msg.encode('ascii')
                            client.send(message)
                        else:
                            client.send('Room already exists'.encode('ascii'))
                    else:
                        client.send('Invalid command'.encode('ascii'))
                else:
                    msg = f'{nickname}: {message}'.encode('ascii')
                    self.broadcast(msg, room)

            except Exception:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the chat!'.encode('ascii'))
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)
            self.rooms['general'].append(client)

            print(f'Nickname of the client is {nickname}!')
            self.broadcast(f'{nickname} joined the chat!'.encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(
                target=self.handle,
                args=(client, nickname)
            )
            thread.start()

    def run(self):
        print("Server Started!")
        self.receive()


if __name__ == "__main__":
    ChatServer().run()
