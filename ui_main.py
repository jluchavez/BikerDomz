# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVBhMaK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1366, 768))
        font = QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(244, 242, 240);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        sizePolicy.setHeightForWidth(self.Content.sizePolicy().hasHeightForWidth())
        self.Content.setSizePolicy(sizePolicy)
        self.Content.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.Content)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_pages = QWidget(self.Content)
        self.widget_pages.setObjectName(u"widget_pages")
        sizePolicy.setHeightForWidth(self.widget_pages.sizePolicy().hasHeightForWidth())
        self.widget_pages.setSizePolicy(sizePolicy)
        self.widget_pages.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_35 = QGridLayout(self.widget_pages)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setLineWidth(0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.page_1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.content_1 = QWidget(self.page_1)
        self.content_1.setObjectName(u"content_1")
        self.content_1.setMinimumSize(QSize(40, 0))
        self.content_1.setStyleSheet(u"")
        self.gridLayout_34 = QGridLayout(self.content_1)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.top_content_frame = QFrame(self.content_1)
        self.top_content_frame.setObjectName(u"top_content_frame")
        self.top_content_frame.setMinimumSize(QSize(0, 70))
        self.top_content_frame.setMaximumSize(QSize(16777215, 70))
        self.top_content_frame.setStyleSheet(u"QFrame #top_content_frame {\n"
"border-bottom: 1px solid #ebebea;\n"
"border-top: 1px solid #ebebea;\n"
"}")
        self.top_content_frame.setFrameShape(QFrame.StyledPanel)
        self.top_content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.top_content_frame)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_10 = QLabel(self.top_content_frame)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamilies([u"Satoshi Medium"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"border: none;")

        self.gridLayout_41.addWidget(self.label_10, 0, 1, 1, 1)

        self.inventory_icon_6 = QPushButton(self.top_content_frame)
        self.inventory_icon_6.setObjectName(u"inventory_icon_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inventory_icon_6.sizePolicy().hasHeightForWidth())
        self.inventory_icon_6.setSizePolicy(sizePolicy1)
        self.inventory_icon_6.setMinimumSize(QSize(40, 40))
        self.inventory_icon_6.setMaximumSize(QSize(40, 40))
        self.inventory_icon_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(55, 50, 52);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/columns-gap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_icon_6.setIcon(icon)
        self.inventory_icon_6.setIconSize(QSize(20, 20))

        self.gridLayout_41.addWidget(self.inventory_icon_6, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.year_dropdown = QComboBox(self.top_content_frame)
        self.year_dropdown.setObjectName(u"year_dropdown")
        self.year_dropdown.setMinimumSize(QSize(100, 35))
        self.year_dropdown.setMaximumSize(QSize(100, 35))
        font2 = QFont()
        font2.setFamilies([u"Satoshi Medium"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.year_dropdown.setFont(font2)
        self.year_dropdown.setStyleSheet(u"QComboBox { \n"
"background-color:white;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"text-align:center ;\n"
"color: black;\n"
"border: 1px solid #ebebea;;\n"
"}\n"
"QComboBox::drop-down {\n"
"border: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}")
        self.year_dropdown.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.gridLayout_41.addWidget(self.year_dropdown, 0, 4, 1, 1)

        self.month_dropdown = QComboBox(self.top_content_frame)
        self.month_dropdown.setObjectName(u"month_dropdown")
        self.month_dropdown.setMinimumSize(QSize(100, 35))
        self.month_dropdown.setMaximumSize(QSize(100, 35))
        self.month_dropdown.setFont(font2)
        self.month_dropdown.setStyleSheet(u"QComboBox { \n"
"background-color: white;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"color:black;\n"
"border: 1px solid #ebebea;;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"border: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}")

        self.gridLayout_41.addWidget(self.month_dropdown, 0, 3, 1, 1)


        self.gridLayout_34.addWidget(self.top_content_frame, 0, 0, 1, 1)

        self.content_frame_1 = QFrame(self.content_1)
        self.content_frame_1.setObjectName(u"content_frame_1")
        self.content_frame_1.setFrameShape(QFrame.StyledPanel)
        self.content_frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.content_frame_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.top_frame_1 = QFrame(self.content_frame_1)
        self.top_frame_1.setObjectName(u"top_frame_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.top_frame_1.sizePolicy().hasHeightForWidth())
        self.top_frame_1.setSizePolicy(sizePolicy2)
        self.top_frame_1.setFrameShape(QFrame.StyledPanel)
        self.top_frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.top_frame_1)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(20)
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.inventory_summary_frame = QFrame(self.top_frame_1)
        self.inventory_summary_frame.setObjectName(u"inventory_summary_frame")
        sizePolicy2.setHeightForWidth(self.inventory_summary_frame.sizePolicy().hasHeightForWidth())
        self.inventory_summary_frame.setSizePolicy(sizePolicy2)
        self.inventory_summary_frame.setMinimumSize(QSize(300, 0))
        self.inventory_summary_frame.setMaximumSize(QSize(300, 16777215))
        self.inventory_summary_frame.setStyleSheet(u"QFrame #inventory_summary_frame { \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #ebebea;\n"
"}")
        self.inventory_summary_frame.setFrameShape(QFrame.StyledPanel)
        self.inventory_summary_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.inventory_summary_frame)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.frame_40 = QFrame(self.inventory_summary_frame)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy3)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_56 = QGridLayout(self.frame_40)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy3.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy3)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_41)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_42)
        self.gridLayout_58.setSpacing(0)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_42)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setFamilies([u"Satoshi"])
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_58.addWidget(self.label_12, 0, 0, 1, 1)

        self.stockreceived_label = QLabel(self.frame_42)
        self.stockreceived_label.setObjectName(u"stockreceived_label")
        font4 = QFont()
        font4.setFamilies([u"Satoshi Black"])
        font4.setPointSize(20)
        self.stockreceived_label.setFont(font4)
        self.stockreceived_label.setStyleSheet(u"color:#172532;")

        self.gridLayout_58.addWidget(self.stockreceived_label, 1, 0, 1, 1)


        self.gridLayout_57.addWidget(self.frame_42, 0, 0, 1, 1)


        self.gridLayout_56.addWidget(self.frame_41, 0, 0, 1, 1)


        self.gridLayout_59.addWidget(self.frame_40, 1, 0, 1, 1)

        self.frame_23 = QFrame(self.inventory_summary_frame)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy3.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy3)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_23)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.frame_31 = QFrame(self.frame_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 50))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.frame_31)
        self.gridLayout_54.setSpacing(0)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_31)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_54.addWidget(self.label_14, 0, 0, 1, 1)

        self.totalstocks_label_2 = QLabel(self.frame_31)
        self.totalstocks_label_2.setObjectName(u"totalstocks_label_2")
        self.totalstocks_label_2.setFont(font4)
        self.totalstocks_label_2.setStyleSheet(u"color:#172532;")

        self.gridLayout_54.addWidget(self.totalstocks_label_2, 1, 0, 1, 1)


        self.gridLayout_53.addWidget(self.frame_31, 0, 0, 1, 1)


        self.gridLayout_59.addWidget(self.frame_23, 1, 1, 1, 1)

        self.frame_32 = QFrame(self.inventory_summary_frame)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy4)
        self.frame_32.setMinimumSize(QSize(0, 25))
        self.frame_32.setMaximumSize(QSize(16777215, 35))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(False)
        self.frame_32.setFont(font5)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.frame_32)
        self.gridLayout_55.setSpacing(0)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(-1, 0, -1, 0)
        self.label_24 = QLabel(self.frame_32)
        self.label_24.setObjectName(u"label_24")
        font6 = QFont()
        font6.setFamilies([u"Satoshi Medium"])
        font6.setPointSize(11)
        font6.setBold(False)
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"color:#172532;")

        self.gridLayout_55.addWidget(self.label_24, 0, 0, 1, 1)


        self.gridLayout_59.addWidget(self.frame_32, 0, 0, 1, 2)


        self.gridLayout_32.addWidget(self.inventory_summary_frame, 0, 2, 1, 1)

        self.inventory_overview_frame = QFrame(self.top_frame_1)
        self.inventory_overview_frame.setObjectName(u"inventory_overview_frame")
        sizePolicy2.setHeightForWidth(self.inventory_overview_frame.sizePolicy().hasHeightForWidth())
        self.inventory_overview_frame.setSizePolicy(sizePolicy2)
        self.inventory_overview_frame.setMinimumSize(QSize(344, 100))
        self.inventory_overview_frame.setMaximumSize(QSize(16777215, 16777215))
        self.inventory_overview_frame.setStyleSheet(u"QFrame #inventory_overview_frame { \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #ebebea;\n"
"}")
        self.inventory_overview_frame.setFrameShape(QFrame.StyledPanel)
        self.inventory_overview_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.inventory_overview_frame)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.frame_22 = QFrame(self.inventory_overview_frame)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy4.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy4)
        self.frame_22.setMinimumSize(QSize(0, 25))
        self.frame_22.setMaximumSize(QSize(16777215, 35))
        self.frame_22.setFont(font5)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_22)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"color:#172532;")

        self.gridLayout_30.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_22, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.inventory_overview_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_17)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMinimumSize(QSize(158, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_18)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.pushButton_7 = QPushButton(self.frame_18)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setMinimumSize(QSize(50, 50))
        self.pushButton_7.setMaximumSize(QSize(50, 16777215))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/soldstocktoday.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(35, 35))

        self.gridLayout_26.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_19)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_27.addWidget(self.label_11, 0, 0, 1, 1)

        self.soldstockstoday_label = QLabel(self.frame_19)
        self.soldstockstoday_label.setObjectName(u"soldstockstoday_label")
        self.soldstockstoday_label.setFont(font4)
        self.soldstockstoday_label.setStyleSheet(u"color:#172532;")

        self.gridLayout_27.addWidget(self.soldstockstoday_label, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_19, 0, 1, 1, 1)


        self.gridLayout_25.addWidget(self.frame_18, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.inventory_overview_frame)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy3.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy3)
        self.frame_20.setMinimumSize(QSize(158, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.pushButton_8 = QPushButton(self.frame_20)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(50, 50))
        self.pushButton_8.setMaximumSize(QSize(50, 16777215))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/graph.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.gridLayout_28.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 50))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_21)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_29.addWidget(self.label_13, 0, 0, 1, 1)

        self.totalsoldstocks_label = QLabel(self.frame_21)
        self.totalsoldstocks_label.setObjectName(u"totalsoldstocks_label")
        self.totalsoldstocks_label.setFont(font4)
        self.totalsoldstocks_label.setStyleSheet(u"color:#172532;")

        self.gridLayout_29.addWidget(self.totalsoldstocks_label, 1, 0, 1, 1)


        self.gridLayout_28.addWidget(self.frame_21, 0, 1, 1, 1)


        self.gridLayout_31.addWidget(self.frame_20, 1, 1, 1, 1)


        self.gridLayout_32.addWidget(self.inventory_overview_frame, 0, 1, 1, 1)

        self.sales_overview_frame = QFrame(self.top_frame_1)
        self.sales_overview_frame.setObjectName(u"sales_overview_frame")
        sizePolicy2.setHeightForWidth(self.sales_overview_frame.sizePolicy().hasHeightForWidth())
        self.sales_overview_frame.setSizePolicy(sizePolicy2)
        self.sales_overview_frame.setMinimumSize(QSize(344, 100))
        self.sales_overview_frame.setMaximumSize(QSize(16777215, 16777215))
        self.sales_overview_frame.setStyleSheet(u"QFrame #sales_overview_frame { \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #ebebea;\n"
"}")
        self.sales_overview_frame.setFrameShape(QFrame.StyledPanel)
        self.sales_overview_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.sales_overview_frame)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_11 = QFrame(self.sales_overview_frame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setMinimumSize(QSize(158, 70))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_11)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_13)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_24.addWidget(self.label_8, 0, 0, 1, 1)

        self.totalsales_label = QLabel(self.frame_13)
        self.totalsales_label.setObjectName(u"totalsales_label")
        self.totalsales_label.setFont(font4)
        self.totalsales_label.setStyleSheet(u"color:#172532;")

        self.gridLayout_24.addWidget(self.totalsales_label, 1, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_13, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(50, 16777215))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/totalsales.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.gridLayout_22.addWidget(self.pushButton_6, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.sales_overview_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setMinimumSize(QSize(0, 25))
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setFont(font5)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_2)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color:#172532;")

        self.gridLayout_19.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.sales_overview_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_9)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setMinimumSize(QSize(158, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_10)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_12)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_23.addWidget(self.label_7, 0, 0, 1, 1)

        self.todaysales_label = QLabel(self.frame_12)
        self.todaysales_label.setObjectName(u"todaysales_label")
        self.todaysales_label.setFont(font4)
        self.todaysales_label.setStyleSheet(u"color:#172532;")

        self.gridLayout_23.addWidget(self.todaysales_label, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_12, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setMaximumSize(QSize(50, 16777215))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/todaysales.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(30, 30))

        self.gridLayout_21.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_10, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_9, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.sales_overview_frame, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.top_frame_1, 0, 0, 1, 1)

        self.bottom_frame_1 = QFrame(self.content_frame_1)
        self.bottom_frame_1.setObjectName(u"bottom_frame_1")
        sizePolicy.setHeightForWidth(self.bottom_frame_1.sizePolicy().hasHeightForWidth())
        self.bottom_frame_1.setSizePolicy(sizePolicy)
        self.bottom_frame_1.setMinimumSize(QSize(0, 0))
        self.bottom_frame_1.setStyleSheet(u"")
        self.bottom_frame_1.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.bottom_frame_1)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setHorizontalSpacing(20)
        self.gridLayout_52.setVerticalSpacing(0)
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.sub_bottom_frame_1 = QFrame(self.bottom_frame_1)
        self.sub_bottom_frame_1.setObjectName(u"sub_bottom_frame_1")
        sizePolicy.setHeightForWidth(self.sub_bottom_frame_1.sizePolicy().hasHeightForWidth())
        self.sub_bottom_frame_1.setSizePolicy(sizePolicy)
        self.sub_bottom_frame_1.setMinimumSize(QSize(300, 0))
        self.sub_bottom_frame_1.setMaximumSize(QSize(300, 16777215))
        self.sub_bottom_frame_1.setFrameShape(QFrame.StyledPanel)
        self.sub_bottom_frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.sub_bottom_frame_1)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setHorizontalSpacing(0)
        self.gridLayout_60.setVerticalSpacing(20)
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.product_details_frame = QFrame(self.sub_bottom_frame_1)
        self.product_details_frame.setObjectName(u"product_details_frame")
        sizePolicy3.setHeightForWidth(self.product_details_frame.sizePolicy().hasHeightForWidth())
        self.product_details_frame.setSizePolicy(sizePolicy3)
        self.product_details_frame.setMinimumSize(QSize(300, 200))
        self.product_details_frame.setStyleSheet(u"QFrame #product_details_frame { \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #ebebea;\n"
"}")
        self.product_details_frame.setFrameShape(QFrame.StyledPanel)
        self.product_details_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.product_details_frame)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setVerticalSpacing(0)
        self.frame_39 = QFrame(self.product_details_frame)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy)
        self.frame_39.setMinimumSize(QSize(0, 35))
        self.frame_39.setMaximumSize(QSize(16777215, 35))
        self.frame_39.setFont(font5)
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_39)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.frame_39)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)

        self.gridLayout_51.addWidget(self.label_21, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_39, 1, 0, 1, 1)

        self.frame_33 = QFrame(self.product_details_frame)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_33)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.no_items_frame = QFrame(self.frame_33)
        self.no_items_frame.setObjectName(u"no_items_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.no_items_frame.sizePolicy().hasHeightForWidth())
        self.no_items_frame.setSizePolicy(sizePolicy5)
        self.no_items_frame.setMinimumSize(QSize(0, 48))
        self.no_items_frame.setMaximumSize(QSize(16777215, 61))
        self.no_items_frame.setFrameShape(QFrame.StyledPanel)
        self.no_items_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.no_items_frame)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(9, 9, 0, -1)
        self.no_items_label_2 = QLabel(self.no_items_frame)
        self.no_items_label_2.setObjectName(u"no_items_label_2")
        self.no_items_label_2.setMinimumSize(QSize(133, 0))
        self.no_items_label_2.setFont(font4)
        self.no_items_label_2.setStyleSheet(u"color:#172532;\n"
"padding-right: 5px;")
        self.no_items_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_46.addWidget(self.no_items_label_2, 1, 1, 1, 1)

        self.label_25 = QLabel(self.no_items_frame)
        self.label_25.setObjectName(u"label_25")
        font7 = QFont()
        font7.setFamilies([u"Satoshi"])
        font7.setPointSize(11)
        self.label_25.setFont(font7)
        self.label_25.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_46.addWidget(self.label_25, 1, 0, 1, 1)


        self.gridLayout_42.addWidget(self.no_items_frame, 0, 0, 1, 1)

        self.item_group_frame = QFrame(self.frame_33)
        self.item_group_frame.setObjectName(u"item_group_frame")
        sizePolicy5.setHeightForWidth(self.item_group_frame.sizePolicy().hasHeightForWidth())
        self.item_group_frame.setSizePolicy(sizePolicy5)
        self.item_group_frame.setMinimumSize(QSize(0, 48))
        self.item_group_frame.setFrameShape(QFrame.StyledPanel)
        self.item_group_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.item_group_frame)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(-1, 9, 0, 9)
        self.no_category_label_2 = QLabel(self.item_group_frame)
        self.no_category_label_2.setObjectName(u"no_category_label_2")
        self.no_category_label_2.setMinimumSize(QSize(133, 0))
        self.no_category_label_2.setFont(font4)
        self.no_category_label_2.setStyleSheet(u"color:#172532;\n"
"padding-right: 5px;")
        self.no_category_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_50.addWidget(self.no_category_label_2, 1, 1, 1, 1)

        self.label_23 = QLabel(self.item_group_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font7)
        self.label_23.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_50.addWidget(self.label_23, 1, 0, 1, 1)


        self.gridLayout_42.addWidget(self.item_group_frame, 1, 0, 1, 1)

        self.low_stock_items_frame = QFrame(self.frame_33)
        self.low_stock_items_frame.setObjectName(u"low_stock_items_frame")
        sizePolicy5.setHeightForWidth(self.low_stock_items_frame.sizePolicy().hasHeightForWidth())
        self.low_stock_items_frame.setSizePolicy(sizePolicy5)
        self.low_stock_items_frame.setMinimumSize(QSize(0, 48))
        self.low_stock_items_frame.setMaximumSize(QSize(16777215, 50))
        self.low_stock_items_frame.setFrameShape(QFrame.StyledPanel)
        self.low_stock_items_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.low_stock_items_frame)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(9, 9, 0, 9)
        self.lowstockitems_label_2 = QLabel(self.low_stock_items_frame)
        self.lowstockitems_label_2.setObjectName(u"lowstockitems_label_2")
        self.lowstockitems_label_2.setMinimumSize(QSize(133, 0))
        self.lowstockitems_label_2.setFont(font4)
        self.lowstockitems_label_2.setStyleSheet(u"color:#172532;\n"
"padding-right: 5px;")
        self.lowstockitems_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_49.addWidget(self.lowstockitems_label_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.low_stock_items_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font7)
        self.label_19.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_49.addWidget(self.label_19, 1, 0, 1, 1)


        self.gridLayout_42.addWidget(self.low_stock_items_frame, 2, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_33, 2, 0, 1, 1)


        self.gridLayout_60.addWidget(self.product_details_frame, 0, 0, 1, 1)

        self.low_stock_frame = QFrame(self.sub_bottom_frame_1)
        self.low_stock_frame.setObjectName(u"low_stock_frame")
        sizePolicy3.setHeightForWidth(self.low_stock_frame.sizePolicy().hasHeightForWidth())
        self.low_stock_frame.setSizePolicy(sizePolicy3)
        self.low_stock_frame.setMinimumSize(QSize(300, 0))
        self.low_stock_frame.setStyleSheet(u"QFrame #low_stock_frame { \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #ebebea;\n"
"}")
        self.low_stock_frame.setFrameShape(QFrame.StyledPanel)
        self.low_stock_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.low_stock_frame)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.frame_43 = QFrame(self.low_stock_frame)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setMinimumSize(QSize(0, 35))
        self.frame_43.setMaximumSize(QSize(16777215, 35))
        self.frame_43.setFont(font5)
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_61 = QGridLayout(self.frame_43)
        self.gridLayout_61.setSpacing(0)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(-1, 0, -1, 0)
        self.label_26 = QLabel(self.frame_43)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"color:#172532;")

        self.gridLayout_61.addWidget(self.label_26, 0, 0, 1, 1)


        self.gridLayout_47.addWidget(self.frame_43, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.low_stock_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_3)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_3)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setMinimumSize(QSize(0, 38))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_64 = QGridLayout(self.frame_46)
        self.gridLayout_64.setSpacing(0)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(-1, 9, 0, 9)
        self.item1_stock = QLabel(self.frame_46)
        self.item1_stock.setObjectName(u"item1_stock")
        self.item1_stock.setFont(font4)
        self.item1_stock.setStyleSheet(u"padding-right:5px;")
        self.item1_stock.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_64.addWidget(self.item1_stock, 1, 1, 1, 1)

        self.itemname_1 = QLabel(self.frame_46)
        self.itemname_1.setObjectName(u"itemname_1")
        self.itemname_1.setFont(font7)
        self.itemname_1.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_64.addWidget(self.itemname_1, 1, 0, 1, 1)


        self.gridLayout_45.addWidget(self.frame_46, 0, 0, 1, 1)

        self.frame_44 = QFrame(self.frame_3)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setMinimumSize(QSize(0, 45))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_44)
        self.gridLayout_62.setSpacing(0)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(-1, 9, 0, 9)
        self.item2_stock = QLabel(self.frame_44)
        self.item2_stock.setObjectName(u"item2_stock")
        self.item2_stock.setFont(font4)
        self.item2_stock.setStyleSheet(u"padding-right:5px;")
        self.item2_stock.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_62.addWidget(self.item2_stock, 1, 1, 1, 1)

        self.itemname_2 = QLabel(self.frame_44)
        self.itemname_2.setObjectName(u"itemname_2")
        self.itemname_2.setFont(font7)
        self.itemname_2.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_62.addWidget(self.itemname_2, 1, 0, 1, 1)


        self.gridLayout_45.addWidget(self.frame_44, 1, 0, 1, 1)

        self.frame_45 = QFrame(self.frame_3)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy)
        self.frame_45.setMinimumSize(QSize(0, 45))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_45)
        self.gridLayout_63.setSpacing(0)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(-1, 9, 0, 9)
        self.item3_stock = QLabel(self.frame_45)
        self.item3_stock.setObjectName(u"item3_stock")
        self.item3_stock.setFont(font4)
        self.item3_stock.setStyleSheet(u"padding-right:5px;")
        self.item3_stock.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_63.addWidget(self.item3_stock, 1, 1, 1, 1)

        self.itemname_3 = QLabel(self.frame_45)
        self.itemname_3.setObjectName(u"itemname_3")
        self.itemname_3.setFont(font7)
        self.itemname_3.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_63.addWidget(self.itemname_3, 1, 0, 1, 1)


        self.gridLayout_45.addWidget(self.frame_45, 2, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_3)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QSize(0, 45))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_65 = QGridLayout(self.frame_34)
        self.gridLayout_65.setSpacing(0)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(-1, -1, 0, 9)
        self.itemname_4 = QLabel(self.frame_34)
        self.itemname_4.setObjectName(u"itemname_4")
        self.itemname_4.setFont(font7)
        self.itemname_4.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_65.addWidget(self.itemname_4, 0, 0, 1, 1)

        self.item4_stock = QLabel(self.frame_34)
        self.item4_stock.setObjectName(u"item4_stock")
        self.item4_stock.setFont(font4)
        self.item4_stock.setStyleSheet(u"padding-right:5px;")
        self.item4_stock.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_65.addWidget(self.item4_stock, 0, 1, 1, 1)


        self.gridLayout_45.addWidget(self.frame_34, 3, 0, 1, 1)

        self.frame_35 = QFrame(self.frame_3)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QSize(0, 45))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_66 = QGridLayout(self.frame_35)
        self.gridLayout_66.setSpacing(0)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(-1, 9, 0, 9)
        self.itemname_5 = QLabel(self.frame_35)
        self.itemname_5.setObjectName(u"itemname_5")
        self.itemname_5.setFont(font7)
        self.itemname_5.setStyleSheet(u"color: rgb(124, 124, 135);")

        self.gridLayout_66.addWidget(self.itemname_5, 0, 0, 1, 1)

        self.item5_stock = QLabel(self.frame_35)
        self.item5_stock.setObjectName(u"item5_stock")
        self.item5_stock.setFont(font4)
        self.item5_stock.setStyleSheet(u"padding-right:5px;")
        self.item5_stock.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_66.addWidget(self.item5_stock, 0, 1, 1, 1)


        self.gridLayout_45.addWidget(self.frame_35, 4, 0, 1, 1)


        self.gridLayout_47.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout_60.addWidget(self.low_stock_frame, 1, 0, 1, 1)


        self.gridLayout_52.addWidget(self.sub_bottom_frame_1, 0, 1, 1, 1)

        self.graph_frame = QFrame(self.bottom_frame_1)
        self.graph_frame.setObjectName(u"graph_frame")
        sizePolicy.setHeightForWidth(self.graph_frame.sizePolicy().hasHeightForWidth())
        self.graph_frame.setSizePolicy(sizePolicy)
        self.graph_frame.setMinimumSize(QSize(0, 0))
        self.graph_frame.setStyleSheet(u"QFrame #graph_frame { \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #ebebea;\n"
"}")
        self.graph_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_67 = QGridLayout(self.graph_frame)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(9, -1, -1, -1)
        self.frame_48 = QFrame(self.graph_frame)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 50))
        self.frame_48.setMaximumSize(QSize(16777215, 50))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_76 = QGridLayout(self.frame_48)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.frame_16 = QFrame(self.frame_48)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 35))
        self.frame_16.setMaximumSize(QSize(16777215, 35))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_68 = QGridLayout(self.frame_16)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setHorizontalSpacing(10)
        self.gridLayout_68.setVerticalSpacing(0)
        self.gridLayout_68.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_76.addWidget(self.frame_16, 0, 4, 1, 1)

        self.label_9 = QLabel(self.frame_48)
        self.label_9.setObjectName(u"label_9")
        font8 = QFont()
        font8.setFamilies([u"Satoshi Medium"])
        font8.setPointSize(11)
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"color:#172532;")

        self.gridLayout_76.addWidget(self.label_9, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_76.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)


        self.gridLayout_67.addWidget(self.frame_48, 0, 0, 1, 1)

        self.graph_frame_2 = QFrame(self.graph_frame)
        self.graph_frame_2.setObjectName(u"graph_frame_2")
        self.graph_frame_2.setStyleSheet(u"border: 1px solid white;")
        self.graph_frame_2.setFrameShape(QFrame.StyledPanel)
        self.graph_frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_67.addWidget(self.graph_frame_2, 1, 0, 1, 1)


        self.gridLayout_52.addWidget(self.graph_frame, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.bottom_frame_1, 1, 0, 1, 1)


        self.gridLayout_34.addWidget(self.content_frame_1, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.content_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        font9 = QFont()
        font9.setFamilies([u"Satoshi"])
        font9.setPointSize(10)
        self.page_4.setFont(font9)
        self.horizontalLayout_6 = QHBoxLayout(self.page_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content_4 = QWidget(self.page_4)
        self.content_4.setObjectName(u"content_4")
        sizePolicy.setHeightForWidth(self.content_4.sizePolicy().hasHeightForWidth())
        self.content_4.setSizePolicy(sizePolicy)
        self.content_4.setMinimumSize(QSize(0, 0))
        self.content_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.content_4)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_content_frame_4 = QFrame(self.content_4)
        self.top_content_frame_4.setObjectName(u"top_content_frame_4")
        self.top_content_frame_4.setMinimumSize(QSize(0, 70))
        self.top_content_frame_4.setStyleSheet(u"QFrame #top_content_frame_4 {\n"
"border-top: 1px solid #ebebea;\n"
"border-bottom: 1px solid #ebebea;\n"
"}")
        self.top_content_frame_4.setFrameShape(QFrame.StyledPanel)
        self.top_content_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.top_content_frame_4)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.inventory_icon = QPushButton(self.top_content_frame_4)
        self.inventory_icon.setObjectName(u"inventory_icon")
        sizePolicy1.setHeightForWidth(self.inventory_icon.sizePolicy().hasHeightForWidth())
        self.inventory_icon.setSizePolicy(sizePolicy1)
        self.inventory_icon.setMinimumSize(QSize(40, 40))
        self.inventory_icon.setMaximumSize(QSize(40, 40))
        self.inventory_icon.setStyleSheet(u"QPushButton {\n"
"	color: rgb(55, 50, 52);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/box-seam.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_icon.setIcon(icon5)
        self.inventory_icon.setIconSize(QSize(20, 20))

        self.gridLayout_40.addWidget(self.inventory_icon, 0, 0, 1, 1)

        self.label = QLabel(self.top_content_frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_40.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.top_content_frame_4, 0, 0, 1, 1)

        self.content_frame_4 = QFrame(self.content_4)
        self.content_frame_4.setObjectName(u"content_frame_4")
        font10 = QFont()
        font10.setFamilies([u"Roman"])
        font10.setBold(True)
        self.content_frame_4.setFont(font10)
        self.content_frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.content_frame_4.setFrameShape(QFrame.StyledPanel)
        self.content_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.content_frame_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.bottom_frame_4 = QFrame(self.content_frame_4)
        self.bottom_frame_4.setObjectName(u"bottom_frame_4")
        self.bottom_frame_4.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.bottom_frame_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 5, 10, 5)
        self.tableWidget = QTableWidget(self.bottom_frame_4)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setFont(font9)
        self.tableWidget.setFocusPolicy(Qt.TabFocus)
        self.tableWidget.setStyleSheet(u"QTableWidget#tableWidget QHeaderView::section {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-bottom: 1px solid #ebebea;\n"
"	font-family: Satoshi;\n"
"	font-size: 13px;\n"
"	height:35px;\n"
"\n"
"}\n"
"QTableWidget#tableWidget {\n"
"	border: 1px solid #ebebea;\n"
"	padding-left: 10px;\n"
"}\n"
"QTableWidget::item:hover  {\n"
"background-color: #f4f4f4;\n"
"}\n"
"QTableWidget::item {\n"
"	font-size: 13px;\n"
"	color:#7C7C87 ;\n"
"	background-color:white ;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(138)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.bottom_frame_4, 1, 0, 1, 1)

        self.middle_frame_4 = QFrame(self.content_frame_4)
        self.middle_frame_4.setObjectName(u"middle_frame_4")
        sizePolicy.setHeightForWidth(self.middle_frame_4.sizePolicy().hasHeightForWidth())
        self.middle_frame_4.setSizePolicy(sizePolicy)
        self.middle_frame_4.setMinimumSize(QSize(0, 50))
        self.middle_frame_4.setMaximumSize(QSize(16777215, 50))
        self.middle_frame_4.setFrameShape(QFrame.StyledPanel)
        self.middle_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.middle_frame_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 0, 10, 0)
        self.frame_7 = QFrame(self.middle_frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_7)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(10)
        self.gridLayout_33.setVerticalSpacing(0)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.edit_btn = QPushButton(self.frame_7)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(100, 35))
        self.edit_btn.setFont(font9)
        self.edit_btn.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"border:1px solid #ebebea;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius: 5px;\n"
