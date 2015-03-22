# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dag.ui'
#
# Created: Sun Mar 22 16:03:08 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(969, 674)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.Map = QtGui.QGraphicsView(Form)
        self.Map.setMaximumSize(QtCore.QSize(16777215, 687))
        self.Map.setSceneRect(QtCore.QRectF(0.0, 0.0, 1.0, 0.0))
        self.Map.setAlignment(QtCore.Qt.AlignCenter)
        self.Map.setObjectName(_fromUtf8("Map"))
        self.gridLayout.addWidget(self.Map, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 200, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.ArrowLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ArrowLabel.setFont(font)
        self.ArrowLabel.setObjectName(_fromUtf8("ArrowLabel"))
        self.verticalLayout.addWidget(self.ArrowLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.ArrowAmount = QtGui.QLCDNumber(Form)
        self.ArrowAmount.setObjectName(_fromUtf8("ArrowAmount"))
        self.verticalLayout.addWidget(self.ArrowAmount)
        self.GoldLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GoldLabel.setFont(font)
        self.GoldLabel.setObjectName(_fromUtf8("GoldLabel"))
        self.verticalLayout.addWidget(self.GoldLabel)
        self.GoldAmount = QtGui.QLCDNumber(Form)
        self.GoldAmount.setObjectName(_fromUtf8("GoldAmount"))
        self.verticalLayout.addWidget(self.GoldAmount)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.BtnMove = QtGui.QPushButton(Form)
        self.BtnMove.setObjectName(_fromUtf8("BtnMove"))
        self.verticalLayout.addWidget(self.BtnMove)
        self.BtnShoot = QtGui.QPushButton(Form)
        self.BtnShoot.setObjectName(_fromUtf8("BtnShoot"))
        self.verticalLayout.addWidget(self.BtnShoot)
        self.BtnUp = QtGui.QPushButton(Form)
        self.BtnUp.setObjectName(_fromUtf8("BtnUp"))
        self.verticalLayout.addWidget(self.BtnUp, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.BtnLeft = QtGui.QPushButton(Form)
        self.BtnLeft.setObjectName(_fromUtf8("BtnLeft"))
        self.horizontalLayout_2.addWidget(self.BtnLeft)
        self.BtnDown = QtGui.QPushButton(Form)
        self.BtnDown.setObjectName(_fromUtf8("BtnDown"))
        self.horizontalLayout_2.addWidget(self.BtnDown)
        self.BtnRight = QtGui.QPushButton(Form)
        self.BtnRight.setObjectName(_fromUtf8("BtnRight"))
        self.horizontalLayout_2.addWidget(self.BtnRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 5, 2, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 6, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ArrowLabel.setText(_translate("Form", "Arrows", None))
        self.GoldLabel.setText(_translate("Form", "Gold", None))
        self.BtnMove.setText(_translate("Form", "Move", None))
        self.BtnShoot.setText(_translate("Form", "Shoot", None))
        self.BtnUp.setText(_translate("Form", "Up", None))
        self.BtnLeft.setText(_translate("Form", "Left", None))
        self.BtnDown.setText(_translate("Form", "Down", None))
        self.BtnRight.setText(_translate("Form", "Right", None))

