import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QWidget, QGridLayout, QAction,
                             qApp, QFileDialog, QComboBox,QLineEdit, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Базовые массивы
        self.consolmetod = ['CONSOLIDATED', 'HOLDING', 'DISPOSED', 'DISPOSEDDY', 'NEWSUBS', 'DISCONTINUED', 'AHS',
                            'NOTCONSOL']
        self.consolsettings = ['[Active]', '[PCON]', '[POWN]', '[Method]', '[Consol1]']
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.years = [year for year in range(2012, 2031)]

        # Окно
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Consolidation form helper")
        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)
        self.layout_grid = QGridLayout()
        self.mainwidget.setLayout(self.layout_grid)

        # Элементы в окне
        self.Entity_label = QLabel("Entity")
        self.Entity = QLineEdit()
        self.ICP_label = QLabel("ICP")
        self.ICP = QLineEdit()
        self.year_from_label = QLabel('Start year')
        self.year_from = QComboBox()
        self.year_to_label = QLabel('End year')
        self.year_to = QComboBox()
        # Расположение
        self.layout_grid.addWidget(self.Entity_label, 0, 0)
        self.layout_grid.addWidget(self.ICP_label, 0, 1)
        self.layout_grid.addWidget(self.Entity, 1, 0)
        self.layout_grid.addWidget(self.ICP, 1, 1)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())