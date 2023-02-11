from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

a = 0
def show():
    global a
    a = a + 1
    label.setText(str(a))       # 更新 QLabel 內容

label = QtWidgets.QLabel(Form)
label.setText('0')
label.setStyleSheet('font-size:20px;')
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText('增加數字')
btn.setGeometry(50,60,100,30)
btn.clicked.connect(show)       # 點擊時執行 show 函式

Form.show()
sys.exit(app.exec_())