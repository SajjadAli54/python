# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 180, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(10, 50, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 451, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelDefaultRef = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDefaultRef.setObjectName("labelDefaultRef")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDefaultRef)
        self.comboBoxDefaultRef = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBoxDefaultRef.setObjectName("comboBoxDefaultRef")
        self.comboBoxDefaultRef.addItem("")
        self.comboBoxDefaultRef.addItem("")
        self.comboBoxDefaultRef.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxDefaultRef)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelTitle.setText(_translate("Dialog", "Configuration Settings"))
        self.labelDefaultRef.setText(_translate("Dialog", "Default Currency Reference"))
        self.comboBoxDefaultRef.setItemText(0, _translate("Dialog", "USD"))
        self.comboBoxDefaultRef.setItemText(1, _translate("Dialog", "PHP"))
        self.comboBoxDefaultRef.setItemText(2, _translate("Dialog", "IDR"))
