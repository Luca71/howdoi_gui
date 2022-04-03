from msilib.schema import Font
import sys
from tkinter import TOP, Toplevel
from tkinter.font import BOLD
import qdarkstyle
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QTextBrowser, QTextEdit)
from PySide2.QtCore import QMargins, Qt
from PySide2.QtGui import QFont
from howdoi import howdoi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        Font = QFont('Segoe UI Variable', 12, QFont.Bold)
        FontSmall = QFont('Segoe UI Variable', 10, QFont.Bold)

        self.setWindowTitle("Howdoi GUI")
        self.setFont(Font)

        self.input = QLineEdit()
        self.input.setFont(Font)

        self.QuestioLabel = QLabel()
        self.QuestioLabel.setFont(Font)
        self.QuestioLabel.setText("How do I:")

        self.TextEdit = QTextEdit()
        self.TextEdit.setFont(Font)
        self.TextEdit.setStyleSheet("border: 1px solid #1A72BB")
        self.TextEdit.setAlignment(Qt.AlignTop)

        AskButton = QPushButton("Ask")
        AskButton.setFont(Font)
        AskButton.clicked.connect(self.GetAnswer)

        JsonButton = QPushButton("Show raw json format")
        JsonButton.setFont(FontSmall)
        JsonButton.clicked.connect(self.JsonAnswer)

        LinkButton = QPushButton("Show the answer link")
        LinkButton.setFont(FontSmall)
        LinkButton.clicked.connect(self.ShowLink)

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.QuestioLabel)
        HLayout.addWidget(self.input)

        VLayout = QVBoxLayout()
        VLayout.addLayout(HLayout)
        VLayout.addWidget(AskButton)
        VLayout.addWidget(JsonButton)
        VLayout.addWidget(self.TextEdit)
        VLayout.addWidget(LinkButton)

        Container = QWidget()
        Container.setMinimumSize(500, 500)
        Container.setLayout(VLayout)
        self.setCentralWidget(Container)
        self.setContentsMargins(QMargins(5, 5, 5, 5)) # set margin for main window content

    def GetAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText))
    
    def JsonAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + " -j"))
    
    def ShowLink(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.TextEdit.setText(howdoi.howdoi(QueryText + " -l"))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2()) # usign dark mode stylesheet

    window = MainWindow()
    window.show()

    app.exec_()