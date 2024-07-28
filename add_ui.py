# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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

class Ui_Add_Dialog(object):
    def setupUi(self, Add_Dialog):
        if not Add_Dialog.objectName():
            Add_Dialog.setObjectName(u"Add_Dialog")
        Add_Dialog.resize(400, 550)
        self.verticalLayout = QVBoxLayout(Add_Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Add_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.widget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 100))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.top_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.top_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(298, 16777215))
        font = QFont()
        font.setFamilies([u"Satoshi Black"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: black;")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 1)

        self.bottom_frame = QFrame(self.widget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 100))
        self.bottom_frame.setMaximumSize(QSize(16777215, 100))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bottom_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setContentsMargins(50, 0, 50, 10)
        self.add_btn = QPushButton(self.bottom_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Satoshi Medium"])
        font1.setPointSize(10)
        self.add_btn.setFont(font1)
        self.add_btn.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #191919;\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_2.addWidget(self.add_btn, 0, 1, 1, 1)

        self.cancel_btn = QPushButton(self.bottom_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMaximumSize(QSize(16777215, 45))
        self.cancel_btn.setFont(font1)
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


        self.gridLayout.addWidget(self.bottom_frame, 3, 0, 1, 1)

        self.content_frame = QFrame(self.widget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.content_frame)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        font2 = QFont()
        font2.setFamilies([u"Satoshi Black"])
        self.frame_5.setFont(font2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        font3 = QFont()
        font3.setFamilies([u"Satoshi Medium"])
        font3.setPointSize(9)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: black;")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.product_name_lineEdit = QLineEdit(self.frame_5)
        self.product_name_lineEdit.setObjectName(u"product_name_lineEdit")
        self.product_name_lineEdit.setMinimumSize(QSize(299, 45))
        self.product_name_lineEdit.setMaximumSize(QSize(299, 45))
        font4 = QFont()
        font4.setFamilies([u"Satoshi"])
        self.product_name_lineEdit.setFont(font4)
        self.product_name_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.product_name_lineEdit, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))
        font5 = QFont()
        font5.setFamilies([u"Satoshi Medium"])
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: black;")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.category_lineEdit = QLineEdit(self.frame_3)
        self.category_lineEdit.setObjectName(u"category_lineEdit")
        self.category_lineEdit.setMinimumSize(QSize(299, 45))
        self.category_lineEdit.setMaximumSize(QSize(299, 45))
        self.category_lineEdit.setFont(font4)
        self.category_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_3.addWidget(self.category_lineEdit, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 15))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: black;")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.price_lineEdit = QLineEdit(self.frame_4)
        self.price_lineEdit.setObjectName(u"price_lineEdit")
        self.price_lineEdit.setMinimumSize(QSize(299, 45))
        self.price_lineEdit.setMaximumSize(QSize(299, 45))
        self.price_lineEdit.setFont(font4)
        self.price_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_6.addWidget(self.price_lineEdit, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 15))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: black;")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.quantity_lineEdit = QLineEdit(self.frame_2)
        self.quantity_lineEdit.setObjectName(u"quantity_lineEdit")
        self.quantity_lineEdit.setMinimumSize(QSize(299, 45))
        self.quantity_lineEdit.setMaximumSize(QSize(299, 45))
        self.quantity_lineEdit.setFont(font4)
        self.quantity_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_7.addWidget(self.quantity_lineEdit, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_2, 3, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.content_frame, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Add_Dialog)
        self.cancel_btn.clicked.connect(Add_Dialog.close)

        QMetaObject.connectSlotsByName(Add_Dialog)
    # setupUi

    def retranslateUi(self, Add_Dialog):
        Add_Dialog.setWindowTitle(QCoreApplication.translate("Add_Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Add_Dialog", u"New Item", None))
        self.add_btn.setText(QCoreApplication.translate("Add_Dialog", u"ADD", None))
        self.cancel_btn.setText(QCoreApplication.translate("Add_Dialog", u"CANCEL", None))
        self.label_3.setText(QCoreApplication.translate("Add_Dialog", u"Product Name", None))
        self.product_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Add_Dialog", u"Product Name", None))
        self.label_4.setText(QCoreApplication.translate("Add_Dialog", u"Category", None))
        self.category_lineEdit.setText("")
        self.category_lineEdit.setPlaceholderText(QCoreApplication.translate("Add_Dialog", u"Category", None))
        self.label_5.setText(QCoreApplication.translate("Add_Dialog", u"Price", None))
        self.price_lineEdit.setText("")
        self.price_lineEdit.setPlaceholderText(QCoreApplication.translate("Add_Dialog", u"Price", None))
        self.label_6.setText(QCoreApplication.translate("Add_Dialog", u"Quantity", None))
        self.quantity_lineEdit.setText("")
        self.quantity_lineEdit.setPlaceholderText(QCoreApplication.translate("Add_Dialog", u"Quantity", None))
    # retranslateUi

