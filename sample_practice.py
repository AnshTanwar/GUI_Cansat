# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1716, 1030)
        MainWindow.setStyleSheet("background-color:#303030")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")#1
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:#303030;\n"
"border-radius:10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frame_2.setStyleSheet("\n"
"border-radius:5px;\n"
"background-color:#303030")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_3.setStyleSheet("background-color:#595959;\n"
"padding: 1px;\n"
"border-radius:5px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.NameSymbol = QtWidgets.QFrame(self.frame_3)
        self.NameSymbol.setMinimumSize(QtCore.QSize(237, 66))
        self.NameSymbol.setStyleSheet("background-color:rgb(89, 89, 89);")
        self.NameSymbol.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NameSymbol.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NameSymbol.setObjectName("NameSymbol")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.NameSymbol)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.NameSymbol)
        self.label_7.setMinimumSize(QtCore.QSize(10, 0))
        self.label_7.setMaximumSize(QtCore.QSize(57, 49))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icons/space-shuttle.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 11, -1, 19)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.NameSymbol)
        self.label_5.setStyleSheet("border:none")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.NameSymbol)
        self.label_6.setStyleSheet("border:none;\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.horizontalLayout_5.addWidget(self.NameSymbol, 0, QtCore.Qt.AlignLeft)
        self.Commands = QtWidgets.QFrame(self.frame_3)
        self.Commands.setMinimumSize(QtCore.QSize(900, 90))
        self.Commands.setStyleSheet("background-color:rgb(89, 89, 89)")
        self.Commands.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Commands.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Commands.setObjectName("Commands")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Commands)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_31 = QtWidgets.QFrame(self.Commands)
        self.frame_31.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_31.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_31.setStyleSheet("background-color:rgb(89, 89, 89);\n"
"border: solid grey;\n"
"border-width: 0px 3px 0px 3px\n"
"")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_17.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_17.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_17.setStyleSheet("border: 6px solid white;\n"
"border-radius:12px\n"
"")
        self.pushButton_17.setText("")
        self.pushButton_17.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_19.addWidget(self.pushButton_17, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_16 = QtWidgets.QLabel(self.frame_31)
        self.label_16.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border:none")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_19.addWidget(self.label_16, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_31)
        self.frame_30 = QtWidgets.QFrame(self.Commands)
        self.frame_30.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_30.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_30.setStyleSheet("background-color:rgb(89, 89, 89);\n"
"border: solid grey;\n"
"border-width: 0px 3px 0px 0px")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_30)
        self.pushButton_16.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_16.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_16.setStyleSheet("border: 6px solid white;\n"
"border-radius:12px;\n"
"")
        self.pushButton_16.setText("")
        self.pushButton_16.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_18.addWidget(self.pushButton_16, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_15 = QtWidgets.QLabel(self.frame_30)
        self.label_15.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:none")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_18.addWidget(self.label_15, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_30)
        self.frame_26 = QtWidgets.QFrame(self.Commands)
        self.frame_26.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_26.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_26.setStyleSheet("background-color:rgb(89, 89, 89);\n"
"border: solid grey;\n"
"border-width: 0px 3px 0px 0px")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_11.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_11.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_11.setStyleSheet("border: 6px solid white;\n"
"border-radius:12px\n"
"")
        self.pushButton_11.setText("")
        self.pushButton_11.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_14.addWidget(self.pushButton_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11 = QtWidgets.QLabel(self.frame_26)
        self.label_11.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border:none")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.Commands)
        self.frame_27.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_27.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_27.setStyleSheet("background-color:rgb(89, 89, 89);\n"
"border: solid grey;\n"
"border-width: 0px 3px 0px 0px")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_13.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_13.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_13.setStyleSheet("border: 6px solid white;\n"
"border-radius:12px\n"
"")
        self.pushButton_13.setText("")
        self.pushButton_13.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_15.addWidget(self.pushButton_13, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_12 = QtWidgets.QLabel(self.frame_27)
        self.label_12.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border:none")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(self.label_12, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_27)
        self.frame_29 = QtWidgets.QFrame(self.Commands)
        self.frame_29.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_29.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_29.setStyleSheet("background-color:rgb(89, 89, 89);\n"
"border: solid grey;\n"
"border-width: 0px 3px 0px 0px")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_15.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_15.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_15.setStyleSheet("border: 6px solid white;\n"
"border-radius:12px\n"
"")
        self.pushButton_15.setText("")
        self.pushButton_15.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_17.addWidget(self.pushButton_15, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_14 = QtWidgets.QLabel(self.frame_29)
        self.label_14.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border:none")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_17.addWidget(self.label_14, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_29)
        self.frame_28 = QtWidgets.QFrame(self.Commands)
        self.frame_28.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_28.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_28.setStyleSheet("background-color:rgb(89, 89, 89);\n"
"border: solid grey;\n"
"border-width: 0px 3px 0px 0px")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_14.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_14.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_14.setStyleSheet("border: 6px solid white;\n"
"border-radius:12px\n"
"")
        self.pushButton_14.setText("")
        self.pushButton_14.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_16.addWidget(self.pushButton_14, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13 = QtWidgets.QLabel(self.frame_28)
        self.label_13.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border:none")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_28)
        self.horizontalLayout_5.addWidget(self.Commands)
        self.Packetstime = QtWidgets.QFrame(self.frame_3)
        self.Packetstime.setMinimumSize(QtCore.QSize(301, 70))
        self.Packetstime.setStyleSheet("background-color:rgb(42, 42, 42)")
        self.Packetstime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Packetstime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Packetstime.setObjectName("Packetstime")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Packetstime)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.Packetstime)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.Packetstime)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Packetstime)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_5.addWidget(self.Packetstime, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("\n"
"background-color:#2A2A2A")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 800))
        self.scrollArea.setStyleSheet("border-radius:10px")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -768, 1629, 1589))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet("background-color:#2A2A2A;\n"
"border-radius:10px")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.part1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.part1.setMinimumSize(QtCore.QSize(0, 780))
        self.part1.setStyleSheet("background-color:#2A2A2A")
        self.part1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part1.setObjectName("part1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.part1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_9 = QtWidgets.QFrame(self.part1)
        self.frame_9.setMaximumSize(QtCore.QSize(350, 670))
        self.frame_9.setStyleSheet("background-color:#595959;\n"
"border-radius:10px")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setMinimumSize(QtCore.QSize(277, 290))
        self.frame_15.setStyleSheet("background-color:#2A2A2A")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_7.addWidget(self.frame_15, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setMinimumSize(QtCore.QSize(277, 281))
        self.frame_14.setStyleSheet("background-color:#2A2A2A")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_7.addWidget(self.frame_14, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.part1)
        self.frame_12.setMaximumSize(QtCore.QSize(350, 670))
        self.frame_12.setStyleSheet("background-color:#595959;\n"
"border-radius:10px")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_17 = QtWidgets.QFrame(self.frame_12)
        self.frame_17.setMinimumSize(QtCore.QSize(300, 179))
        self.frame_17.setStyleSheet("background-color:#2A2A2A")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_8.addWidget(self.frame_17, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_18 = QtWidgets.QFrame(self.frame_12)
        self.frame_18.setMinimumSize(QtCore.QSize(300, 180))
        self.frame_18.setStyleSheet("background-color:#2A2A2A")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_8.addWidget(self.frame_18, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_23 = QtWidgets.QFrame(self.frame_12)
        self.frame_23.setMinimumSize(QtCore.QSize(300, 180))
        self.frame_23.setStyleSheet("background-color:#2A2A2A")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_8.addWidget(self.frame_23, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_12)
        self.frame_10 = QtWidgets.QFrame(self.part1)
        self.frame_10.setMaximumSize(QtCore.QSize(350, 670))
        self.frame_10.setStyleSheet("background-color:#595959;\n"
"border-radius:10px")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_19 = QtWidgets.QFrame(self.frame_10)
        self.frame_19.setMinimumSize(QtCore.QSize(300, 179))
        self.frame_19.setStyleSheet("background-color:#2A2A2A")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_9.addWidget(self.frame_19, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_20 = QtWidgets.QFrame(self.frame_10)
        self.frame_20.setMinimumSize(QtCore.QSize(300, 179))
        self.frame_20.setStyleSheet("background-color:#2A2A2A")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_9.addWidget(self.frame_20, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_21 = QtWidgets.QFrame(self.frame_10)
        self.frame_21.setMinimumSize(QtCore.QSize(300, 179))
        self.frame_21.setStyleSheet("background-color:#2A2A2A")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_9.addWidget(self.frame_21, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.part1)
        self.frame_11.setMaximumSize(QtCore.QSize(350, 670))
        self.frame_11.setStyleSheet("background-color:#595959;\n"
"border-radius:10px")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_22 = QtWidgets.QFrame(self.frame_11)
        self.frame_22.setMinimumSize(QtCore.QSize(280, 605))
        self.frame_22.setStyleSheet("background-color:#2A2A2A")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_10.addWidget(self.frame_22, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_11)
        self.verticalLayout_4.addWidget(self.part1)
        self.part2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.part2.setMinimumSize(QtCore.QSize(0, 780))
        self.part2.setStyleSheet("background-color:#2A2A2A")
        self.part2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part2.setObjectName("part2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.part2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.part2)
        self.frame_5.setStyleSheet("background-color:#2A2A2A")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setMinimumSize(QtCore.QSize(678, 644))
        self.frame_13.setStyleSheet("background-color:rgb(89, 89, 89)")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label = QtWidgets.QLabel(self.frame_13)
        self.label.setGeometry(QtCore.QRect(150, 120, 351, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/Picture1.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.frame_13, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.part2)
        self.frame_6.setStyleSheet("background-color:#2A2A2A")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_7.setStyleSheet("background-color:rgb(89, 89, 89)\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_8.setStyleSheet("background-color:rgb(89, 89, 89)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.part2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#2b2b2b;\">Team: NSUT</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#2b2b2b;\">Team Id: #4098</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">Set Time</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">Callibrate</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">SIM Enable</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">SIM Disable</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">SIM Activate</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">On/Off</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Team ID: _____ </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Packet: _____</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Time: _____</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())