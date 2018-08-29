from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import sys
import os

app = QApplication(sys.argv)

browser = QWebEngineView()
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "video.html"))
local_url = QUrl.fromLocalFile(file_path)
browser.load(local_url)

browser.show()

app.exec_()