"border:1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_btn.setIcon(icon6)
        self.edit_btn.setIconSize(QSize(20, 20))

        self.gridLayout_33.addWidget(self.edit_btn, 0, 4, 1, 1)

        self.openAddDialog_btn = QPushButton(self.frame_7)
        self.openAddDialog_btn.setObjectName(u"openAddDialog_btn")
        self.openAddDialog_btn.setMinimumSize(QSize(100, 35))
        font11 = QFont()
        font11.setFamilies([u"Satoshi Medium"])
        font11.setPointSize(10)
        self.openAddDialog_btn.setFont(font11)
        self.openAddDialog_btn.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color:black;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #191919;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_33.addWidget(self.openAddDialog_btn, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(344, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_33.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.delete_btn = QPushButton(self.frame_7)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(100, 35))
        self.delete_btn.setFont(font9)
        self.delete_btn.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"border:1px solid #ebebea;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius: 5px;\n"
"border:1px solid black;\n"
"color: black;\n"
"}\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/trash3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon7)
        self.delete_btn.setIconSize(QSize(20, 20))

        self.gridLayout_33.addWidget(self.delete_btn, 0, 5, 1, 1)

        self.openAddStock_btn = QPushButton(self.frame_7)
        self.openAddStock_btn.setObjectName(u"openAddStock_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.openAddStock_btn.sizePolicy().hasHeightForWidth())
        self.openAddStock_btn.setSizePolicy(sizePolicy6)
        self.openAddStock_btn.setMinimumSize(QSize(100, 35))
        self.openAddStock_btn.setMaximumSize(QSize(16777215, 40))
        self.openAddStock_btn.setFont(font11)
        self.openAddStock_btn.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color:black;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #191919;\n"
"	border-radius: 5px;\n"
"}")
        self.openAddStock_btn.setIconSize(QSize(25, 25))

        self.gridLayout_33.addWidget(self.openAddStock_btn, 0, 6, 1, 1)


        self.gridLayout_5.addWidget(self.frame_7, 0, 4, 1, 1)


        self.gridLayout_6.addWidget(self.middle_frame_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.content_frame_4, 1, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.content_4)

        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setFont(font9)
        self.page_3.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.content_3 = QWidget(self.page_3)
        self.content_3.setObjectName(u"content_3")
        self.gridLayout_11 = QGridLayout(self.content_3)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.top_content_frame_3 = QFrame(self.content_3)
        self.top_content_frame_3.setObjectName(u"top_content_frame_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.top_content_frame_3.sizePolicy().hasHeightForWidth())
        self.top_content_frame_3.setSizePolicy(sizePolicy7)
        self.top_content_frame_3.setMinimumSize(QSize(0, 70))
        self.top_content_frame_3.setStyleSheet(u"QFrame #top_content_frame_3 {\n"
"border-top: 1px solid #ebebea;\n"
"border-bottom: 1px solid #ebebea;\n"
"}")
        self.top_content_frame_3.setFrameShape(QFrame.StyledPanel)
        self.top_content_frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.top_content_frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.inventory_icon_4 = QPushButton(self.top_content_frame_3)
        self.inventory_icon_4.setObjectName(u"inventory_icon_4")
        sizePolicy1.setHeightForWidth(self.inventory_icon_4.sizePolicy().hasHeightForWidth())
        self.inventory_icon_4.setSizePolicy(sizePolicy1)
        self.inventory_icon_4.setMinimumSize(QSize(40, 40))
        self.inventory_icon_4.setMaximumSize(QSize(40, 40))
        self.inventory_icon_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(55, 50, 52);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_icon_4.setIcon(icon8)
        self.inventory_icon_4.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.inventory_icon_4, 0, 0, 1, 1)

        self.label_4 = QLabel(self.top_content_frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_7.addWidget(self.label_4, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.top_content_frame_3, 0, 0, 1, 1)

        self.content_frame_3 = QFrame(self.content_3)
        self.content_frame_3.setObjectName(u"content_frame_3")
        sizePolicy.setHeightForWidth(self.content_frame_3.sizePolicy().hasHeightForWidth())
        self.content_frame_3.setSizePolicy(sizePolicy)
        self.content_frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.content_frame_3.setFrameShape(QFrame.StyledPanel)
        self.content_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.content_frame_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.middle_frame_3 = QFrame(self.content_frame_3)
        self.middle_frame_3.setObjectName(u"middle_frame_3")
        self.middle_frame_3.setMaximumSize(QSize(16777215, 50))
        self.middle_frame_3.setFrameShape(QFrame.StyledPanel)
        self.middle_frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_69 = QGridLayout(self.middle_frame_3)
        self.gridLayout_69.setSpacing(0)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setContentsMargins(10, 5, 0, 5)
        self.frame_27 = QFrame(self.middle_frame_3)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy5.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy5)
        self.frame_27.setMaximumSize(QSize(16777215, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_27)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(10)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(10, 0, 10, 0)
        self.pushButton_9 = QPushButton(self.frame_27)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon9 = QIcon()
        icon9.addFile(u":/icons/search-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.gridLayout_9.addWidget(self.pushButton_9, 0, 0, 1, 1)

        self.clear_btn = QPushButton(self.frame_27)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setEnabled(True)
        self.clear_btn.setMinimumSize(QSize(100, 35))
        self.clear_btn.setMaximumSize(QSize(100, 35))
        self.clear_btn.setFont(font11)
        self.clear_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #191919;\n"
"border-radius: 5px;\n"
"color: white;\n"
"}")

        self.gridLayout_9.addWidget(self.clear_btn, 0, 6, 1, 1)

        self.dateEdit = QDateEdit(self.frame_27)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMaximumSize(QSize(150, 35))
        self.dateEdit.setFont(font7)
        self.dateEdit.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"  	color: black;\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"	border-radius: 5px;\n"
"    border-color: #ebebea;\n"
"	padding-left: 5px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"	subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    margin-right: 5px;\n"
"	image: url(C:/Users/James Catedrilla/Desktop/Test/Icons/calendar.svg)\n"
"}\n"
"QDateEdit QCalendarWidget {\n"
"	border:none;\n"
"}\n"
"")
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dateEdit.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.UTC)
        self.dateEdit.setDate(QDate(2023, 1, 1))

        self.gridLayout_9.addWidget(self.dateEdit, 0, 4, 1, 1)

        self.today_btn = QPushButton(self.frame_27)
        self.today_btn.setObjectName(u"today_btn")
        self.today_btn.setMinimumSize(QSize(75, 35))
        self.today_btn.setMaximumSize(QSize(50, 35))
        self.today_btn.setFont(font9)
        self.today_btn.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"border:1px solid #ebebea;\n"
