import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(500,500)
        self.setWindowTitle('Welcome')

        self.textedit1 = QLineEdit('',self)
        self.textedit1.move(200,200)

        self.button = QPushButton('Login',self)
        self.button.move(250,250)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):

        user = self.textedit1.text()
        self.textedit1.setText('')

        self.f = Floor(self, user)
        self.f.show()
        self.close()



class Floor(QWidget):

    def __init__(self, parent, user):
        super().__init__()

        self.parent = parent
        self.user = user
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        self.resize(500,500)

        names = ['4', '3', '2', '1', '','','23','33',
                 '12', '', '11', '', '','','22','32',
                 '', '', '', '', '', '','21','31',
                 'Return', '', '', '','', '', '', '',
                 '', '', '', '','', '41', '51', '61',
                 '', '', '', '','', '42', '52', '62',
                 '', '', '', '','', '43', '53', '63']

        self.btn_group = QButtonGroup()
        positions = [(i, j) for i in range(7) for j in range(8)]
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            button.name = name
            self.btn_group.addButton(button)
            grid.addWidget(button, *position)

        self.btn_group.buttonClicked.connect(self.on_click)
        self.setWindowTitle('Floor Map - ' + self.user)

    def on_click(self,btn):

        if btn.name == 'Return':
            self.parent.show()
            self.close()
        else:
            self.table = Table(self, btn.name)
            self.table.show()
            self.close()



class Table(QWidget):

    def __init__(self, parent, number):
        super().__init__()

        self.parent = parent
        self.number = number

        self.initUI()

    def initUI(self):

        self.resize(500,500)
        self.setWindowTitle('Table ' + self.number + ' -' + self.parent.user)

        self.button = QPushButton('Return',self)
        self.button.move(25,450)
        self.button.clicked.connect(self.buttonClicked)

        self.buttonOpen = QPushButton('Open Ticket', self)
        self.buttonOpen.move(400,50)

    def buttonClicked(self):

        self.parent.show()
        self.close()



class Ticket(QWidget):

    def __init__(self, parent, number):
        super().__init__()







def main():
    app = QApplication(sys.argv)
    l = Login()
    l.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

