import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox, QLineEdit, QLabel, QTableWidget, QTableWidgetItem)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Базовые массивы
        self.consolmetod = ['CONSOLIDATED', 'HOLDING', 'DISPOSED', 'DISPOSEDDY', 'NEWSUBS', 'DISCONTINUED', 'AHS',
                            'NOTCONSOL']
        self.consolsettings = ['[Active]', '[PCON]', '[POWN]', '[Method]', '[Consol1]']
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.scenario = ["ACT", "BDG", "TAX"]
        self.years = [year for year in range(2012, 2031)]

        # Окно
        self.setGeometry(500, 300, 1100, 300)
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

        self.layout_grid.addWidget(self.table, 0, 0)

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