import sys
import os
import json
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QLabel, QTableWidget, QTableWidgetItem)
from Table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Базовые массивы
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.scenario = ["ACT", "BDG", "TAX"]
        self.years = [year for year in range(2012, 2031)]

        # Окно
        '''Высота одной строки с настройками - 40. При каждом добавлении новой энтити,
         окно соответственно должно увеличиваться на 40'''
        self.setGeometry(500, 300, 500, 40)
        self.setWindowTitle("Consolidation form helper")
        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)
        self.layout_grid = QGridLayout()
        self.mainwidget.setLayout(self.layout_grid)

        # Комбобоксы
        self.scenario_box = QComboBox()
        self.scenario_box.addItems(self.scenario)
        self.Entity = QLineEdit()
        self.ICP = QLineEdit()
        self.button = QPushButton("Show table")
        self.table = ""

        # Одна линия с настройками
        self.button.clicked.connect(self.generatetable)
        self.layout_grid.addWidget(self.scenario_box,0,0)
        self.layout_grid.addWidget(self.Entity, 0, 1)
        self.layout_grid.addWidget(self.ICP, 0, 2)
        self.layout_grid.addWidget(self.button, 0, 3)

    def generatetable(self):
        self.table = Table(entity=self.Entity.text())
        self.table.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())