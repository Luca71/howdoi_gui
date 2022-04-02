import sys
from tkinter import TOP, Toplevel
from tkinter.font import BOLD
import qdarkstyle
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget)
from PySide2.QtCore import QMargins, Qt
from PySide2.QtGui import QFont
from howdoi import howdoi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        Font = QFont('Segoe UI Variable', 12, QFont.Bold)

        self.setWindowTitle("Howdoi GUI")
        self.setFont(Font)

        self.label = QLabel()
        self.label.setStyleSheet("border: 1px solid #1A72BB")
        self.label.setAlignment(Qt.AlignTop)

        self.input = QLineEdit()

        AskButton = QPushButton("Ask")
        AskButton.setFont(Font)
        AskButton.clicked.connect(self.GetAnswer)

        self.QuestioLabel = QLabel()
        self.QuestioLabel.setFont(Font)
        self.QuestioLabel.setText("How do I:")

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.QuestioLabel)
        HLayout.addWidget(self.input)

        VLayout = QVBoxLayout()
        VLayout.addLayout(HLayout)
        VLayout.addWidget(self.label)
        VLayout.addWidget(AskButton)

        Container = QWidget()
        Container.setMinimumSize(500, 500)
        Container.setLayout(VLayout)
        self.setCentralWidget(Container)
        self.setContentsMargins(QMargins(5, 5, 5, 5)) # set margin for main window content

    def GetAnswer(self):
        QueryText = self.input.text()
        if QueryText != "":
            self.label.setText(howdoi.howdoi(QueryText))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2()) # usign dark mode stylesheet

    window = MainWindow()
    window.show()

    app.exec_()