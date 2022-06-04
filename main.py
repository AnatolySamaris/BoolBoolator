import sys
from pyperclip import copy

from PyQt5 import uic
from PyQt5 import QtWidgets
from module import Decider
from design import Ui_MainWindow_1
from table import Ui_MainWindow_2
from answer import Ui_MainWindow_3


def delete_spaces(expression):
		exp = ''
		for i in expression:
			if i == ' ':
				continue
			exp += i
		return exp


class Calculator(QtWidgets.QMainWindow):
	def __init__(self):
		super(Calculator, self).__init__()
		uic.loadUi('design.ui', self)
		self.ui = Ui_MainWindow_1()
		self.ui.setupUi(self)
		self.Expression = self.ui.Expression
		self.ui.Conjunction.clicked.connect(self.Add_Conjunction)
		self.ui.Disjunction.clicked.connect(self.Add_Disjunction)
		self.ui.Equivalence.clicked.connect(self.Add_Equivalence)
		self.ui.Implication.clicked.connect(self.Add_Implication)
		self.ui.Mod_2.clicked.connect(self.Add_Mod_2)
		self.ui.Negation.clicked.connect(self.Add_Negation)
		self.ui.Pier.clicked.connect(self.Add_Pier)
		self.ui.Schaeffer.clicked.connect(self.Add_Schaeffer)
		self.ui.Calculate.clicked.connect(self.Calculate_It)
		self.ui.Make_x.clicked.connect(self.Add_x)
		self.ui.Make_y.clicked.connect(self.Add_y)
		self.ui.Make_z.clicked.connect(self.Add_z)
		self.ui.Make_t.clicked.connect(self.Add_t)
		self.ui.OpenBracket.clicked.connect(self.Add_Open)
		self.ui.CloseBracket.clicked.connect(self.Add_Close)
		self.ui.Clean_line.clicked.connect(self.Clear)
		self.ui.BackSpace.clicked.connect(self.Backspace)
		self.ui.Ans = None

	def Add_Conjunction(self):
		text = self.Expression.text()
		self.Expression.setText(text + '∧')

	def Add_Disjunction(self):
		self.Expression.setText(self.Expression.text() + '∨')

	def Add_Equivalence(self):
		self.Expression.setText(self.Expression.text() + '~')

	def Add_Implication(self):
		self.Expression.setText(self.Expression.text() + '→')	

	def Add_Mod_2(self):
		self.Expression.setText(self.Expression.text() + '⊕')

	def Add_Pier(self):
		self.Expression.setText(self.Expression.text() + '↓')

	def Add_Schaeffer(self):
		self.Expression.setText(self.Expression.text() + '|')

	def Add_Negation(self):
		self.Expression.setText(self.Expression.text() + '¬')

	def Add_x(self):
		self.Expression.setText(self.Expression.text() + 'x')

	def Add_y(self):
		self.Expression.setText(self.Expression.text() + 'y')

	def Add_z(self):
		self.Expression.setText(self.Expression.text() + 'z')

	def Add_t(self):
		self.Expression.setText(self.Expression.text() + 't')

	def Add_Open(self):
		self.Expression.setText(self.Expression.text() + '(')

	def Add_Close(self):
		self.Expression.setText(self.Expression.text() + ')')

	def Clear(self):
		self.Expression.setText('')

	def Backspace(self):
		self.Expression.setText(self.Expression.text()[:-1])

	def Calculate_It(self):
		exp = self.Expression.text()

		self.ui.Ans = Answer(exp)
		self.ui.Ans.show()


class Answer(QtWidgets.QMainWindow):
	def __init__(self, exp):
		super(Answer, self).__init__()
		uic.loadUi('table.ui', self)
		self.ui = Ui_MainWindow_2()
		self.ui.setupUi(self)
		self.exp = exp
		self.ui.OrigExp.append(self.exp)
		self.ui.Page = None

		self.expression = Decider(delete_spaces(self.exp))
		self.expression.make_table(self.expression.get_size())
		self.expression.pdnf_pcnf()
		self.expression.Zhegalkin()
		self.expression.get_classes()
		self.expression.make_carnot()
		self.expression.minimization()
		self.expression.evaluate(self.expression.ans_pdnf, 'shaef')
		self.expression.prepare_ans()
		
		self.ui.Zhegalkin.append(self.expression.zhegalkin)
		self.ui.PDNF.append(self.expression.ans_pdnf)
		self.ui.PCNF.append(self.expression.ans_pcnf)
		self.ui.Table.append(self.expression.ans)
		self.ui.Classes.append(self.expression.classes)

		self.ui.Next.clicked.connect(self.Show_New)
		self.ui.Copy_Zhegalkin.clicked.connect(self.copy_zhegalkin)
		self.ui.Copy_PDNF.clicked.connect(self.copy_pdnf)
		self.ui.Copy_PCNF.clicked.connect(self.copy_pcnf)
		self.ui.Copy_Func.clicked.connect(self.copy_func)
		

	def Show_New(self):
		self.ui.Page = Second_Ans(self.expression.ans_carnot, self.expression.min_pdnf,
								self.expression.min_pcnf, self.expression.schaef_basis)
		self.ui.Page.show()


	def copy_zhegalkin(self):
		copy(self.ui.Zhegalkin.toPlainText())

	def copy_pdnf(self):
		copy(self.ui.PDNF.toPlainText())

	def copy_pcnf(self):
		copy(self.ui.PCNF.toPlainText())

	def copy_func(self):
		copy(self.ui.OrigExp.toPlainText())
		
	
class Second_Ans(QtWidgets.QMainWindow):
	def __init__(self, carnot, min_pdnf, min_pcnf, schaef):
		super(Second_Ans, self).__init__()
		uic.loadUi('answer.ui', self)
		self.ui = Ui_MainWindow_3()
		self.ui.setupUi(self)

		self.ui.Carnot.append(carnot)
		self.ui.MinPDNF.append(min_pdnf)
		self.ui.MinPCNF.append(min_pcnf)
		self.ui.SchaefBasis.append(schaef)

		self.ui.Copy_MIN_PDNF.clicked.connect(self.Copy_min_pdnf)
		self.ui.Copy_MIN_PCNF.clicked.connect(self.Copy_min_pcnf)

	def Copy_min_pdnf(self):
		copy(self.ui.MinPDNF.toPlainText())

	def Copy_min_pcnf(self):
		copy(self.ui.MinPCNF.toPlainText())


app = QtWidgets.QApplication(sys.argv)

window = Calculator()
window.show()

sys.exit(app.exec())