"color: black;\n"
"}\n"
"QPushButton:hover {\n"
"border-radius: 5px;\n"
"border:1px solid black;\n"
"color: black;\n"
"}")

        self.gridLayout_9.addWidget(self.today_btn, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.dateEdit_2 = QDateEdit(self.frame_27)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setMaximumSize(QSize(150, 35))
        self.dateEdit_2.setFont(font7)
        self.dateEdit_2.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"  	color: black;\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"	border-radius: 5px;\n"
"    border-color: #ebebea;\n"
"	padding-left: 5px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"	subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    margin-right: 5px;\n"
"	image: url(C:/Users/James Catedrilla/Desktop/Test/Icons/calendar.svg)\n"
"}\n"
"QDateEdit QCalendarWidget {\n"
"	border:none;\n"
"}\n"
"")
        self.dateEdit_2.setFrame(True)
        self.dateEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dateEdit_2.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setTimeSpec(Qt.UTC)
        self.dateEdit_2.setDate(QDate(2023, 1, 1))

        self.gridLayout_9.addWidget(self.dateEdit_2, 0, 5, 1, 1)

        self.search_lineEdit_3 = QLineEdit(self.frame_27)
        self.search_lineEdit_3.setObjectName(u"search_lineEdit_3")
        self.search_lineEdit_3.setMinimumSize(QSize(325, 35))
        self.search_lineEdit_3.setMaximumSize(QSize(325, 35))
        self.search_lineEdit_3.setFont(font9)
        self.search_lineEdit_3.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"border:1px solid #ebebea;")
        self.search_lineEdit_3.setClearButtonEnabled(False)

        self.gridLayout_9.addWidget(self.search_lineEdit_3, 0, 1, 1, 1)


        self.gridLayout_69.addWidget(self.frame_27, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.middle_frame_3)

        self.bottom_frame_3 = QFrame(self.content_frame_3)
        self.bottom_frame_3.setObjectName(u"bottom_frame_3")
        self.bottom_frame_3.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.bottom_frame_3)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(10, 5, 10, 5)
        self.tableWidget_3 = QTableWidget(self.bottom_frame_3)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setMinimumSize(QSize(0, 0))
        self.tableWidget_3.setFont(font9)
        self.tableWidget_3.setFocusPolicy(Qt.TabFocus)
        self.tableWidget_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_3.setStyleSheet(u"QTableWidget#tableWidget_3 QHeaderView::section {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-bottom:1px solid #ebebea;\n"
"	font-family: Satoshi;\n"
"	font-size: 13px;\n"
"	height:40px;\n"
"}\n"
"QTableWidget#tableWidget_3 {\n"
"	border: 1px solid #ebebea;\n"
"	padding-left: 10px;\n"
"}\n"
"QTableWidget#tableWidget_3::item {\n"
"	font-size: 13px;\n"
"	color:#7C7C87 ;\n"
"}")
        self.tableWidget_3.setFrameShape(QFrame.NoFrame)
        self.tableWidget_3.setFrameShadow(QFrame.Plain)
        self.tableWidget_3.setLineWidth(0)
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setProperty("showDropIndicator", False)
        self.tableWidget_3.setDragDropOverwriteMode(False)
        self.tableWidget_3.setAlternatingRowColors(False)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setGridStyle(Qt.NoPen)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setWordWrap(False)
        self.tableWidget_3.setCornerButtonEnabled(False)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(148)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.gridLayout_10.addWidget(self.tableWidget_3, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.bottom_frame_3)


        self.gridLayout_11.addWidget(self.content_frame_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.content_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_12 = QGridLayout(self.page_5)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.content_5 = QWidget(self.page_5)
        self.content_5.setObjectName(u"content_5")
        self.gridLayout_13 = QGridLayout(self.content_5)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(20, 20, 20, 20)
        self.content_frame_5 = QFrame(self.content_5)
        self.content_frame_5.setObjectName(u"content_frame_5")
        self.content_frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.content_frame_5.setFrameShape(QFrame.StyledPanel)
        self.content_frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.content_frame_5)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.middle_frame_5 = QFrame(self.content_frame_5)
        self.middle_frame_5.setObjectName(u"middle_frame_5")
        self.middle_frame_5.setMinimumSize(QSize(0, 50))
        self.middle_frame_5.setMaximumSize(QSize(16777215, 50))
        self.middle_frame_5.setFrameShape(QFrame.StyledPanel)
        self.middle_frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_72 = QGridLayout(self.middle_frame_5)
        self.gridLayout_72.setSpacing(0)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setContentsMargins(10, 0, 10, 0)
        self.frame = QFrame(self.middle_frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(10)
        self.gridLayout_16.setVerticalSpacing(0)
        self.gridLayout_16.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_4 = QSpacerItem(564, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.openAddStockDialog_btn = QPushButton(self.frame)
        self.openAddStockDialog_btn.setObjectName(u"openAddStockDialog_btn")
        self.openAddStockDialog_btn.setMinimumSize(QSize(100, 35))
        self.openAddStockDialog_btn.setMaximumSize(QSize(100, 35))
        self.openAddStockDialog_btn.setFont(font2)
        self.openAddStockDialog_btn.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: white;")

        self.gridLayout_16.addWidget(self.openAddStockDialog_btn, 0, 0, 1, 1)


        self.gridLayout_72.addWidget(self.frame, 0, 2, 1, 1)


        self.gridLayout_14.addWidget(self.middle_frame_5, 1, 0, 1, 1)

        self.bottom_frame_5 = QFrame(self.content_frame_5)
        self.bottom_frame_5.setObjectName(u"bottom_frame_5")
        self.bottom_frame_5.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.bottom_frame_5)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(10, 5, 10, 5)
        self.tableWidget_4 = QTableWidget(self.bottom_frame_5)
        if (self.tableWidget_4.columnCount() < 6):
            self.tableWidget_4.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        if (self.tableWidget_4.rowCount() < 5):
            self.tableWidget_4.setRowCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem19)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setMinimumSize(QSize(0, 0))
        self.tableWidget_4.setFont(font7)
        self.tableWidget_4.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_4.setStyleSheet(u"QTableWidget#tableWidget_4 QHeaderView::section {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-bottom:1px solid black ;\n"
"	border-top:1px solid black ;\n"
"	font-family: Satoshi;\n"
"	font-size: 13px;\n"
"	height:35px;\n"
"}\n"
"")
        self.tableWidget_4.setFrameShape(QFrame.NoFrame)
        self.tableWidget_4.setFrameShadow(QFrame.Plain)
        self.tableWidget_4.setLineWidth(0)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setProperty("showDropIndicator", False)
        self.tableWidget_4.setDragDropOverwriteMode(False)
        self.tableWidget_4.setAlternatingRowColors(False)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setGridStyle(Qt.NoPen)
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setWordWrap(False)
        self.tableWidget_4.setCornerButtonEnabled(False)
        self.tableWidget_4.setRowCount(5)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setHighlightSections(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.verticalHeader().setHighlightSections(True)
        self.tableWidget_4.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(False)

        self.gridLayout_17.addWidget(self.tableWidget_4, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.bottom_frame_5, 2, 0, 1, 1)

        self.top_frame_5 = QFrame(self.content_frame_5)
        self.top_frame_5.setObjectName(u"top_frame_5")
        self.top_frame_5.setMinimumSize(QSize(0, 65))
        self.top_frame_5.setMaximumSize(QSize(16777215, 65))
        self.top_frame_5.setFrameShape(QFrame.StyledPanel)
        self.top_frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.top_frame_5)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(10, 5, 10, 5)
        self.frame_14 = QFrame(self.top_frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_74 = QGridLayout(self.frame_14)
        self.gridLayout_74.setSpacing(0)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gridLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        font12 = QFont()
        font12.setFamilies([u"Satoshi Medium"])
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setStrikeOut(False)
        font12.setKerning(True)
        font12.setStyleStrategy(QFont.PreferAntialias)
        self.label_5.setFont(font12)
        self.label_5.setStyleSheet(u"")

        self.gridLayout_74.addWidget(self.label_5, 0, 1, 1, 1)

        self.inventory_icon_5 = QPushButton(self.frame_14)
        self.inventory_icon_5.setObjectName(u"inventory_icon_5")
        sizePolicy1.setHeightForWidth(self.inventory_icon_5.sizePolicy().hasHeightForWidth())
        self.inventory_icon_5.setSizePolicy(sizePolicy1)
        self.inventory_icon_5.setMinimumSize(QSize(40, 40))
        self.inventory_icon_5.setMaximumSize(QSize(40, 40))
        self.inventory_icon_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(55, 50, 52);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f5f5f5;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/boxes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_icon_5.setIcon(icon10)
        self.inventory_icon_5.setIconSize(QSize(20, 20))

        self.gridLayout_74.addWidget(self.inventory_icon_5, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_14, 0, 0, 1, 1)

        self.line_4 = QFrame(self.top_frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_15.addWidget(self.line_4, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.top_frame_5, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.content_frame_5, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.content_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_37 = QGridLayout(self.page_2)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.content_2 = QWidget(self.page_2)
        self.content_2.setObjectName(u"content_2")
        sizePolicy.setHeightForWidth(self.content_2.sizePolicy().hasHeightForWidth())
        self.content_2.setSizePolicy(sizePolicy)
        self.gridLayout_39 = QGridLayout(self.content_2)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.top_content_frame_2 = QFrame(self.content_2)
        self.top_content_frame_2.setObjectName(u"top_content_frame_2")
        self.top_content_frame_2.setMinimumSize(QSize(0, 70))
        self.top_content_frame_2.setStyleSheet(u"QFrame #top_content_frame_2 {\n"
"border-top: 1px solid #ebebea;\n"
"border-bottom: 1px solid #ebebea;\n"
"}")
        self.top_content_frame_2.setFrameShape(QFrame.StyledPanel)
        self.top_content_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_77 = QGridLayout(self.top_content_frame_2)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.inventory_icon_7 = QPushButton(self.top_content_frame_2)
        self.inventory_icon_7.setObjectName(u"inventory_icon_7")
        sizePolicy1.setHeightForWidth(self.inventory_icon_7.sizePolicy().hasHeightForWidth())
        self.inventory_icon_7.setSizePolicy(sizePolicy1)
        self.inventory_icon_7.setMinimumSize(QSize(40, 40))
        self.inventory_icon_7.setMaximumSize(QSize(40, 40))
        self.inventory_icon_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(55, 50, 52);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/cart3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_icon_7.setIcon(icon11)
        self.inventory_icon_7.setIconSize(QSize(20, 20))

        self.gridLayout_77.addWidget(self.inventory_icon_7, 0, 0, 1, 1)

        self.label_16 = QLabel(self.top_content_frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_77.addWidget(self.label_16, 0, 1, 1, 1)


        self.gridLayout_39.addWidget(self.top_content_frame_2, 0, 0, 1, 1)

        self.content_frame_2 = QFrame(self.content_2)
        self.content_frame_2.setObjectName(u"content_frame_2")
        sizePolicy.setHeightForWidth(self.content_frame_2.sizePolicy().hasHeightForWidth())
        self.content_frame_2.setSizePolicy(sizePolicy)
        self.content_frame_2.setStyleSheet(u"border-radius: 15px;")
        self.content_frame_2.setFrameShape(QFrame.StyledPanel)
        self.content_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.content_frame_2)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(10, 10, 10, 10)
        self.bottom_frame_2 = QFrame(self.content_frame_2)
        self.bottom_frame_2.setObjectName(u"bottom_frame_2")
        self.bottom_frame_2.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.bottom_frame_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 5, 10, 5)
        self.tableWidget_2 = QTableWidget(self.bottom_frame_2)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setMinimumSize(QSize(0, 0))
        self.tableWidget_2.setFont(font9)
        self.tableWidget_2.setFocusPolicy(Qt.TabFocus)
        self.tableWidget_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_2.setStyleSheet(u"QTableWidget#tableWidget_2 QHeaderView::section {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-bottom:1px solid #ebebea;\n"
"	font-family: Satoshi;\n"
"	font-size: 13px;\n"
"	height:40px;\n"
"}\n"
"QTableWidget#tableWidget_2 {\n"
"	border: 1px solid #ebebea;\n"
"	padding-left: 10px;\n"
"}\n"
"QTableWidget#tableWidget_2::item {\n"
"	font-size: 13px;\n"
"	color:#7C7C87 ;\n"
"}\n"
"\n"
"")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setFrameShadow(QFrame.Plain)
        self.tableWidget_2.setLineWidth(0)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setProperty("showDropIndicator", False)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setGridStyle(Qt.NoPen)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setWordWrap(False)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(127)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.tableWidget_2, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.bottom_frame_2, 1, 0, 1, 1)

        self.middle_frame_2 = QFrame(self.content_frame_2)
        self.middle_frame_2.setObjectName(u"middle_frame_2")
        sizePolicy.setHeightForWidth(self.middle_frame_2.sizePolicy().hasHeightForWidth())
        self.middle_frame_2.setSizePolicy(sizePolicy)
        self.middle_frame_2.setMinimumSize(QSize(0, 50))
        self.middle_frame_2.setMaximumSize(QSize(16777215, 50))
        self.middle_frame_2.setFrameShape(QFrame.StyledPanel)
        self.middle_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_71 = QGridLayout(self.middle_frame_2)
        self.gridLayout_71.setSpacing(0)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(10, 5, 0, 5)
        self.frame_24 = QFrame(self.middle_frame_2)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_70 = QGridLayout(self.frame_24)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setHorizontalSpacing(10)
        self.gridLayout_70.setVerticalSpacing(0)
        self.gridLayout_70.setContentsMargins(10, 0, 10, 0)
        self.pushButton_4 = QPushButton(self.frame_24)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border: none;")
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.gridLayout_70.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.search_lineEdit_2 = QLineEdit(self.frame_24)
        self.search_lineEdit_2.setObjectName(u"search_lineEdit_2")
        sizePolicy.setHeightForWidth(self.search_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.search_lineEdit_2.setSizePolicy(sizePolicy)
        self.search_lineEdit_2.setMinimumSize(QSize(325, 35))
        self.search_lineEdit_2.setMaximumSize(QSize(325, 35))
        self.search_lineEdit_2.setFont(font9)
        self.search_lineEdit_2.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"border:1px solid #ebebea;")
        self.search_lineEdit_2.setClearButtonEnabled(False)

        self.gridLayout_70.addWidget(self.search_lineEdit_2, 0, 1, 1, 1)

        self.openOrderDialog_btn = QPushButton(self.frame_24)
        self.openOrderDialog_btn.setObjectName(u"openOrderDialog_btn")
        self.openOrderDialog_btn.setMinimumSize(QSize(100, 35))
        self.openOrderDialog_btn.setMaximumSize(QSize(100, 40))
        self.openOrderDialog_btn.setFont(font11)
        self.openOrderDialog_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #191919;\n"
"border-radius: 5px;\n"
"color: white;\n"
"}")

        self.gridLayout_70.addWidget(self.openOrderDialog_btn, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_70.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.gridLayout_71.addWidget(self.frame_24, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.middle_frame_2, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.content_frame_2, 1, 0, 1, 1)


        self.gridLayout_37.addWidget(self.content_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_35.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_36.addWidget(self.widget_pages, 1, 1, 1, 1)

        self.widget_left_menu = QWidget(self.Content)
        self.widget_left_menu.setObjectName(u"widget_left_menu")
        sizePolicy.setHeightForWidth(self.widget_left_menu.sizePolicy().hasHeightForWidth())
        self.widget_left_menu.setSizePolicy(sizePolicy)
        self.widget_left_menu.setMinimumSize(QSize(250, 0))
        self.widget_left_menu.setMaximumSize(QSize(250, 16777215))
        self.widget_left_menu.setStyleSheet(u"")
        self.gridLayout_75 = QGridLayout(self.widget_left_menu)
        self.gridLayout_75.setSpacing(0)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.gridLayout_75.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.widget_left_menu)
        self.logo_frame.setObjectName(u"logo_frame")
        sizePolicy3.setHeightForWidth(self.logo_frame.sizePolicy().hasHeightForWidth())
        self.logo_frame.setSizePolicy(sizePolicy3)
        self.logo_frame.setMinimumSize(QSize(0, 69))
        self.logo_frame.setMaximumSize(QSize(16777215, 69))
        self.logo_frame.setStyleSheet(u"border-right: 1px solid #ebebea;\n"
"border-top: 1px solid #ebebea;\n"
"")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.logo_frame)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.pushButton_14 = QPushButton(self.logo_frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 0))
        self.pushButton_14.setMaximumSize(QSize(16777215, 70))
        self.pushButton_14.setStyleSheet(u"border:none;\n"
"text-align:left;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon12)
        self.pushButton_14.setIconSize(QSize(175, 175))

        self.gridLayout_38.addWidget(self.pushButton_14, 0, 0, 1, 1)


        self.gridLayout_75.addWidget(self.logo_frame, 0, 0, 1, 1)

        self.widget_top_menu = QWidget(self.widget_left_menu)
        self.widget_top_menu.setObjectName(u"widget_top_menu")
        sizePolicy.setHeightForWidth(self.widget_top_menu.sizePolicy().hasHeightForWidth())
        self.widget_top_menu.setSizePolicy(sizePolicy)
        self.widget_top_menu.setMaximumSize(QSize(16777215, 16777215))
        self.widget_top_menu.setStyleSheet(u"background-color: white;\n"
"border-right: 1px solid #ebebea;\n"
"border-top: 1px solid #ebebea;")
        self.verticalLayout_6 = QVBoxLayout(self.widget_top_menu)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.btn_menu_1 = QPushButton(self.widget_top_menu)
        self.btn_menu_1.setObjectName(u"btn_menu_1")
        self.btn_menu_1.setMinimumSize(QSize(0, 50))
        self.btn_menu_1.setFont(font8)
        self.btn_menu_1.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color:white;\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f4f4f4;\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_menu_1.setIcon(icon)
        self.btn_menu_1.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.btn_menu_1)

        self.btn_menu_2 = QPushButton(self.widget_top_menu)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setMinimumSize(QSize(0, 50))
        self.btn_menu_2.setFont(font8)
        self.btn_menu_2.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color:white;\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f4f4f4;\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_menu_2.setIcon(icon11)
        self.btn_menu_2.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.btn_menu_2)

        self.btn_menu_3 = QPushButton(self.widget_top_menu)
        self.btn_menu_3.setObjectName(u"btn_menu_3")
        self.btn_menu_3.setMinimumSize(QSize(0, 50))
        self.btn_menu_3.setFont(font8)
        self.btn_menu_3.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color:white;\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f4f4f4;\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_menu_3.setIcon(icon8)
        self.btn_menu_3.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.btn_menu_3)

        self.btn_menu_4 = QPushButton(self.widget_top_menu)
        self.btn_menu_4.setObjectName(u"btn_menu_4")
        self.btn_menu_4.setMinimumSize(QSize(0, 50))
        self.btn_menu_4.setFont(font8)
        self.btn_menu_4.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color:white;\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #f4f4f4;\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_menu_4.setIcon(icon5)
        self.btn_menu_4.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.btn_menu_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.logout_btn = QPushButton(self.widget_top_menu)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setMinimumSize(QSize(0, 50))
        self.logout_btn.setFont(font8)
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color:black;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #191919;\n"
"	border-radius: 10px;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon13)
        self.logout_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.logout_btn)


        self.gridLayout_75.addWidget(self.widget_top_menu, 1, 0, 1, 2)


        self.gridLayout_36.addWidget(self.widget_left_menu, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.inventory_icon_6.setText("")
        self.year_dropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Year", None))
        self.month_dropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Month", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"`Stock Received", None))
        self.stockreceived_label.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total Stocks", None))
        self.totalstocks_label_2.setText(QCoreApplication.translate("MainWindow", u"1500", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Inventory Summary", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Inventory Overview", None))
        self.pushButton_7.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sold Stocks Today", None))
        self.soldstockstoday_label.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_8.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Total Sold Stocks", None))
        self.totalsoldstocks_label.setText(QCoreApplication.translate("MainWindow", u"1500", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None))
        self.totalsales_label.setText(QCoreApplication.translate("MainWindow", u"1200", None))
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sales Overview", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Today Sales", None))
        self.todaysales_label.setText(QCoreApplication.translate("MainWindow", u"1250", None))
        self.pushButton.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Product Details", None))
        self.no_items_label_2.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"No of Items", None))
        self.no_category_label_2.setText(QCoreApplication.translate("MainWindow", u"05", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Item Group", None))
        self.lowstockitems_label_2.setText(QCoreApplication.translate("MainWindow", u"02", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Low Stock Items", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Low Stock Items", None))
        self.item1_stock.setText("")
        self.itemname_1.setText("")
        self.item2_stock.setText("")
        self.itemname_2.setText("")
        self.item3_stock.setText("")
        self.itemname_3.setText("")
        self.itemname_4.setText("")
        self.item4_stock.setText("")
        self.itemname_5.setText("")
        self.item5_stock.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Inventory Analysis", None))
        self.inventory_icon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inventory Management", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date Added", None));
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.openAddDialog_btn.setText(QCoreApplication.translate("MainWindow", u"New Item", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.openAddStock_btn.setText(QCoreApplication.translate("MainWindow", u"Add Stock", None))
        self.inventory_icon_4.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stock History", None))
        self.pushButton_9.setText("")
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.today_btn.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.search_lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Transaction ID", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Item ID", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Transaction Date", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Stock Supply", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Current Stock", None));
        self.openAddStockDialog_btn.setText(QCoreApplication.translate("MainWindow", u"Add Stock", None))
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Item ID", None));
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Price", None));

        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stock Management", None))
        self.inventory_icon_5.setText("")
        self.inventory_icon_7.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Purchase List", None))
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Order ID", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Discount", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Purchase Date", None));
        self.pushButton_4.setText("")
        self.search_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.openOrderDialog_btn.setText(QCoreApplication.translate("MainWindow", u"New Order", None))
        self.pushButton_14.setText("")
        self.btn_menu_1.setText(QCoreApplication.translate("MainWindow", u"   Dashboard", None))
        self.btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"   Purchase Entry", None))
        self.btn_menu_3.setText(QCoreApplication.translate("MainWindow", u"   Stock History", None))
        self.btn_menu_4.setText(QCoreApplication.translate("MainWindow", u"   Inventory", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"   Logout", None))
    # retranslateUi

