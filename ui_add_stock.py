# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_stockSoFPnJ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AddStock_Dialog(object):
    def setupUi(self, AddStock_Dialog):
        if not AddStock_Dialog.objectName():
            AddStock_Dialog.setObjectName(u"AddStock_Dialog")
        AddStock_Dialog.resize(400, 350)
        AddStock_Dialog.setMaximumSize(QSize(400, 350))
        self.verticalLayout = QVBoxLayout(AddStock_Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(AddStock_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(298, 16777215))
        font = QFont()
        font.setFamilies([u"Satoshi Black"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: black;")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.content_frame = QFrame(self.widget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.content_frame)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 10, 0, 9)
        self.frame_3 = QFrame(self.content_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.productname_lineEdit = QLineEdit(self.frame_3)
        self.productname_lineEdit.setObjectName(u"productname_lineEdit")
        self.productname_lineEdit.setMinimumSize(QSize(298, 45))
        self.productname_lineEdit.setMaximumSize(QSize(298, 45))
        font1 = QFont()
        font1.setFamilies([u"Satoshi"])
        self.productname_lineEdit.setFont(font1)
        self.productname_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.productname_lineEdit, 0, 0, 1, 1)

        self.newquantity_lineEdit = QLineEdit(self.frame_3)
        self.newquantity_lineEdit.setObjectName(u"newquantity_lineEdit")
        self.newquantity_lineEdit.setMinimumSize(QSize(298, 45))
        self.newquantity_lineEdit.setMaximumSize(QSize(298, 45))
        self.newquantity_lineEdit.setFont(font1)
        self.newquantity_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.newquantity_lineEdit, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)

        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.content_frame, 1, 0, 1, 1)

        self.bottom_frame = QFrame(self.widget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 100))
        self.bottom_frame.setMaximumSize(QSize(16777215, 100))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bottom_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(50, 0, 50, 10)
        self.cancel_btn = QPushButton(self.bottom_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 45))
        self.cancel_btn.setMaximumSize(QSize(143, 45))
        font2 = QFont()
        font2.setFamilies([u"Satoshi Medium"])
        font2.setPointSize(10)
        self.cancel_btn.setFont(font2)
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.cancel_btn, 0, 0, 1, 1)

        self.save_btn = QPushButton(self.bottom_frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 45))
        self.save_btn.setMaximumSize(QSize(143, 45))
        self.save_btn.setFont(font2)
        self.save_btn.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #191919;\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.save_btn, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.bottom_frame, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AddStock_Dialog)
        self.cancel_btn.clicked.connect(AddStock_Dialog.close)

        QMetaObject.connectSlotsByName(AddStock_Dialog)
    # setupUi

    def retranslateUi(self, AddStock_Dialog):
        AddStock_Dialog.setWindowTitle(QCoreApplication.translate("AddStock_Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("AddStock_Dialog", u"Add Stock", None))
        self.productname_lineEdit.setText("")
        self.productname_lineEdit.setPlaceholderText(QCoreApplication.translate("AddStock_Dialog", u"Product Name", None))
        self.newquantity_lineEdit.setText("")
        self.newquantity_lineEdit.setPlaceholderText(QCoreApplication.translate("AddStock_Dialog", u"Quantity", None))
        self.label_2.setText(QCoreApplication.translate("AddStock_Dialog", u"Quantity", None))
        self.label.setText(QCoreApplication.translate("AddStock_Dialog", u"Product Name", None))
        self.cancel_btn.setText(QCoreApplication.translate("AddStock_Dialog", u"CANCEL", None))
        self.save_btn.setText(QCoreApplication.translate("AddStock_Dialog", u"SAVE", None))
    # retranslateUi

