import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QLabel, QTableWidget, QTableWidgetItem)


class Table(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Consolidation settings")
        self.setGeometry(300, 300, 350, 200)
        self.table = QTableWidget(self)
        self.table_layout =QGridLayout()
        self.setLayout(self.table_layout)
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0,150)
        self.table.setColumnWidth(1,150)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ConsolSettings"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))
        self.consolsettings = ['[Active]', '[PCON]', '[POWN]', '[Method]', '[Consol1]']
        for i in range(0,len(self.consolsettings)):
            self.table.setItem(i, 0, QTableWidgetItem(self.consolsettings[i]))
        self.table_layout.addWidget(self.table)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Базовые массивы
        self.consolmetod = ['CONSOLIDATED', 'HOLDING', 'DISPOSED', 'DISPOSEDDY', 'NEWSUBS', 'DISCONTINUED', 'AHS',
                            'NOTCONSOL']

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
        self.consolmethod_box = QComboBox()
        self.consolmethod_box.addItems(self.consolmetod)
        self.scenario_box = QComboBox()
        self.scenario_box.addItems(self.scenario)
        '''
        # таблица
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(10)
        self.table.setColumnWidth(8, 120)
        self.table.setColumnHidden(9, True)

        # Имена колонок
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Scenario"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Month/year start"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Month/year end"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Entity"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("ICP"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("[Active]"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem('[PCON]'))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem('[POWN]'))
        self.table.setHorizontalHeaderItem(8, QTableWidgetItem('[Method]'))
        self.table.setHorizontalHeaderItem(9, QTableWidgetItem('[Consol1]'))

        # Заполнение первой строки таблицы
        self.table.setCellWidget(0, 8, self.consolmethod_box)
        self.table.setCellWidget(0, 0, self.scenario_box)
        '''
        self.table = Table()
        self.button = QPushButton("Show table")
        self.button.clicked.connect(self.table.show)
        self.layout_grid.addWidget(self.button)

        self.consolmethod_box.currentIndexChanged.connect(self.method_check)

    def method_check(self):
        current_text = self.consolmethod_box.itemText(self.consolmethod_box.currentIndex())
        if current_text == 'DISPOSEDDY':
            self.table.setColumnHidden(9, False)
        else:
            self.table.setColumnHidden(9, True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())