from PyQt5.QtWidgets import QWidget,QPushButton,QComboBox,QGridLayout,QTableWidget,QTableWidgetItem

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