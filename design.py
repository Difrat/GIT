# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator_Two.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/calculate_black_24dp.svg", QSize(), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"color:white;\n"
"background-color:#222222;\n"
"font-family:Engravers MT;\n"
"font-size:18pt;\n"
"font-weight:1000;\n"
"}\n"
"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #555;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_temp, 0, 0, 1, 1)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(16)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_entry, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.Button_5 = QPushButton(self.centralwidget)
        self.Button_5.setObjectName(u"Button_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_5, 2, 1, 1, 1)

        self.Button_8 = QPushButton(self.centralwidget)
        self.Button_8.setObjectName(u"Button_8")
        sizePolicy1.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_8, 1, 1, 1, 1)

        self.Button_Backspace = QPushButton(self.centralwidget)
        self.Button_Backspace.setObjectName(u"Button_Backspace")
        sizePolicy1.setHeightForWidth(self.Button_Backspace.sizePolicy().hasHeightForWidth())
        self.Button_Backspace.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/backspace_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Backspace.setIcon(icon1)
        self.Button_Backspace.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.Button_Backspace, 0, 2, 1, 1)

        self.Button_2 = QPushButton(self.centralwidget)
        self.Button_2.setObjectName(u"Button_2")
        sizePolicy1.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_2, 3, 1, 1, 1)

        self.Button_clear = QPushButton(self.centralwidget)
        self.Button_clear.setObjectName(u"Button_clear")
        sizePolicy1.setHeightForWidth(self.Button_clear.sizePolicy().hasHeightForWidth())
        self.Button_clear.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_clear, 0, 0, 1, 1)

        self.Button_3 = QPushButton(self.centralwidget)
        self.Button_3.setObjectName(u"Button_3")
        sizePolicy1.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_3, 3, 2, 1, 1)

        self.Button_0 = QPushButton(self.centralwidget)
        self.Button_0.setObjectName(u"Button_0")
        sizePolicy1.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_0, 4, 1, 1, 1)

        self.Button_4 = QPushButton(self.centralwidget)
        self.Button_4.setObjectName(u"Button_4")
        sizePolicy1.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_4, 2, 0, 1, 1)

        self.Button_CE = QPushButton(self.centralwidget)
        self.Button_CE.setObjectName(u"Button_CE")
        sizePolicy1.setHeightForWidth(self.Button_CE.sizePolicy().hasHeightForWidth())
        self.Button_CE.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_CE, 0, 1, 1, 1)

        self.Button_9 = QPushButton(self.centralwidget)
        self.Button_9.setObjectName(u"Button_9")
        sizePolicy1.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_9, 1, 2, 1, 1)

        self.Button_Mult = QPushButton(self.centralwidget)
        self.Button_Mult.setObjectName(u"Button_Mult")
        sizePolicy1.setHeightForWidth(self.Button_Mult.sizePolicy().hasHeightForWidth())
        self.Button_Mult.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_Mult, 1, 3, 1, 1)

        self.Button_1 = QPushButton(self.centralwidget)
        self.Button_1.setObjectName(u"Button_1")
        sizePolicy1.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_1, 3, 0, 1, 1)

        self.Button_6 = QPushButton(self.centralwidget)
        self.Button_6.setObjectName(u"Button_6")
        sizePolicy1.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_6, 2, 2, 1, 1)

        self.Button_7 = QPushButton(self.centralwidget)
        self.Button_7.setObjectName(u"Button_7")
        sizePolicy1.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_7, 1, 0, 1, 1)

        self.Button_Dot = QPushButton(self.centralwidget)
        self.Button_Dot.setObjectName(u"Button_Dot")
        sizePolicy1.setHeightForWidth(self.Button_Dot.sizePolicy().hasHeightForWidth())
        self.Button_Dot.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_Dot, 4, 2, 1, 1)

        self.Button_Neg = QPushButton(self.centralwidget)
        self.Button_Neg.setObjectName(u"Button_Neg")
        sizePolicy1.setHeightForWidth(self.Button_Neg.sizePolicy().hasHeightForWidth())
        self.Button_Neg.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_Neg, 2, 3, 1, 1)

        self.Button_Calc = QPushButton(self.centralwidget)
        self.Button_Calc.setObjectName(u"Button_Calc")
        sizePolicy1.setHeightForWidth(self.Button_Calc.sizePolicy().hasHeightForWidth())
        self.Button_Calc.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_Calc, 4, 3, 1, 1)

        self.Button_Add = QPushButton(self.centralwidget)
        self.Button_Add.setObjectName(u"Button_Add")
        sizePolicy1.setHeightForWidth(self.Button_Add.sizePolicy().hasHeightForWidth())
        self.Button_Add.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_Add, 3, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_13, 4, 0, 1, 1)

        self.Button_Div = QPushButton(self.centralwidget)
        self.Button_Div.setObjectName(u"Button_Div")
        sizePolicy1.setHeightForWidth(self.Button_Div.sizePolicy().hasHeightForWidth())
        self.Button_Div.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.Button_Div, 0, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator_One", None))
        self.lbl_temp.setText(QCoreApplication.translate("MainWindow", u"6+9=15", None))
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Button_Backspace.setText("")
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Button_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.Button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Button_Mult.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Button_Dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Button_Neg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Button_Calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Button_Add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.Button_Div.setText(QCoreApplication.translate("MainWindow", u"/", None))
    # retranslateUi

