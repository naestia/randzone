from random import randint
import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic

from settings import *

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'vibe.randdrop.0.1.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class Cod(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Cod, self).__init__(*args, **kwargs)
        self.picture = os.path.join(album_art_dir, "al-mazra-grid.jpg")
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "main.ui"), self)
        self.setWindowTitle("RandDrop")
        self.set_pixmap()
        self.randomize.clicked.connect(self.check_position)
        
    def set_pixmap(self):
        art = QPixmap(self.picture)
        self.label.setPixmap(art)
        self.label.setScaledContents(True)

    def check_position(self):
        self.okay_list = []
        for x in range(0, 10):
            for y in range(0, 10):
                pair = [(x * 80), (y * 80)]
                if pair not in no_go:
                    self.okay_list.append(pair)

        draw_pair = self.okay_list[randint(0, len(self.okay_list)-1)]
        self.draw_something(draw_pair)

    def draw_something(self, pos):
        self.set_pixmap()
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.setBrush(QColor(133, 183, 62, 127))
        painter.drawRect(pos[0], pos[1], 80, 80)
        painter.end()
        self.label.setPixmap(canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Cod()
    window.show()
    sys.exit(app.exec())