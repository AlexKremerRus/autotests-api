import socket



def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("server start")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"connetc {client_address}")

        data = client_socket.recv(1024).decode()
        print(f"Получено {data}")

        response = f"сервер получил {data}"
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == '__main__':
    server()
