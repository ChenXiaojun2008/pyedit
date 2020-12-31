# -*- coding:UTF-8  -*-
from PyQt5 import QtWidgets

import sys
import Libs.pyeditor
import Libs.editorMain

app = QtWidgets.QApplication(sys.argv)
editorMain = QtWidgets.QMainWindow()

editorMain_ui = Libs.editorMain.Ui_MainWindow()

editorMain_ui.setupUi(editorMain)

def main():
    editorMain.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()