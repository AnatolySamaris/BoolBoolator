# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/calculate_black_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #49423d;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:!hover {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #24b3a7;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Expression = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Expression.sizePolicy().hasHeightForWidth())
        self.Expression.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Expression.setFont(font)
        self.Expression.setStyleSheet("QLineEdit {\n"
"    background-color: #FFF;\n"
"    color: black;\n"
"    font-size: 24pt;\n"
"}")
        self.Expression.setMaxLength(128)
        self.Expression.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Expression.setObjectName("Expression")
        self.verticalLayout.addWidget(self.Expression)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CloseBracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseBracket.sizePolicy().hasHeightForWidth())
        self.CloseBracket.setSizePolicy(sizePolicy)
        self.CloseBracket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseBracket.setStyleSheet("")
        self.CloseBracket.setObjectName("CloseBracket")
        self.gridLayout.addWidget(self.CloseBracket, 2, 1, 1, 1)
        self.Equivalence = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Equivalence.sizePolicy().hasHeightForWidth())
        self.Equivalence.setSizePolicy(sizePolicy)
        self.Equivalence.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Equivalence.setStyleSheet("")
        self.Equivalence.setObjectName("Equivalence")
        self.gridLayout.addWidget(self.Equivalence, 1, 1, 1, 1)
        self.Negation = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Negation.sizePolicy().hasHeightForWidth())
        self.Negation.setSizePolicy(sizePolicy)
        self.Negation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Negation.setStyleSheet("")
        self.Negation.setObjectName("Negation")
        self.gridLayout.addWidget(self.Negation, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Make_y = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Make_y.sizePolicy().hasHeightForWidth())
        self.Make_y.setSizePolicy(sizePolicy)
        self.Make_y.setObjectName("Make_y")
        self.verticalLayout_3.addWidget(self.Make_y)
        self.Make_t = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Make_t.sizePolicy().hasHeightForWidth())
        self.Make_t.setSizePolicy(sizePolicy)
        self.Make_t.setObjectName("Make_t")
        self.verticalLayout_3.addWidget(self.Make_t)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 3, 1, 1)
        self.Pier = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pier.sizePolicy().hasHeightForWidth())
        self.Pier.setSizePolicy(sizePolicy)
        self.Pier.setObjectName("Pier")
        self.gridLayout.addWidget(self.Pier, 1, 3, 1, 1)
        self.Mod_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mod_2.sizePolicy().hasHeightForWidth())
        self.Mod_2.setSizePolicy(sizePolicy)
        self.Mod_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mod_2.setStyleSheet("QPushButton {\n"
"    font-size: 48px;\n"
"}\n"
"")
        self.Mod_2.setObjectName("Mod_2")
        self.gridLayout.addWidget(self.Mod_2, 1, 2, 1, 1)
        self.Disjunction = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Disjunction.sizePolicy().hasHeightForWidth())
        self.Disjunction.setSizePolicy(sizePolicy)
        self.Disjunction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Disjunction.setStyleSheet("")
        self.Disjunction.setObjectName("Disjunction")
        self.gridLayout.addWidget(self.Disjunction, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Make_x = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Make_x.sizePolicy().hasHeightForWidth())
        self.Make_x.setSizePolicy(sizePolicy)
        self.Make_x.setObjectName("Make_x")
        self.verticalLayout_2.addWidget(self.Make_x)
        self.Make_z = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Make_z.sizePolicy().hasHeightForWidth())
        self.Make_z.setSizePolicy(sizePolicy)
        self.Make_z.setObjectName("Make_z")
        self.verticalLayout_2.addWidget(self.Make_z)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 1, 1)
        self.Schaeffer = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Schaeffer.sizePolicy().hasHeightForWidth())
        self.Schaeffer.setSizePolicy(sizePolicy)
        self.Schaeffer.setObjectName("Schaeffer")
        self.gridLayout.addWidget(self.Schaeffer, 0, 3, 1, 1)
        self.OpenBracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenBracket.sizePolicy().hasHeightForWidth())
        self.OpenBracket.setSizePolicy(sizePolicy)
        self.OpenBracket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenBracket.setStyleSheet("")
        self.OpenBracket.setObjectName("OpenBracket")
        self.gridLayout.addWidget(self.OpenBracket, 2, 0, 1, 1)
        self.Implication = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Implication.sizePolicy().hasHeightForWidth())
        self.Implication.setSizePolicy(sizePolicy)
        self.Implication.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Implication.setStyleSheet("")
        self.Implication.setObjectName("Implication")
        self.gridLayout.addWidget(self.Implication, 1, 0, 1, 1)
        self.Conjunction = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Conjunction.sizePolicy().hasHeightForWidth())
        self.Conjunction.setSizePolicy(sizePolicy)
        self.Conjunction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Conjunction.setStyleSheet("")
        self.Conjunction.setObjectName("Conjunction")
        self.gridLayout.addWidget(self.Conjunction, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setObjectName("Calculate")
        self.horizontalLayout.addWidget(self.Calculate)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BackSpace = QtWidgets.QPushButton(self.centralwidget)
        self.BackSpace.setMaximumSize(QtCore.QSize(115, 16777215))
        self.BackSpace.setObjectName("BackSpace")
        self.horizontalLayout_2.addWidget(self.BackSpace)
        self.Clean_line = QtWidgets.QPushButton(self.centralwidget)
        self.Clean_line.setMaximumSize(QtCore.QSize(115, 16777215))
        self.Clean_line.setObjectName("Clean_line")
        self.horizontalLayout_2.addWidget(self.Clean_line)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logical Calculator"))
        self.CloseBracket.setText(_translate("MainWindow", ")"))
        self.Equivalence.setText(_translate("MainWindow", "~"))
        self.Negation.setText(_translate("MainWindow", "¬"))
        self.Make_y.setText(_translate("MainWindow", "y"))
        self.Make_t.setText(_translate("MainWindow", "t"))
        self.Pier.setText(_translate("MainWindow", "↓"))
        self.Mod_2.setText(_translate("MainWindow", "⊕"))
        self.Disjunction.setText(_translate("MainWindow", "∨"))
        self.Make_x.setText(_translate("MainWindow", "x"))
        self.Make_z.setText(_translate("MainWindow", "z"))
        self.Schaeffer.setText(_translate("MainWindow", "|"))
        self.OpenBracket.setText(_translate("MainWindow", "("))
        self.Implication.setText(_translate("MainWindow", "→"))
        self.Conjunction.setText(_translate("MainWindow", "∧"))
        self.Calculate.setText(_translate("MainWindow", "="))
        self.BackSpace.setText(_translate("MainWindow", "<<<"))
        self.Clean_line.setText(_translate("MainWindow", "Clean"))