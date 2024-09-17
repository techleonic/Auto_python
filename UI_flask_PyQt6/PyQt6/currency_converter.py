from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit,QComboBox
from bs4 import BeautifulSoup
import requests
def get_currency(in_currency, out_curency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_curency}&amount=1"
    content= requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").getText()
    rate = rate.split(" ")[0].replace(",","")
    print(rate)
    f_rate = round( float(rate), 2)
    print("covertir a float")
    return (f_rate)

def show_currency():
    input_text = float(text.text())
    in_cur =in_combo.currentText()
    out_cur = target_combo.currentText()
    rate =  get_currency(in_cur,out_cur)
    print(rate)
    result =  round( input_text * rate, 2)
    output_label.setText(str(result))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Sentence Maker")

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel("")
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

in_combo =  QComboBox()
currencies = ["USD", "EUR", "INR", "AUD", "CAD", "SGD", "ARS", "COP", "MXN", "VEF"]
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo =  QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

text = QLineEdit()
layout3.addWidget(text)

btn = QPushButton("Convert")
layout3.addWidget(btn)



btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()