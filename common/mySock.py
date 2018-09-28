from socketIO_client import SocketIO


class mySockIo(object):
    def __init__(self,host,port,router):
        self.sock = SocketIO(host,port)
        self.sock.on(router,self.on_message)

    def on_message(self,*args):
        return args[0] if isinstance(args[0],dict) else None

    def send(self,data):
        self.sock.send(data)
        result = self.sock.wait_for_callbacks(2)
        return result

    def close(self):
        self.sock.disconnect()




if __name__ == '__main__':
    host = 'http://tst-bubble2-dev-stg74.1768.com'
    port = 80
    router = 'router'
    sock = mySock(host, port, router)
    result = sock.send('cc')
    print(result)
