import socket
import sys


class HttpServer:
    def __init__(self, host: str, port: int, server_name: str) -> None:
        self._host: str = host 
        self._port: int = port
        self._server_name: str = server_name

    
    def serve_forever(self) -> None:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            server.bind((self._host, self._port))  # Привязка серверного сокета к определенному адресу
            server.listen()  # Начало прослушивания 

            while 1:
                conn, _ = server.accept()  # Принятие клиентского сокета

                try:
                    self.serve_client(conn)  # Обработка HTTP запроса
                except Exception as e:
                    print("Client serving failed", e)
        finally:
            server.close()

    
    def serve_client(self) -> None:
        try:
            req = self.parse_request(conn)  # Синтаксический анализ HTTP запроса
            resp = self.handle_request(req)  # Обработка HTTP запроса
            self.send_response(conn, resp)  # Отправка ответа
        except ConnectionResetError as e:
            conn = None
        except Exception as e:
            self.send_error(conn, e)  # Отправка ошибки в случае неполадки
        
        if conn:
            conn.close()

    
    def parse_request(self, conn) -> None: ...

    def handle_request(self, req) -> None: ...
    
    def send_response(self, conn, resp) -> None: ...

    def send_error(self, conn, err) -> None: ...


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]

    server = HttpServer(host, port, name)

    try:
        server.serve_forever()
    except KeyboardInterrupt: pass