# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Air Navigation Toolkit"
        self.width = 1200
        self.height = 800
        self.setup_ui(self)

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowTitle(self.title)
        main_window.resize(self.width, self.height)
        main_window.setMinimumSize(QtCore.QSize(self.width, self.height))
        main_window.setMaximumSize(QtCore.QSize(self.width, self.height))
        font = QtGui.QFont()
        font.setFamily("GOST type A")
        font.setPointSize(14)
        main_window.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_globe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget)

        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.setGeometry(QtCore.QRect(1, 0, 1200, 760))
        self.tab_widget.setFont(font)
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setObjectName("tab_widget")

        self.arp_tab = QtWidgets.QWidget()
        self.arp_tab.setObjectName("arp_tab")
        self.tab_widget.addTab(self.arp_tab, "AD - Aerodrome Info")

        self.arp_table = QtWidgets.QTableView(self.arp_tab)
        self.arp_table.setGeometry(QtCore.QRect(20, 50, 600, 150))
        self.arp_table.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.arp_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.arp_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.arp_table.setObjectName("arp_table")

        self.star_tab = QtWidgets.QWidget()
        self.star_tab.setObjectName("star_tab")
        self.tab_widget.addTab(self.star_tab, "STAR - Standart Terminal Arrival Routes")

        self.sid_tab = QtWidgets.QWidget()
        self.sid_tab.setObjectName("sid_tab")
        self.tab_widget.addTab(self.sid_tab, "SID - Standart Instrument Departure")

        self.apch_tab = QtWidgets.QWidget()
        self.apch_tab.setObjectName("apch_tab")
        self.tab_widget.addTab(self.apch_tab, "APCH - Instrument Approach")

        self.ma_tab = QtWidgets.QWidget()
        self.ma_tab.setObjectName("ma_tab")
        self.tab_widget.addTab(self.ma_tab, "MA - Missed Approach")

        self.wp_tab = QtWidgets.QWidget()
        self.wp_tab.setObjectName("wp_tab")
        self.tab_widget.addTab(self.wp_tab, "WP - Waypoints ")

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 25))
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.menu_file = QtWidgets.QMenu(self.menubar)
        font.setPointSize(10)
        self.menu_file.setFont(font)
        self.menu_file.setObjectName("menu_file")

        self.menu_save = QtWidgets.QMenu(self.menu_file)
        self.menu_save.setFont(font)
        self.menu_save.setObjectName("menu_save")

        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setFont(font)
        self.menu_help.setObjectName("menu_help")

        self.action_new = QtWidgets.QAction(main_window)
        self.action_new.setText("New")
        self.action_new.setIconText("New")
        self.action_new.setFont(font)
        self.action_new.setObjectName("action_new")

        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setText("Open")
        self.action_open.setIconText("Open")
        self.action_open.setFont(font)
        self.action_open.setObjectName("action_open")

        self.action_close = QtWidgets.QAction(main_window)
        self.action_close.setText("Close")
        self.action_close.setIconText("Close")
        self.action_close.setObjectName("action_close")

        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setText("Save")
        self.action_save.setIconText("Save")
        self.action_save.setObjectName("action_save")

        self.action_save_as = QtWidgets.QAction(main_window)
        self.action_save_as.setText("Save as...")
        self.action_save_as.setIconText("Save as")
        self.action_save_as.setObjectName("action_save_as")

        self.action_about = QtWidgets.QAction(main_window)
        self.action_about.setText("About")
        self.action_about.setIconText("About")
        self.action_about.setObjectName("action_about")

        self.menu_save.addAction(self.action_save)
        self.menu_save.addAction(self.action_save_as)
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.menu_save.menuAction())
        self.menu_file.addAction(self.action_close)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(main_window)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.setWindowTitle('Center')
        self.statusBar().showMessage('Ready')
        self.show()

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        self.menu_file.setTitle(_translate("main_window", "File"))
        self.menu_save.setTitle(_translate("main_window", "Save"))
        self.menu_help.setTitle(_translate("main_window", "Help"))

    def center(self):
        frame = self.frameGeometry()
        monitor = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(monitor)
        self.move(frame.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


