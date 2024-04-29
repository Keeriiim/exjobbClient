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
            exit(0)









    def send_message(self, message):
        try:
            self.socket.sendall(message.encode())
        except BrokenPipeError:
            print("Connection to the server is lost.")
        except Exception as e:
            print(e)

    def receive_response(self):
        try:
            response = self.socket.recv(1024).decode()  # Receive data from the server
            print(response)


        except ConnectionResetError:
            print("Connection to the server is reset.")
        except Exception as e:
            print(e)

    def close(self):
        self.socket.close()

    def message_handler(self):
        while True:
            message = input("Enter message to send: ")
            if message.strip():  # Check if the message is not empty (ignoring leading and trailing whitespace)
                return message
            else:
                print("Please enter a non-empty message.")







    def run(self):
        self.connect()
        print('Type "quit" to exit')
        while True:
            try:
                print("")
                self.receive_response()  # Receive response from the server

                message = self.message_handler()

                if message.lower() == 'quit':
                    break
                self.send_message(message)

            except Exception as e:
                print(e)

        self.close()

if __name__ == "__main__":
    client = Client('127.0.0.1', 12345)  # Use the same host and port as the server
    client.run()















    '''running = ""
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True

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
            response = self.socket.recv(1024).decode()
            message_content, expect_response = response.split('|')
            print(message_content)
            if expect_response == "True":
                # Expecting a response, handle accordingly
                message = client.message_handler()

                self.socket.send(message.encode())


            if message_content.lower().startswith("congratz"):
                # Close the connection if the message is congratulatory
                self.close()
        except ConnectionResetError:
            print("Connection to the server is reset.")
        except Exception as e:
            print(e)

    def close(self):
        self.socket.close()

    def message_handler(self):
        message = input("Client response:")
        if message.lower() == '':
            message = input("Client response:")
        return message


if __name__ == "__main__":
    client = Client('127.0.0.1', 12345)  # Use the same host and port as the server
    client.connect()
    print('type quit to exit')

    while True:

        try:
            print("")
            client.receive_response()

        except Exception as e:
            print(e)

    client.close()'''











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
