# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginBApXLG.ui'
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
    QWidget)
import icons_rc

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        if not Login_Dialog.objectName():
            Login_Dialog.setObjectName(u"Login_Dialog")
        Login_Dialog.resize(400, 500)
        Login_Dialog.setMinimumSize(QSize(0, 500))
        Login_Dialog.setMaximumSize(QSize(500, 16777215))
        self.gridLayout = QGridLayout(Login_Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Login_Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.middle_frame = QFrame(self.widget)
        self.middle_frame.setObjectName(u"middle_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.middle_frame.sizePolicy().hasHeightForWidth())
        self.middle_frame.setSizePolicy(sizePolicy1)
        self.middle_frame.setMinimumSize(QSize(0, 0))
        self.middle_frame.setStyleSheet(u"text-align: center;")
        self.gridLayout_7 = QGridLayout(self.middle_frame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 30)
        self.frame_4 = QFrame(self.middle_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setMaximumSize(QSize(300, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(250, 15))
        self.label.setMaximumSize(QSize(250, 15))
        font = QFont()
        font.setFamilies([u"Satoshi Medium"])
        font.setPointSize(9)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setMinimumSize(QSize(250, 45))
        self.username_lineEdit.setMaximumSize(QSize(250, 45))
        font1 = QFont()
        font1.setFamilies([u"Satoshi"])
        font1.setPointSize(9)
        self.username_lineEdit.setFont(font1)
        self.username_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")

        self.gridLayout_2.addWidget(self.username_lineEdit, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(250, 15))
        self.label_2.setMaximumSize(QSize(250, 15))
        self.label_2.setFont(font)

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)

        self.password_lineEdit = QLineEdit(self.frame_2)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(250, 45))
        self.password_lineEdit.setMaximumSize(QSize(250, 45))
        self.password_lineEdit.setFont(font1)
        self.password_lineEdit.setStyleSheet(u"border: 1px solid rgb(244, 242, 240);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"background-color: transparent;")

        self.gridLayout_9.addWidget(self.password_lineEdit, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.middle_frame, 1, 0, 1, 1)

        self.bottom_frame = QFrame(self.widget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 100))
        self.bottom_frame.setMaximumSize(QSize(16777215, 100))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.bottom_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.login_btn = QPushButton(self.bottom_frame)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QSize(0, 45))
        self.login_btn.setMaximumSize(QSize(250, 45))
        font2 = QFont()
        font2.setFamilies([u"Satoshi Medium"])
        font2.setPointSize(10)
        self.login_btn.setFont(font2)
        self.login_btn.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color:black;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #191919;\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.login_btn, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.bottom_frame, 2, 0, 1, 1)

        self.top_frame = QFrame(self.widget)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setMaximumSize(QSize(16777215, 125))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.top_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(self.top_frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(300, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMaximumSize(QSize(300, 100))
        font3 = QFont()
        font3.setFamilies([u"Satoshi Black"])
        font3.setPointSize(24)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"padding-left: 15px;\n"
"padding-top: 35px;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setMaximumSize(QSize(16777215, 25))
        font4 = QFont()
        font4.setFamilies([u"Satoshi"])
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"padding-left: 22px;\n"
"color:rgb(104, 104, 104);")

        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.top_frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Login_Dialog)

        QMetaObject.connectSlotsByName(Login_Dialog)
    # setupUi

    def retranslateUi(self, Login_Dialog):
        Login_Dialog.setWindowTitle(QCoreApplication.translate("Login_Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Login_Dialog", u"Username", None))
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("Login_Dialog", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Login_Dialog", u"Password", None))
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("Login_Dialog", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("Login_Dialog", u"LOGIN", None))
        self.label_3.setText(QCoreApplication.translate("Login_Dialog", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("Login_Dialog", u"Please sign in to continue.", None))
    # retranslateUi

