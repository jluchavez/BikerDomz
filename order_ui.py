# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Order_Dialog(object):
    def setupUi(self, Order_Dialog):
        if not Order_Dialog.objectName():
            Order_Dialog.setObjectName(u"Order_Dialog")
        Order_Dialog.resize(400, 550)
        self.verticalLayout = QVBoxLayout(Order_Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Order_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.widget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 100))
        self.top_frame.setMaximumSize(QSize(16777215, 16777215))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.top_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 25, 0, 0)
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

        self.middle_frame = QFrame(self.widget)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.middle_frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.conten_frame = QFrame(self.middle_frame)
        self.conten_frame.setObjectName(u"conten_frame")
        self.conten_frame.setMinimumSize(QSize(300, 0))
        self.conten_frame.setMaximumSize(QSize(300, 16777215))
        self.conten_frame.setFrameShape(QFrame.StyledPanel)
        self.conten_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.conten_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.conten_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 70))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.category_lineEdit = QLineEdit(self.frame_8)
        self.category_lineEdit.setObjectName(u"category_lineEdit")
        self.category_lineEdit.setMinimumSize(QSize(0, 45))
        self.category_lineEdit.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Satoshi"])
        font1.setPointSize(9)
        self.category_lineEdit.setFont(font1)
        self.category_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")
        self.category_lineEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.category_lineEdit, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamilies([u"Satoshi Medium"])
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: black;")

        self.gridLayout_9.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.conten_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_9)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.price_lineEdit = QLineEdit(self.frame_9)
        self.price_lineEdit.setObjectName(u"price_lineEdit")
        self.price_lineEdit.setMinimumSize(QSize(0, 45))
        self.price_lineEdit.setMaximumSize(QSize(16777215, 45))
        self.price_lineEdit.setFont(font1)
        self.price_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")
        self.price_lineEdit.setReadOnly(True)

        self.gridLayout_10.addWidget(self.price_lineEdit, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 15))
        font3 = QFont()
        font3.setFamilies([u"Satoshi Medium"])
        font3.setPointSize(9)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: black;")

        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_9, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.conten_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_7)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: black;")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.product_dropdown = QComboBox(self.frame_7)
        self.product_dropdown.setObjectName(u"product_dropdown")
        self.product_dropdown.setMinimumSize(QSize(0, 45))
        self.product_dropdown.setFont(font1)
        self.product_dropdown.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_8.addWidget(self.product_dropdown, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.conten_frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 45))
        self.frame_6.setMaximumSize(QSize(16777215, 70))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.discount_lineEdit = QLineEdit(self.frame_6)
        self.discount_lineEdit.setObjectName(u"discount_lineEdit")
        sizePolicy.setHeightForWidth(self.discount_lineEdit.sizePolicy().hasHeightForWidth())
        self.discount_lineEdit.setSizePolicy(sizePolicy)
        self.discount_lineEdit.setMinimumSize(QSize(100, 45))
        self.discount_lineEdit.setMaximumSize(QSize(16777215, 45))
        self.discount_lineEdit.setFont(font1)
        self.discount_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_7.addWidget(self.discount_lineEdit, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 15))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: black;")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.quantity_SpinBox = QSpinBox(self.frame_6)
        self.quantity_SpinBox.setObjectName(u"quantity_SpinBox")
        sizePolicy.setHeightForWidth(self.quantity_SpinBox.sizePolicy().hasHeightForWidth())
        self.quantity_SpinBox.setSizePolicy(sizePolicy)
        self.quantity_SpinBox.setMinimumSize(QSize(135, 45))
        self.quantity_SpinBox.setMaximumSize(QSize(16777215, 45))
        self.quantity_SpinBox.setFont(font1)
        self.quantity_SpinBox.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")

        self.gridLayout_7.addWidget(self.quantity_SpinBox, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 15))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: black;")

        self.gridLayout_7.addWidget(self.label_7, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.conten_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.total_lineEdit = QLineEdit(self.frame_5)
        self.total_lineEdit.setObjectName(u"total_lineEdit")
        self.total_lineEdit.setMaximumSize(QSize(16777215, 45))
        self.total_lineEdit.setFont(font1)
        self.total_lineEdit.setStyleSheet(u"border: none;\n"
"padding-right: 5px;\n"
"background-color: transparent;\n"
"color: rgb(124, 124, 135);")
        self.total_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.total_lineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.total_lineEdit, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 5, 0, 1, 1)


        self.gridLayout_3.addWidget(self.conten_frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.middle_frame, 1, 0, 1, 1)

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
        self.cancel_btn = QPushButton(self.bottom_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy1)
        self.cancel_btn.setMinimumSize(QSize(0, 45))
        self.cancel_btn.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setFamilies([u"Satoshi Medium"])
        font4.setPointSize(10)
        self.cancel_btn.setFont(font4)
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

        self.add_btn = QPushButton(self.bottom_frame)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy1.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy1)
        self.add_btn.setMinimumSize(QSize(0, 45))
        self.add_btn.setMaximumSize(QSize(16777215, 45))
        self.add_btn.setFont(font4)
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


        self.gridLayout.addWidget(self.bottom_frame, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Order_Dialog)
        self.cancel_btn.clicked.connect(Order_Dialog.close)

        QMetaObject.connectSlotsByName(Order_Dialog)
    # setupUi

    def retranslateUi(self, Order_Dialog):
        Order_Dialog.setWindowTitle(QCoreApplication.translate("Order_Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Order_Dialog", u"New Order", None))
        self.category_lineEdit.setText("")
        self.category_lineEdit.setPlaceholderText(QCoreApplication.translate("Order_Dialog", u"Category", None))
        self.label_4.setText(QCoreApplication.translate("Order_Dialog", u"Category", None))
        self.price_lineEdit.setText("")
        self.price_lineEdit.setPlaceholderText(QCoreApplication.translate("Order_Dialog", u"Price", None))
        self.label_5.setText(QCoreApplication.translate("Order_Dialog", u"Price", None))
        self.label_3.setText(QCoreApplication.translate("Order_Dialog", u"Product Name", None))
        self.product_dropdown.setPlaceholderText(QCoreApplication.translate("Order_Dialog", u"Select Product", None))
        self.discount_lineEdit.setPlaceholderText(QCoreApplication.translate("Order_Dialog", u"Discount", None))
        self.label_6.setText(QCoreApplication.translate("Order_Dialog", u"Quantity", None))
        self.label_7.setText(QCoreApplication.translate("Order_Dialog", u"Discount", None))
        self.label_2.setText(QCoreApplication.translate("Order_Dialog", u"Total:", None))
        self.cancel_btn.setText(QCoreApplication.translate("Order_Dialog", u"CANCEL", None))
        self.add_btn.setText(QCoreApplication.translate("Order_Dialog", u"ADD", None))
    # retranslateUi

