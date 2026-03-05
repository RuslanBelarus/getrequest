import socket

class HttpWebBrowserKit:

    def __init__(self): pass

    @staticmethod
    def Initing(handler, func, *args):
        if handler.legal: return [func, args]
    
    @staticmethod
    def Protocol(collection):
        outp = None
        try:
            for proto in collection:
                outp = proto[0](*proto[1]) if proto is not None else None
        except KeyError: pass
        return outp
    
class HttpWebBrowserHander:

    def __init__(self, ip : str = 'localhost', port : int = 8080):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(5)

        self.legal = 0
        self.iteration = 0

        print(f'Server started on http://{ip}:{port}')
    
    def MainHandler(self, user, addres, data, legal):
        pass

    def HttpOpen(self, *args, **kwds):

        while True:
            self.iteration += 1

            self.legal = self.iteration % 2 == 1
            user, addres = self.sock.accept()
            data = user.recv(4096).decode()
            self.MainHandler(user, addres, data, self.legal)
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
    
    @staticmethod
    def HttpStatus(data : str) -> str:
        return data.split('\n')[0].replace('POST /', '').replace(' HTTP/1.1', '').replace('\r', '')
    
    @staticmethod
    def HtmlFormating(html : str, *args) -> str:
        for i, val in enumerate(args):
            html = html.replace(f'${i}', val)
        return html
