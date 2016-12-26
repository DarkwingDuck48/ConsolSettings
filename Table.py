import json
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QComboBox,QGridLayout,QTableWidget,QTableWidgetItem,QApplication


class Table(QWidget):
    def __init__(self, scenario=None, year_start=None, month_start=None, entity=None, icp=None,
                 year_end=None, month_end=None, parent=None):
        super().__init__(parent)
        self.scenario = scenario
        self.year_start = year_start
        self.month_start = month_start
        self.year_end = year_end
        self.month_end = month_end
        self.entity = entity
        self.icp = icp
        self.setWindowTitle("Consolidation settings for {}".format(self.entity))
        self.setGeometry(300, 300, 350, 240)
        self.file = open('.\\text.txt', 'w', encoding='utf-8')

        # Consol Combobox
        self.consolmetod = ['CONSOLIDATED', 'HOLDING', 'DISPOSED', 'DISPOSEDDY', 'NEWSUBS', 'DISCONTINUED', 'AHS',
                            'NOTCONSOL']
        self.consolmethod_box = QComboBox()
        self.consolmethod_box.addItems(self.consolmetod)
        self.but_confirm = QPushButton("Confirm")
        self.but_clear = QPushButton("Clear")
        # Parametrs set 0 if init, else set old
        self.settings = {'Active': '', "POwn": '', 'PCon': '', "Method": '', "Consol1": ""}
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

        self.but_clear.clicked.connect(self.cleartable)
        self.consolmethod_box.currentIndexChanged.connect(self.method_check)
        self.but_confirm.clicked.connect(self.writetable)

    def method_check(self):
        current_text = self.consolmethod_box.itemText(self.consolmethod_box.currentIndex())
        if current_text == 'DISPOSEDDY':
            self.table.setRowHidden(4, False)
        else:
            self.table.setRowHidden(4, True)

    def cleartable(self):
        rows = [i for i in range(0, self.table.rowCount()) if i != 3]
        for row in rows:
            self.table.setItem(row, 1, QTableWidgetItem("0"))

    def writetable(self):
        self.settings["Active"] = self.table.item(0, 1).text()
        self.settings["Pcon"] = self.table.item(1, 1).text()
        self.settings["POwn"] = self.table.item(2, 1).text()
        self.settings["Method"] = self.consolmethod_box.itemText(self.consolmethod_box.currentIndex())
        if not self.table.isRowHidden(4):
            self.settings["Consol1"] = self.table.item(4, 1).text()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.show()
    sys.exit(app.exec_())
