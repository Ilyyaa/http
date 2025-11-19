from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWebEngineWidgets
from pathlib import Path
import sys
import requests

class MainWindow(QMainWindow):
    def __init__(self, page):
        super().__init__()

        self.setWindowTitle("http")
        
        view = QtWebEngineWidgets.QWebEngineView()
        html = page #Path('C:\\Python\\http\\hello.html').read_text(encoding="utf8")
        view.setHtml(html)
        self.setCentralWidget(view)

app = QApplication(sys.argv)

r = requests.get('http://localhost:80/summary.html')

window = MainWindow(r.content.decode())
window.show()


app.exec()
