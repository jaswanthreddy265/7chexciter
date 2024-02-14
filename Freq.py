# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U_I.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Dwell_Time = QtWidgets.QLineEdit(self.centralwidget)
        self.Dwell_Time.setGeometry(QtCore.QRect(180, 230, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Dwell_Time.setFont(font)
        self.Dwell_Time.setObjectName("Dwell_Time")
        self.Start_Frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_Frequency.setGeometry(QtCore.QRect(180, 50, 125, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Start_Frequency.setFont(font)
        self.Start_Frequency.setObjectName("Start_Frequency")
        self.Stop_Frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.Stop_Frequency.setGeometry(QtCore.QRect(180, 110, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Stop_Frequency.setFont(font)
        self.Stop_Frequency.setObjectName("Stop_Frequency")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(130, 290, 75, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.CB_Start_Freq = QtWidgets.QComboBox(self.centralwidget)
        self.CB_Start_Freq.setEnabled(False)
        self.CB_Start_Freq.setGeometry(QtCore.QRect(320, 50, 69, 40))
        self.CB_Start_Freq.setObjectName("CB_Start_Freq")
        self.CB_Start_Freq.addItem("")
        self.CB_Stop_Freq = QtWidgets.QComboBox(self.centralwidget)
        self.CB_Stop_Freq.setEnabled(False)
        self.CB_Stop_Freq.setGeometry(QtCore.QRect(320, 110, 69, 40))
        self.CB_Stop_Freq.setObjectName("CB_Stop_Freq")
        self.CB_Stop_Freq.addItem("")
        self.CB_Bandwidth = QtWidgets.QComboBox(self.centralwidget)
        self.CB_Bandwidth.setGeometry(QtCore.QRect(178, 170, 121, 40))
        self.CB_Bandwidth.setObjectName("CB_Bandwidth")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_Bandwidth.addItem("")
        self.CB_dt = QtWidgets.QComboBox(self.centralwidget)
        self.CB_dt.setGeometry(QtCore.QRect(320, 230, 69, 40))
        self.CB_dt.setObjectName("CB_dt")
        self.CB_dt.addItem("")
        self.CB_dt.addItem("")
        self.CB_dt.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Start_Frequency, self.Stop_Frequency)
        MainWindow.setTabOrder(self.Stop_Frequency, self.CB_Bandwidth)
        MainWindow.setTabOrder(self.CB_Bandwidth, self.Dwell_Time)
        MainWindow.setTabOrder(self.Dwell_Time, self.CB_dt)
        MainWindow.setTabOrder(self.CB_dt, self.Save)
        MainWindow.setTabOrder(self.Save, self.CB_Stop_Freq)
        MainWindow.setTabOrder(self.CB_Stop_Freq, self.CB_Start_Freq)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Start Frequency"))
        self.label_2.setText(_translate("MainWindow", "Stop Frequency"))
        self.label_3.setText(_translate("MainWindow", "Noise Bandwidth"))
        self.label_4.setText(_translate("MainWindow", "Dweel Time"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.CB_Start_Freq.setItemText(0, _translate("MainWindow", "MHz"))
        self.CB_Stop_Freq.setItemText(0, _translate("MainWindow", "MHz"))
        self.CB_Bandwidth.setItemText(0, _translate("MainWindow", "0 KHz"))
        self.CB_Bandwidth.setItemText(1, _translate("MainWindow", "1 KHz"))
        self.CB_Bandwidth.setItemText(2, _translate("MainWindow", "2 KHz"))
        self.CB_Bandwidth.setItemText(3, _translate("MainWindow", "3 KHz"))
        self.CB_Bandwidth.setItemText(4, _translate("MainWindow", "5 KHz"))
        self.CB_Bandwidth.setItemText(5, _translate("MainWindow", "10 KHz"))
        self.CB_Bandwidth.setItemText(6, _translate("MainWindow", "15 KHz"))
        self.CB_Bandwidth.setItemText(7, _translate("MainWindow", "30 KHz"))
        self.CB_Bandwidth.setItemText(8, _translate("MainWindow", "50 KHz"))
        self.CB_Bandwidth.setItemText(9, _translate("MainWindow", "100 KHz"))
        self.CB_Bandwidth.setItemText(10, _translate("MainWindow", "200 KHz"))
        self.CB_Bandwidth.setItemText(11, _translate("MainWindow", "500 KHz"))
        self.CB_Bandwidth.setItemText(12, _translate("MainWindow", "1 MHz"))
        self.CB_Bandwidth.setItemText(13, _translate("MainWindow", "2 MHz"))
        self.CB_Bandwidth.setItemText(14, _translate("MainWindow", "3 MHz"))
        self.CB_dt.setItemText(0, _translate("MainWindow", "μs"))
        self.CB_dt.setItemText(1, _translate("MainWindow", "ns"))
        self.CB_dt.setItemText(2, _translate("MainWindow", "ms"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())