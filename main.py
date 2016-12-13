import sys
import os
import json
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QLabel, QTableWidget, QTableWidgetItem)


class Table(QWidget):
    def __init__(self, entity=None, parent=None):
        super().__init__(parent)
        self.entity = entity
        self.setWindowTitle("Consolidation settings for {}".format(self.entity))
        self.setGeometry(300, 300, 350, 240)
        # Consol Combobox
        self.consolmetod = ['CONSOLIDATED', 'HOLDING', 'DISPOSED', 'DISPOSEDDY', 'NEWSUBS', 'DISCONTINUED', 'AHS',
                            'NOTCONSOL']
        self.consolmethod_box = QComboBox()
        self.consolmethod_box.addItems(self.consolmetod)
        self.but_confirm = QPushButton("Confirm")
        self.but_clear = QPushButton("Clear")
        # Table
        self.table = QTableWidget(self)
        self.table_layout = QGridLayout()
        self.setLayout(self.table_layout)
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ConsolSettings"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))
        self.consolsettings = ['[Active]', '[PCON]', '[POWN]', '[Method]', '[Consol1]']
        for i in range(0, len(self.consolsettings)):
            self.table.setItem(i, 0, QTableWidgetItem(self.consolsettings[i]))
        self.table.setRowHidden(4, True)
        self.table.setCellWidget(3, 1, self.consolmethod_box)

        self.table_layout.addWidget(self.table, 0, 0, 1, 0)
        self.table_layout.addWidget(self.but_clear, 1, 0)
        self.table_layout.addWidget(self.but_confirm, 1, 1)
        self.consolmethod_box.currentIndexChanged.connect(self.method_check)

    def method_check(self):
        current_text = self.consolmethod_box.itemText(self.consolmethod_box.currentIndex())
        if current_text == 'DISPOSEDDY':
            self.table.setRowHidden(4, False)
        else:
            self.table.setRowHidden(4, True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Базовые массивы
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.scenario = ["ACT", "BDG", "TAX"]
        self.years = [year for year in range(2012, 2031)]

        # Окно
        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle("Consolidation form helper")
        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)
        self.layout_grid = QGridLayout()
        self.mainwidget.setLayout(self.layout_grid)

        # Комбобоксы
        self.scenario_box = QComboBox()
        self.scenario_box.addItems(self.scenario)
        self.Entity = QLineEdit()

        self.button = QPushButton("Show table")
        self.table = ""
        self.button.clicked.connect(self.generatetable)
        self.layout_grid.addWidget(self.scenario_box,0,0)
        self.layout_grid.addWidget(self.Entity, 0, 1)
        self.layout_grid.addWidget(self.button, 0, 2)


    def generatetable(self):
        self.table = Table(entity=self.Entity.text())
        self.table.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())