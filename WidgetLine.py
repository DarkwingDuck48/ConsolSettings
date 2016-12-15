import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QComboBox,QHBoxLayout,QApplication


class WidgetLine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_line = QHBoxLayout()
        self.setLayout(self.layout_line)

        # Массивы
        self.scenario = ["ACT", "BDG", "TAX"]
        self.month_dict = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
                      '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': "Dec"}
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.years = [str(year) for year in range(2012, 2031)]

        # Combobox
        self.scenario_box = QComboBox()
        self.scenario_box.addItems(self.scenario)
        self.years_box = QComboBox()
        self.years_box.addItems(self.years)
        self.month_box = QComboBox()
        for key in self.month:
            self.month_box.addItem(key)
        # LineEdit
        self.Entity = QLineEdit()
        self.ICP = QLineEdit()

        # button
        self.show_table_button = QPushButton('ConsolSettings')
        # Линия виджета
        self.layout_line.addWidget(self.scenario_box)
        self.layout_line.addWidget(self.years_box)
        self.layout_line.addWidget(self.month_box)
        self.layout_line.addWidget(self.Entity)
        self.layout_line.addWidget(self.ICP)
        self.layout_line.addWidget(self.show_table_button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WidgetLine()
    window.show()
    sys.exit(app.exec_())