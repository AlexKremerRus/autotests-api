import socket



def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("server start")
    list_ = []
    while True:

        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу ")

        data = client_socket.recv(1024).decode()
        list_.append(data)
        print(f"Пользователь с адресом: {client_address } отправил сообщение: {data}")

        client_socket.send('\n'.join(list_).encode())

        client_socket.close()

if __name__ == '__main__':
    server()
