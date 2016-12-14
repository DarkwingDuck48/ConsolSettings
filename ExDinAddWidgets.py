class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.main_layout = QtGui.QGridLayout()
        self.setLayout(self.main_layout)

        self.widgets = []
        self.build_widgets()

    def build_widgets(self):
        names = ('плюшки', 'баранки', 'бублики')

        for row, i in enumerate(names):
            label = QtGui.QLabel("Введите {}: ".format(i))
            self.main_layout.addWidget(label, row, 0)

            line_edit = QtGui.QLineEdit()
            self.main_layout.addWidget(line_edit, row, 1)

            self.widgets.append((label, line_edit))

        show = QtGui.QPushButton('Вывести содердимое полей')
        show.clicked.connect(self.show_content)
        self.main_layout.addWidget(show, len(names) + 1, 0)

    def show_content(self):
        for label, line_edit in self.widgets:
            print('{} {}'.format(label.text(), line_edit.text()))


app = QtGui.QApplication([])
win = MyWindow()
win.show()
app.exec_()
