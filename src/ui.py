# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display_label = QtWidgets.QLabel(self.centralwidget)
        self.display_label.setGeometry(QtCore.QRect(20, 20, 751, 371))
        self.display_label.setStyleSheet("")
        self.display_label.setScaledContents(True)
        self.display_label.setObjectName("display_label")
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setGeometry(QtCore.QRect(10, 440, 89, 25))
        self.prev_button.setObjectName("prev_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(680, 440, 89, 25))
        self.next_button.setObjectName("next_button")
        self.s_label = QtWidgets.QLabel(self.centralwidget)
        self.s_label.setGeometry(QtCore.QRect(170, 450, 21, 21))
        self.s_label.setObjectName("s_label")
        self.tx_label = QtWidgets.QLabel(self.centralwidget)
        self.tx_label.setGeometry(QtCore.QRect(310, 450, 31, 17))
        self.tx_label.setObjectName("tx_label")
        self.ty_label = QtWidgets.QLabel(self.centralwidget)
        self.ty_label.setGeometry(QtCore.QRect(490, 450, 31, 17))
        self.ty_label.setObjectName("ty_label")
        self.params_button = QtWidgets.QPushButton(self.centralwidget)
        self.params_button.setGeometry(QtCore.QRect(280, 510, 181, 25))
        self.params_button.setObjectName("params_button")
        # self.s_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        # self.s_input.setGeometry(QtCore.QRect(210, 440, 69, 31))
        # self.s_input.setObjectName("s_input")
        # self.tx_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        # self.tx_input.setGeometry(QtCore.QRect(350, 440, 69, 31))
        # self.tx_input.setObjectName("tx_input")
        # self.ty_input = QtWidgets.QDoubleSpinBox(self.centralwidget)
        # self.ty_input.setGeometry(QtCore.QRect(540, 440, 69, 31))
        # self.ty_input.setObjectName("ty_input")
        self.frame_info_label = QtWidgets.QLabel(self.centralwidget)
        self.frame_info_label.setGeometry(QtCore.QRect(660, 410, 121, 21))
        self.frame_info_label.setObjectName("frame_info_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frame viewer"))
        self.display_label.setText(_translate("MainWindow", "Frames"))
        self.prev_button.setText(_translate("MainWindow", "Previous"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.s_label.setText(_translate("MainWindow", "S :"))
        self.tx_label.setText(_translate("MainWindow", "tx :"))
        self.ty_label.setText(_translate("MainWindow", "ty :"))
        self.params_button.setText(_translate("MainWindow", "Change Parameters"))
        self.frame_info_label.setText(_translate("MainWindow", "0/total"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

