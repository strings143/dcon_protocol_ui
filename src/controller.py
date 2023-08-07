from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UI import Ui_Form
import serial 
from PyQt5.QtCore import  QTimer 
from read_data import  machine_7071Z,machine_7051
from refresh_ui import refresh_ui1,refresh_ui2
import serial.tools.list_ports
import sys
import subprocess

BAUD_RATES = 9600 
choices = []


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Form()
        self.ui.setupUi(self) 
        self.find_port() #檢查有無插上usb，如果沒有會跳出視窗提示
        self.ui.pushButton.clicked.connect(self.Run)#start按鈕，執行Run(self) function 
        self.ui.pushButton_view2.clicked.connect(self.Show_Airplane_Window)
    def Show_Airplane_Window(self):
        subprocess.Popen('Rov.exe')
    def closeEvent(self,event):
        sys.exit()

    def find_port(self):
        COM_PORT = list(serial.tools.list_ports.comports())
        if(len(COM_PORT)<=0):
            choices.append('NULL')           
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("發生錯誤")
            msg.setText("請確認有無正確連接序列埠")
            msg.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
            msg.exec_()  
            sys.exit(app.exec_())
        else :
            for i in range(0,len(COM_PORT)) :
                choices.append(COM_PORT[i][0])
        self.ui.comportbox.addItems(choices)
    def Run(self):
        port_serial=self.ui.comportbox.currentText()
        serialport = serial.Serial(port_serial, BAUD_RATES, bytesize=8,parity='N',stopbits=1,timeout=0.1) 
        if self.check_port(serialport):
            msg = QMessageBox(self)
            msg.setWindowTitle("錯誤的通訊埠")
            msg.setText("請選擇正確的序列埠")
            msg.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
            msg.exec_()   
        else:
            self.refresh_data(serialport)
    #檢查是否連接正確的comport
    def check_port(self,ser):
        ser.write(b'$01M\r') #回傳資料b'!017017Z\r'，b''表示byte data，!01位址，7017Z型號
        list1 =ser.readline(9)
        ser.write(b'$02M\r')#回傳資料b'!027051\r'，b''表示byte data，!02位址，7051型號
        list2 =ser.readline(8)
        if list1==b'!017017Z\r' and list2==b'!027051\r': 
            return 0
        else:
            return 1
    #資料更新，每0.2秒(200毫秒)更新一次資料
    def refresh_data(self,arg):
        self.ui.comportbox.setDisabled(True)
        self.ui.pushButton.setDisabled(True) 
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:self.setup_control(arg))
        self.timer.start(50)
    #下指令，讀取read_data.py檔，切割完後的資料
    def setup_control(self,ser):
        try:             
            ser.write(b'#01\r')
            list1 =ser.readline()                 
            ser.write(b'@02\r')
            list2 =ser.readline()
            data1=machine_7071Z(list1)
            data2=machine_7051(list2)
            refresh_ui1(self,data1)
            refresh_ui2(self,data2) 
                    
        except Exception as e:
            ser.close() 
            self.timer.stop()   # 清除序列通訊物件
            print('錯誤:',e)
