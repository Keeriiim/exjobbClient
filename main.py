import socket

class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.socket.connect((self.server_host, self.server_port))
            print("Connected to the server.")
        except ConnectionRefusedError:
            print("Connection to the server failed.")

    def send_message(self, message):
        try:
            self.socket.sendall(message.encode())
        except BrokenPipeError:
            print("Connection to the server is lost.")
        except Exception as e:
            print(e)

    def receive_response(self):
        try:
            response = self.socket.recv(1024)  # Receive data from the server
            print("Question:", response.decode())
        except ConnectionResetError:
            print("Connection to the server is reset.")
        except Exception as e:
            print(e)

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    client = Client('127.0.0.1', 12345)  # Use the same host and port as the server
    client.connect()
    print('type quit to exit')
    while True:

        try:
            print("")
            client.receive_response()  # Receive response from the server after sending a message
            message = input("True/False: ")
            if message.lower() == 'quit':
                break
            client.send_message(message)
        except Exception as e:
            print(e)

    client.close()









'''import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8888") as websocket:
        message = input("Enter a message to send to the server: ")
        await websocket.send(message)
        print("Message sent.")

async def receive_messages():
    async with websockets.connect("ws://localhost:8888") as websocket:
        while True:
            message = await websocket.recv()
            print("Received message from server:", message)

async def main():
    await asyncio.gather(send_message(), receive_messages())

asyncio.run(main())'''


'''async def main():
    async with websockets.connect('ws://localhost:8888') as websocket:
        try:
            while True:
                message = input("Enter a message to send to the server: ")
                await websocket.recv()  # Receive menu options from the server
                print(message)


                await websocket.send('Hello client') # Send the choice to the server

                response = await websocket.recv()  # Receive and print the server's response
                print(response)
        except Exception as e:
            if str(e) == "received 1000 (OK); then sent 1000 (OK)":
                print("Connection successfully closed")
            else:
                print(f"{e}")



if __name__ == "__main__":
    asyncio.run(main())'''
