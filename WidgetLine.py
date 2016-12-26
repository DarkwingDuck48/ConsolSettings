import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QComboBox,QHBoxLayout,QApplication
from Table import Table

class WidgetLine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_line = QHBoxLayout()
        self.setLayout(self.layout_line)
        #self.rows_count = rows

        # Массивы
        self.scenario = ["ACT", "BDG", "TAX"]
        self.month_dict = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
                      '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': "Dec"}
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.years = [str(year) for year in range(2012, 2031)]

        # Combobox
        self.scenario_box = QComboBox()
        self.scenario_box.addItems(self.scenario)
        self.years_box_start = QComboBox()
        self.years_box_start.addItems(self.years)
        self.month_box_start = QComboBox()
        self.month_box_start.addItems(self.month)
        self.years_box_end = QComboBox()
        self.years_box_end.addItems(self.years)
        self.month_box_end = QComboBox()
        self.month_box_end.addItems(self.month)
        # LineEdit
        self.Entity = QLineEdit()
        self.ICP = QLineEdit()

        # button
        self.show_table_button = QPushButton('ConsolSettings')
        self.button_delete = QPushButton('Del')
        # Линия виджета
        self.layout_line.addWidget(self.scenario_box)
        self.layout_line.addWidget(self.years_box_start)
        self.layout_line.addWidget(self.month_box_start)
        self.layout_line.addWidget(self.Entity)
        self.layout_line.addWidget(self.ICP)
        self.layout_line.addWidget(self.years_box_end)
        self.layout_line.addWidget(self.month_box_end)
        self.layout_line.addWidget(self.show_table_button)
        self.layout_line.addWidget(self.button_delete)

        self.show_table_button.clicked.connect(self.generatetable)
        self.button_delete.clicked.connect(self.close)

    def generatetable(self):
        entity = self.Entity.text()
        icp = self.ICP.text()
        scenario = self.scenario_box.itemText(self.scenario_box.currentIndex())
        year_start = self.years_box_start.itemText(self.years_box_start.currentIndex())
        month_start = self.month_box_start.itemText(self.month_box_start.currentIndex())
        year_end = self.years_box_end.itemText(self.years_box_end.currentIndex())
        month_end = self.month_box_end.itemText(self.month_box_end.currentIndex())
        print(entity, icp, scenario, year_start, month_start, year_end, month_end)
        self.table = Table(scenario=scenario, year_start=year_start, month_start=month_start, entity=entity,
                           icp=icp, year_end=year_end, month_end=month_end)
        self.table.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WidgetLine()
    window.show()
    sys.exit(app.exec_())
