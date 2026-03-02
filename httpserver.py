import socket

class HttpWebBrowserHander:

    def __init__(self, ip : str = 'localhost', port : int = 8080):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(5)

        print(f'Server started on http://{ip}:{port}')
    
    def MainHandler(self, user, addres, data, legal):
        pass

    def __call__(self, *args, **kwds):

        iteration = 0

        while True:
            iteration += 1

            legal = iteration % 2 == 1
            user, addres = self.sock.accept()
            data = HttpWebBrowserHander.HttpGet(user.recv(4096).decode())
            self.MainHandler(user, addres, data, legal)
            user.close()
    
    @staticmethod
    def HttpResponse(html_content : str) -> str:
        return f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: {len(html_content)}
Connection: close

{html_content}"""

    @staticmethod
    def HttpGet(data : str) -> str:
        try:
            datas = data.split('\n\n')[0].split('\r\n\r\n')[1].split('&')
            datas = {x.split('=')[0]:x.split('=')[1] for x in datas}
            return datas
        except:
            return {}