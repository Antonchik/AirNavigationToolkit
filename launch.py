import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import MainWindow

app = QApplication(sys.argv)
ex = MainWindow.Ui_MainWindow()
ex.show()

model = QStandardItemModel()
model.setHorizontalHeaderLabels(['Threshold', 'Lat', 'Lon', 'Elevation'])
a = '24R'
model.appendRow(QStandardItem(a))
ex.arp_table.setModel(model)

sys.exit(app.exec_())