import socket
import sys


class HttpServer:
    def __init__(self, host, port, server_name) -> None:
        self._host = host
        self._port = port
        self._server_name = server_name

    
    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            server.bind((self._host, self._port))
            server.listen()

            while 1:
                conn, _ = server.accept()

                try:
                    self.serve_client(conn)
                except Exception as e:
                    print("Client serving failed", e)
        finally:
            server.close()

    
    def serve_client(self) -> None:
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError as e:
            conn = None
        except Exception as e:
            self.send_error(conn, e)
        
        if conn:
            conn.close()

    
    def parse_request(self, conn): ...

    def handle_request(self, req): ...
    
    def send_response(self, conn, resp): ...

    def send_error(self, conn, err): ...


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]

    server = HttpServer(host, port, name)

    try:
        server.serve_forever()
    except KeyboardInterrupt: pass