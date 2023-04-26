import socket

sock = socket.create_server(('127.0.0.1', 8000))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.listen(10)

with sock as s:
    print('Ожидание соединения...')

    try:
        while True:
            connection, address = s.accept()
            print(f'Подключено к: {address[0]} порт {address[1]}')

            received_data = connection.recv(1024).decode('utf-8')
            print('Получено: ', received_data, sep='\n')

            path = received_data.split(' ')[1]

            resp = f'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\nPath: {path}'

            connection.send(resp.encode('utf-8'))
    except KeyboardInterrupt:
        pass