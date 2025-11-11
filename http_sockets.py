from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWebEngineWidgets
from pathlib import Path
import sys
import socket

HOST = 'localhost'
PORT_HTTP = 80
BUFSIZE = 1024
PATH = '/hello2.html'

class MainWindow(QMainWindow):
    def __init__(self, page):
        super().__init__()

        self.setWindowTitle("http")
        
        view = QtWebEngineWidgets.QWebEngineView()
        html = page #Path('C:\\Python\\http\\hello.html').read_text(encoding="utf8")
        view.setHtml(html)
        self.setCentralWidget(view)


def get_resp(sock):
    ret = sock.recv(BUFSIZE)
    resp = ret
    while len(ret) > 0:
        ret = sock.recv(BUFSIZE)
        resp += ret
    return resp

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
        client.connect((HOST,PORT_HTTP))
        
        if not socket: 
            raise Exception("Connection error")
        
except Exception:
    print("Connection error")

msg = f"GET {PATH} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
msg = msg.encode("ascii")
client.sendall(msg)

resp = get_resp(client)

idx = resp.index(b"\r\n\r\n") + 4

app = QApplication(sys.argv)

window = MainWindow(resp[idx:].decode())
window.show()

app.exec()

