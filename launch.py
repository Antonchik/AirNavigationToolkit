import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import MainWindow


class ExampleApp(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


app = QApplication(sys.argv)
ex = ExampleApp()
ex.show()
model = QStandardItemModel()
model.setHorizontalHeaderLabels(['Threshold', 'Lat', 'Lon', 'Elevation'])
a = '24R'
model.appendRow(QStandardItem(a))
ex.arp_table.setModel(model)
sys.exit(app.exec_())