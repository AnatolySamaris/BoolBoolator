# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 10pt;\n"
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
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.BoolTable = QtWidgets.QTableWidget(self.centralwidget)
        self.BoolTable.setGeometry(QtCore.QRect(10, 10, 460, 600))
        self.BoolTable.verticalHeader().setVisible(False)
        self.BoolTable.setStyleSheet("QHeaderView::section {\n"
"    background-color: #121212;\n"
"    color: white;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600\n"
"}")
        self.BoolTable.setObjectName("BoolTable")
        self.BoolTable.setColumnCount(0)
        self.BoolTable.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BoolBoolator - Table"))
