# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoinsertconfig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(297, 248)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 276, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        
        self.targetBpbetweenSkipBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.targetBpbetweenSkipBox.setMaximum(10000)
        self.targetBpbetweenSkipBox.setProperty("value", 7)
        self.targetBpbetweenSkipBox.setObjectName("targetBpbetweenSkipBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.targetBpbetweenSkipBox)
        self.targetBpBetweenSkipLabel = QtWidgets.QLabel(self.layoutWidget)
        self.targetBpBetweenSkipLabel.setObjectName("targetBpBetweenSkipLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.targetBpBetweenSkipLabel)
        self.numOfSkipLabel = QtWidgets.QLabel(self.layoutWidget)
        self.numOfSkipLabel.setObjectName("numOfSkipLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numOfSkipLabel)
        self.numOfSkipBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.numOfSkipBox.setMaximum(2)
        self.numOfSkipBox.setProperty("value", 1)
        self.numOfSkipBox.setObjectName("numOfSkipBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numOfSkipBox)
        self.initialPositionLabel = QtWidgets.QLabel(self.layoutWidget)
        self.initialPositionLabel.setObjectName("initialPositionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.initialPositionLabel)
        self.initialPositionBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.initialPositionBox.setMinimum(2)
        self.initialPositionBox.setMaximum(10000)
        self.initialPositionBox.setProperty("value", 7)
        self.initialPositionBox.setObjectName("initialPositionBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.initialPositionBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.targetBpbetweenSkipBox, self.numOfSkipBox)
        Dialog.setTabOrder(self.numOfSkipBox, self.initialPositionBox)
        Dialog.setTabOrder(self.initialPositionBox, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose autoskip parameters:"))
        self.targetBpBetweenSkipLabel.setText(_translate("Dialog", "target bps between skip"))
        self.numOfSkipLabel.setText(_translate("Dialog", "number of skip"))
        self.initialPositionLabel.setText(_translate("Dialog", "min distance to edge"))

