from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

import sys

class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionIncrease_Font_Size.triggered.connect(self.incFontSize)
        self.actionDecrease_Font_Size.triggered.connect(self.decFontSize)


    def newFile(self):
        print("new file")
    
    def saveFile(self):
        ""

    def saveFileAs(self):
        ""
    
    def openFile(self):
        ""
    
    def undo(self):
        ""

    def redo(self):
        ""
    
    def cut(self):
        ""
    
    def copy(self):
        ""
    
    def paste(self):
        ""
    
    def setDarkMode(self):
        ""

    def setLightMode(self):
        ""
    
    def incFontSize(self):
        ""
    
    def decFontSize(self):
        ""


    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()