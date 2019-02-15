# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget, QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Air Navigation Toolkit'
        self.width = 1200
        self.height = 800
        self.setup_ui()

    def setup_ui(self):
        """Main window properties:"""
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.setMinimumSize(QtCore.QSize(self.width, self.height))
        self.setMaximumSize(QtCore.QSize(self.width, self.height))
        self.center()

        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('icon_globe.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        """Central widget properties:"""
        tabs = QtWidgets.QTabWidget()
        self.setCentralWidget(tabs)

        arp_tab = QtWidgets.QWidget()
        tabs.addTab(arp_tab, 'AD - Aerodrome Info')

        star_tab = QtWidgets.QWidget()
        tabs.addTab(star_tab, 'STAR - Standart Terminal Arrival Routes')

        sid_tab = QtWidgets.QWidget()
        tabs.addTab(sid_tab, 'SID - Standart Instrument Departure')

        apch_tab = QtWidgets.QWidget()
        tabs.addTab(apch_tab, 'APCH - Instrument Approach')

        ma_tab = QtWidgets.QWidget()
        tabs.addTab(ma_tab, 'MA - Missed Approach')

        wp_tab = QtWidgets.QWidget()
        tabs.addTab(wp_tab, 'WP - Waypoints')

        """Actions list:"""
        action_quit = QAction(QIcon('icon_quit'), '&Exit', self)
        action_quit.setShortcut('Ctrl+Q')
        action_quit.triggered.connect(self.close)

        action_new = QAction(QIcon('icon_new'), '&New', self)
        action_new.setShortcut('Ctrl+N')
        # action_new.triggered.connect()

        action_open = QAction(QIcon('icon_open'), '&Open', self)
        action_open.setShortcut('Ctrl+O')
        # action_open.triggered.connect()

        action_save = QAction(QIcon('icon_save'), '&Save', self)
        action_save.setShortcut('Ctrl+S')
        # action_save.triggered.connect()

        action_save_as = QAction(QIcon('icon_save_as'), '&Save as...', self)
        action_save_as.setShortcut('Ctrl+Alt+S')
        # action_save.triggered.connect()

        action_close = QAction(QIcon('icon_close'), '&Close', self)
        action_close.setShortcut('Ctrl+Alt+Q')
        # action_close.triggered.connect()

        action_about = QAction(QIcon('icon_about'), '&About', self)
        # action_close.triggered.connect()

        """Status bar"""
        statusbar = QtWidgets.QStatusBar()
        statusbar.setSizeGripEnabled(False)
        self.setStatusBar(statusbar)

        """Menu bar"""
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')

        save_menu = QtWidgets.QMenu(file_menu)
        save_menu.setTitle('Save')
        save_menu.setIcon(QIcon('icon_save'))
        save_menu.addAction(action_save)
        save_menu.addAction(action_save_as)

        file_menu.addAction(action_quit)
        file_menu.addAction(action_new)
        file_menu.addAction(action_open)
        file_menu.addAction(save_menu.menuAction())
        file_menu.addAction(action_close)
        file_menu.addAction(action_quit)
        help_menu = menubar.addMenu('&Help')
        help_menu.addAction(action_about)

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(action_new)
        toolbar.addAction(action_open)
        toolbar.addAction(action_save)
        toolbar.addAction(action_quit)

        self.statusBar().showMessage('Ready')
        self.show()

    def center(self):
        frame = self.frameGeometry()
        monitor = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(monitor)
        self.move(frame.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Warning message',
                                     'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
