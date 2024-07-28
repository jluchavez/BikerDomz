# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

class Ui_SignIn_Dialog(object):
    def setupUi(self, SignIn_Dialog):
        if not SignIn_Dialog.objectName():
            SignIn_Dialog.setObjectName(u"SignIn_Dialog")
        SignIn_Dialog.resize(480, 620)
        self.gridLayout = QGridLayout(SignIn_Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(SignIn_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 70, 131, 61))
        font = QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.signin_btn = QPushButton(self.widget)
        self.signin_btn.setObjectName(u"signin_btn")
        self.signin_btn.setGeometry(QRect(110, 490, 250, 45))
        self.signin_btn.setStyleSheet(u"background-color: black;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: white;")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 140, 252, 300))
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setMinimumSize(QSize(250, 45))
        self.username_lineEdit.setMaximumSize(QSize(250, 45))
        self.username_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")

        self.verticalLayout.addWidget(self.username_lineEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(250, 45))
        self.password_lineEdit.setMaximumSize(QSize(250, 45))
        self.password_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")

        self.verticalLayout.addWidget(self.password_lineEdit)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.confirmpass_lineEdit = QLineEdit(self.frame)
        self.confirmpass_lineEdit.setObjectName(u"confirmpass_lineEdit")
        self.confirmpass_lineEdit.setMinimumSize(QSize(250, 45))
        self.confirmpass_lineEdit.setMaximumSize(QSize(250, 45))
        self.confirmpass_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")

        self.verticalLayout.addWidget(self.confirmpass_lineEdit)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(SignIn_Dialog)

        QMetaObject.connectSlotsByName(SignIn_Dialog)
    # setupUi

    def retranslateUi(self, SignIn_Dialog):
        SignIn_Dialog.setWindowTitle(QCoreApplication.translate("SignIn_Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("SignIn_Dialog", u"SIGN IN", None))
        self.signin_btn.setText(QCoreApplication.translate("SignIn_Dialog", u"SIGN IN", None))
        self.label.setText(QCoreApplication.translate("SignIn_Dialog", u"Username", None))
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("SignIn_Dialog", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("SignIn_Dialog", u"Password", None))
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("SignIn_Dialog", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("SignIn_Dialog", u"Confirm Password", None))
        self.confirmpass_lineEdit.setPlaceholderText(QCoreApplication.translate("SignIn_Dialog", u"Confirm Password", None))
    # retranslateUi

