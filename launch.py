import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import mainwindow


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = mainwindow.App()

    # model = QStandardItemModel()
    # model.setHorizontalHeaderLabels(['Threshold', 'Lat', 'Lon', 'Elevation', 'Clearway'])
    # model.appendRow(QStandardItem('24R'))
    # ex.arp_table.setModel(model)

    sys.exit(app.exec_())
