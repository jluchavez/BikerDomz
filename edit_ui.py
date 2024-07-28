# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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

class Ui_Edit_Dialog(object):
    def setupUi(self, Edit_Dialog):
        if not Edit_Dialog.objectName():
            Edit_Dialog.setObjectName(u"Edit_Dialog")
        Edit_Dialog.resize(400, 550)
        self.verticalLayout = QVBoxLayout(Edit_Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Edit_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 25, 0, 0)
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

        self.middle_frame = QFrame(self.widget)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.middle_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.middle_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setFamilies([u"Satoshi Medium"])
        font1.setBold(False)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.category_lineEdit = QLineEdit(self.frame_3)
        self.category_lineEdit.setObjectName(u"category_lineEdit")
        self.category_lineEdit.setEnabled(True)
        self.category_lineEdit.setMinimumSize(QSize(298, 45))
        self.category_lineEdit.setMaximumSize(QSize(298, 45))
        font2 = QFont()
        font2.setFamilies([u"Satoshi"])
        self.category_lineEdit.setFont(font2)
        self.category_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.category_lineEdit, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 15))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 15))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_6, 7, 0, 1, 1)

        self.price_lineEdit = QLineEdit(self.frame_3)
        self.price_lineEdit.setObjectName(u"price_lineEdit")
        self.price_lineEdit.setMinimumSize(QSize(298, 45))
        self.price_lineEdit.setMaximumSize(QSize(298, 45))
        self.price_lineEdit.setFont(font2)
        self.price_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.price_lineEdit, 8, 0, 1, 1)

        self.product_name_lineEdit = QLineEdit(self.frame_3)
        self.product_name_lineEdit.setObjectName(u"product_name_lineEdit")
        self.product_name_lineEdit.setMinimumSize(QSize(298, 0))
        self.product_name_lineEdit.setMaximumSize(QSize(298, 45))
        self.product_name_lineEdit.setFont(font2)
        self.product_name_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.product_name_lineEdit, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.quantity_lineEdit = QLineEdit(self.frame_3)
        self.quantity_lineEdit.setObjectName(u"quantity_lineEdit")
        self.quantity_lineEdit.setEnabled(True)
        self.quantity_lineEdit.setMinimumSize(QSize(298, 45))
        self.quantity_lineEdit.setMaximumSize(QSize(298, 16777215))
        self.quantity_lineEdit.setFont(font2)
        self.quantity_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_4.addWidget(self.quantity_lineEdit, 6, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.middle_frame, 1, 0, 1, 1)

        self.bottom_frame = QFrame(self.widget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 100))
        self.bottom_frame.setMaximumSize(QSize(16777215, 100))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bottom_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(50, 0, 50, 10)
        self.cancel_btn = QPushButton(self.bottom_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy2)
        self.cancel_btn.setMinimumSize(QSize(0, 45))
        self.cancel_btn.setMaximumSize(QSize(143, 45))
        font3 = QFont()
        font3.setFamilies([u"Satoshi Medium"])
        font3.setPointSize(10)
        self.cancel_btn.setFont(font3)
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
        sizePolicy2.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy2)
        self.save_btn.setMinimumSize(QSize(0, 45))
        self.save_btn.setMaximumSize(QSize(143, 45))
        self.save_btn.setFont(font3)
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


        self.retranslateUi(Edit_Dialog)
        self.cancel_btn.clicked.connect(Edit_Dialog.close)

        QMetaObject.connectSlotsByName(Edit_Dialog)
    # setupUi

    def retranslateUi(self, Edit_Dialog):
        Edit_Dialog.setWindowTitle(QCoreApplication.translate("Edit_Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Edit_Dialog", u"Edit Item", None))
        self.label_4.setText(QCoreApplication.translate("Edit_Dialog", u"Category", None))
        self.category_lineEdit.setText("")
        self.category_lineEdit.setPlaceholderText(QCoreApplication.translate("Edit_Dialog", u"Category", None))
        self.label_5.setText(QCoreApplication.translate("Edit_Dialog", u"Quantity", None))
        self.label_6.setText(QCoreApplication.translate("Edit_Dialog", u"Price", None))
        self.price_lineEdit.setText("")
        self.price_lineEdit.setPlaceholderText(QCoreApplication.translate("Edit_Dialog", u"Price", None))
        self.product_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Edit_Dialog", u"Product Name", None))
        self.label_3.setText(QCoreApplication.translate("Edit_Dialog", u"Product Name", None))
        self.quantity_lineEdit.setPlaceholderText(QCoreApplication.translate("Edit_Dialog", u"Quantity", None))
        self.cancel_btn.setText(QCoreApplication.translate("Edit_Dialog", u"CANCEL", None))
        self.save_btn.setText(QCoreApplication.translate("Edit_Dialog", u"SAVE", None))
    # retranslateUi

