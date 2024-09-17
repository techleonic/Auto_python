from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit,QComboBox,QFileDialog
from pathlib import Path

def open_files():
    global filenames
    filenames, _=QFileDialog.getOpenFileName(window, 'select files')
    print(filenames)
    message.setText("".join(filenames))


def destroy_file():
    for filename in filenames:
        file_path = Path(filename)
        with open(file_path, "wb") as file:
            file.write(b'')
        file_path.unlink()

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout  = QVBoxLayout()
description = QLabel('select the file you want to destroy. the files will be <font color="red"> Permanently deleted </font>')
layout.addWidget(description)

open_btn = QPushButton("open FIles")
layout.addWidget(open_btn)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("destroy files")
layout.addWidget(destroy_btn)
destroy_btn.clicked.connect(destroy_file)

message =QLabel("")
layout.addWidget(message)

window.setLayout(layout)
window.show()
app.exec()