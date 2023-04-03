import sys
from pyperclip import copy

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect

from input import Ui_MainWindow as InputWindow
from result import Ui_MainWindow as ResultWindow
from table import Ui_MainWindow as TableWindow

from dealwithbool import BoolExp


def delete_spaces(expression):
    exp = ''
    for i in expression:
        if i == ' ':
            continue
        exp += i
    return exp


class Input(QtWidgets.QMainWindow):
    def __init__(self):
        super(Input, self).__init__()
        self.ui = InputWindow()
        self.ui.setupUi(self)
        self.Expression = self.ui.Expression

        self.ui.Negation.clicked.connect(self.add_negation)
        self.ui.Conjunction.clicked.connect(self.add_conjunction)
        self.ui.Disjunction.clicked.connect(self.add_disjunction)
        self.ui.Equivalence.clicked.connect(self.add_equivalence)
        self.ui.Zero.clicked.connect(self.add_zero)
        self.ui.One.clicked.connect(self.add_one)

        self.ui.Implication.clicked.connect(self.add_implication)
        self.ui.Mod2.clicked.connect(self.add_mod_2)
        self.ui.Pier.clicked.connect(self.add_pier)
        self.ui.Schaeffer.clicked.connect(self.add_schaeffer)
        self.ui.Calculate.clicked.connect(self.calculate)
        self.ui.MakeX.clicked.connect(self.add_x)
        self.ui.MakeY.clicked.connect(self.add_y)
        self.ui.MakeZ.clicked.connect(self.add_z)
        self.ui.MakeT.clicked.connect(self.add_t)

        self.ui.OpenBracket.clicked.connect(self.add_open)
        self.ui.CloseBracket.clicked.connect(self.add_close)
        self.ui.CleanLine.clicked.connect(self.clear)
        self.ui.BackSpace.clicked.connect(self.backspace)

    def add_negation(self):
        self.Expression.setText(self.Expression.text() + '¬')

    def add_conjunction(self):
        self.Expression.setText(self.Expression.text() + '∧')

    def add_disjunction(self):
        self.Expression.setText(self.Expression.text() + '∨')

    def add_equivalence(self):
        self.Expression.setText(self.Expression.text() + '~')

    def add_implication(self):
        self.Expression.setText(self.Expression.text() + '→')

    def add_mod_2(self):
        self.Expression.setText(self.Expression.text() + '⊕')

    def add_pier(self):
        self.Expression.setText(self.Expression.text() + '↓')

    def add_schaeffer(self):
        self.Expression.setText(self.Expression.text() + '|')

    def add_zero(self):
        self.Expression.setText(self.Expression.text() + '0')

    def add_one(self):
        self.Expression.setText(self.Expression.text() + '1')

    def add_x(self):
        self.Expression.setText(self.Expression.text() + 'x')

    def add_y(self):
        self.Expression.setText(self.Expression.text() + 'y')

    def add_z(self):
        self.Expression.setText(self.Expression.text() + 'z')

    def add_t(self):
        self.Expression.setText(self.Expression.text() + 't')

    def add_open(self):
        self.Expression.setText(self.Expression.text() + '(')

    def add_close(self):
        self.Expression.setText(self.Expression.text() + ')')

    def clear(self):
        self.Expression.setText('')

    def backspace(self):
        self.Expression.setText(self.Expression.text()[:-1])

    def calculate(self):
        exp = BoolExp(delete_spaces(self.Expression.text()), 'advanced')
        if not any([i.isalpha() for i in self.Expression.text()]):
            self.Expression.setText(str(exp.evaluate()))
        else:
            self.ui.Result = Result(exp)
            self.ui.Table = Table(exp)
            self.ui.Result.show()
            self.ui.Table.show()


class Result(QtWidgets.QMainWindow):
    def __init__(self, exp: BoolExp):
        super(Result, self).__init__()
        self.ui = ResultWindow()
        self.ui.setupUi(self)
        self.ui.OriginalExp.append(exp.expression)
        self.exp = exp
        self.result = exp.calculate()

        self.ui.Zhegalkin.append(self.exp.get_zhegalkin(self.result, pretty=True))
        self.ui.PDNF.append(self.exp.get_pnf(self.result, pnf_mode='pdnf', pretty=True))
        self.ui.PCNF.append(self.exp.get_pnf(self.result, pnf_mode='pcnf', pretty=True))
        self.ui.Classes.append(' '.join(self.exp.get_classes(self.result)))

        self.ui.CopyZhegalkin.clicked.connect(self.copy_zhegalkin)
        self.ui.CopyPDNF.clicked.connect(self.copy_pdnf)
        self.ui.CopyPCNF.clicked.connect(self.copy_pcnf)
        self.ui.CopyFunc.clicked.connect(self.copy_func)

    def copy_zhegalkin(self):
        copy(self.ui.Zhegalkin.toPlainText())

    def copy_pdnf(self):
        copy(self.ui.PDNF.toPlainText())

    def copy_pcnf(self):
        copy(self.ui.PCNF.toPlainText())

    def copy_func(self):
        copy(self.ui.OriginalExp.toPlainText())


class Table(QtWidgets.QMainWindow):
    def __init__(self, exp: BoolExp):
        super(Table, self).__init__()
        self.ui = TableWindow()
        self.ui.setupUi(self)
        self.result = exp.calculate()
        self.column_names = exp.variables + ['f(...)']

        self.ui.BoolTable.horizontalHeader()

        self.ui.BoolTable.setRowCount(len(self.result))
        self.ui.BoolTable.setColumnCount(len(self.column_names))
        self.ui.BoolTable.setHorizontalHeaderLabels(self.column_names)

        for i in range(len(self.result)):
            self.ui.BoolTable.setRowHeight(i, 30)
        for i in range(len(self.column_names)):
            self.ui.BoolTable.setColumnWidth(i, 100)

        for row in range(len(self.result)):
            for col in range(len(self.column_names)):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(Qt.AlignCenter)
                item.setText(str(self.result[row][col]))
                self.ui.BoolTable.setItem(row, col, item)

        if len(self.column_names) * 30 + 90 > 900:
            self.ui.BoolTable.setGeometry(QRect(10, 10, len(self.column_names) * 100 + 40, 900))
            self.resize(len(self.column_names) * 100 + 50, 910)
        else:
            self.ui.BoolTable.setGeometry(QRect(10, 10, len(self.column_names) * 100 + 40, len(self.result) * 30 + 90))
            self.resize(len(self.column_names) * 100 + 50, len(self.result) * 30 + 100)


app = QtWidgets.QApplication(sys.argv)

window = Input()
window.show()

sys.exit(app.exec())
