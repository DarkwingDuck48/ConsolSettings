import sys
import os
import json
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem)
from Table import Table
from WidgetLine import WidgetLine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Окно
        '''Высота одной строки с настройками - 40. При каждом добавлении новой энтити,
         окно соответственно должно увеличиваться на 40'''
        self.setGeometry(500, 300, 500, 40)
        self.setWindowTitle("Consolidation form helper")
        self.mainwidget = QWidget(self)
        self.setCentralWidget(self.mainwidget)
        self.layout_grid = QGridLayout()
        self.mainwidget.setLayout(self.layout_grid)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        addline = QAction('&Add Line', self)
        addline.setShortcut('Ctrl+N')
        addline.setStatusTip('Add new Node')
        addline.triggered.connect(self.addrow)

        self.statusBar()

        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(addline)
        self.widget = ''
        self.table = ""
    '''
    def generatetable(self):
        self.table = Table(entity=self.Entity.text())
        self.table.show()
    '''

    def addrow(self):
        self.widget = WidgetLine()
        self.layout_grid.addWidget(self.widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())