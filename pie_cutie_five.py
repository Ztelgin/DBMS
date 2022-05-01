import sys
from sqlite3 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import sqlite3

class Login(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ids = []
        self.initUI()

    def initUI(self):

        self.resize(500,500)
        self.setWindowTitle('Welcome')

        self.label = QLabel('Enter Login Number')
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.setCentralWidget(self.label)
        self.label.setMargin(20)


        self.msg = QMessageBox()
        self.msg.setWindowTitle('Error')
        self.msg.setText('Invalid ID')
        self.msg.setIcon(QMessageBox.Critical)

        self.textedit1 = QLineEdit('',self)
        self.textedit1.move(200,225)
        self.textedit1.setToolTip('For the purposes of this demo enter 12A for Server\n' +
                                    '... For Manager')
        self.textedit1.returnPressed.connect(self.buttonClicked)

        self.button = QPushButton('Login',self)
        self.button.move(200,275)
        self.button.clicked.connect(self.buttonClicked)

        # Database Connection
        self.connection = sqlite3.connect("RestaurantAutomation.db")
        cursor = self.connection.execute("select emp_id from Employee")
        for i, id in enumerate(cursor):

            if id[0] == '-999':
                continue
            self.ids.append(id[0])

    def buttonClicked(self):
        user = self.textedit1.text()
        if user not in self.ids:

            self.msg.exec_()
            self.textedit1.setText('')
            return

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

        # Database Connection
        self.owned = []
        self.connection = sqlite3.connect("RestaurantAutomation.db")
        cursor = self.connection.execute("select * from Top")
        for i, id in enumerate(cursor):
            if id[2] != '-999':
                self.owned.append(id[0])
        print(self.owned)

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
            if name in self.owned:
                button.setStyleSheet('Background-color:purple')
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



class Table(QMainWindow):

    def __init__(self, parent, number):
        super().__init__()

        self.parent = parent
        self.number = number

        self.initUI()

    def initUI(self):

        self.resize(500,500)
        self.setWindowTitle('Table ' + self.number + ' -' + self.parent.user)


        self.list = QListWidget()
        self.list.addItems(['Ticket 1','Ticket 2'])
        self.setCentralWidget(self.list)
        self.list.resize(150,150)


        self.buttonOpen = QPushButton('Open Ticket', self)
        self.buttonOpen.name = 'Open'
        self.buttonOpen.move(375,50)

        self.buttonReturn = QPushButton('Return',self)
        self.buttonReturn.name = 'Return'
        self.buttonReturn.move(25,450)

        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.buttonReturn)
        self.btn_group.addButton(self.buttonOpen)

        self.btn_group.buttonClicked.connect(self.on_click)


    def on_click(self, btn):
        if btn.name == 'Return':
            self.parent.show()
            self.close()
        else:
            self.t = Ticket(self,self.number,self.parent.user)
            self.t.show()
            self.close()



class Ticket(QMainWindow):

    def __init__(self, parent, number, user):
        super().__init__()

        self.parent = parent
        self.number = number
        self.user = user

        self.initUI()

    def initUI(self):

        self.resize(500,500)
        self.setWindowTitle('Table ' + self.number + ' Ticket 1 - ' + self.parent.parent.user)

        self.button = QPushButton('Return',self)
        self.button.move(25,450)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):

        self.parent.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    l = Login()
    l.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

