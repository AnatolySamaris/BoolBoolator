# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
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
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 115, 20))
        self.label.setObjectName("label")
        self.Carnot = QtWidgets.QTextEdit(self.centralwidget)
        self.Carnot.setGeometry(QtCore.QRect(20, 40, 280, 130))
        self.Carnot.setReadOnly(True)
        self.Carnot.setObjectName("Carnot")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 340, 240, 20))
        self.label_2.setObjectName("label_2")
        self.MinPDNF = QtWidgets.QTextEdit(self.centralwidget)
        self.MinPDNF.setGeometry(QtCore.QRect(20, 370, 860, 60))
        self.MinPDNF.setReadOnly(True)
        self.MinPDNF.setObjectName("MinPDNF")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 450, 240, 20))
        self.label_3.setObjectName("label_3")
        self.MinPCNF = QtWidgets.QTextEdit(self.centralwidget)
        self.MinPCNF.setGeometry(QtCore.QRect(20, 480, 860, 60))
        self.MinPCNF.setReadOnly(True)
        self.MinPCNF.setObjectName("MinPCNF")
        self.SchaefBasis = QtWidgets.QTextEdit(self.centralwidget)
        self.SchaefBasis.setGeometry(QtCore.QRect(310, 40, 500, 60))
        self.SchaefBasis.setReadOnly(True)
        self.SchaefBasis.setObjectName("SchaefBasis")
        self.PierBasis = QtWidgets.QTextEdit(self.centralwidget)
        self.PierBasis.setGeometry(QtCore.QRect(310, 170, 500, 60))
        self.PierBasis.setReadOnly(True)
        self.PierBasis.setObjectName("PierBasis")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 310, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 140, 260, 20))
        self.label_5.setObjectName("label_5")
        self.Copy_MIN_PDNF = QtWidgets.QPushButton(self.centralwidget)
        self.Copy_MIN_PDNF.setGeometry(QtCore.QRect(760, 430, 120, 28))
        self.Copy_MIN_PDNF.setObjectName("Copy_MIN_PDNF")
        self.Copy_MIN_PCNF = QtWidgets.QPushButton(self.centralwidget)
        self.Copy_MIN_PCNF.setGeometry(QtCore.QRect(760, 540, 120, 28))
        self.Copy_MIN_PCNF.setObjectName("Copy_MIN_PCNF")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "?????????? ??????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????????????????????? ????????:"))
        self.label_3.setText(_translate("MainWindow", "???????????????????????????????? ????????:"))
        self.label_4.setText(_translate("MainWindow", "???????????????????? ???? ???????????? ??????????????:"))
        self.label_5.setText(_translate("MainWindow", "???????????????????? ???? ???????????? ??????????:"))
        self.Copy_MIN_PDNF.setText(_translate("MainWindow", "????????????????????"))
        self.Copy_MIN_PCNF.setText(_translate("MainWindow", "????????????????????"))
