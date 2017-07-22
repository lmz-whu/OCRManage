# encoding:utf-8

import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore

from MainForm import MainWindow

app = QtGui.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
