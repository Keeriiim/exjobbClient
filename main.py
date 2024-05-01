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

