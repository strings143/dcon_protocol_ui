from PyQt5 import QtWidgets
from UI import Ui_Form
import serial 
import threading
from PyQt5.QtCore import  QTimer ,QDateTime
import time,sys
from read_data import  machine_7071Z,machine_7051
import icon 
import serial.tools.list_ports

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


BAUD_RATES = 9600 
choices = []

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Form()
        self.ui.setupUi(self)         
        self.find_port()
        self.ui.pushButton.clicked.connect(self.Run)
    def find_port(self):
        COM_PORT = list(serial.tools.list_ports.comports())
        if(len(COM_PORT)<=0):
            choices.append('NULL')
            mbox = QtWidgets.QMessageBox(self)      
            mbox.warning(self, '尚無連接通訊埠', '請確認有無正確連接通訊埠')  
            sys.exit(app.exec_())
        else :
            for i in range(0,len(COM_PORT)) :
                choices.append(COM_PORT[i][0])
        self.ui.comportbox.addItems(choices)
    def Run(self):
        port_serial=self.ui.comportbox.currentText()
        serialport = serial.Serial(port_serial, BAUD_RATES, bytesize=8,parity='N',stopbits=1,timeout=0.1) 
        if self.check_port(serialport):
            mbox = QtWidgets.QMessageBox(self)      
            mbox.warning(self, '錯誤的通訊埠', '請選擇正確的序列埠') 
        else:
            self.refresh_data(serialport)
    def check_port(self,ser):
        ser.write(b'#01\r')
        list1 =ser.readline()                 
        ser.write(b'@02\r')
        list2 =ser.readline()
        if len(list1)==0 or len(list2)==0:
            return 1
        else:
            return 0
    def refresh_data(self,arg):
        self.timer = QTimer(self)
        self.ui.comportbox.setDisabled(True)
        self.ui.pushButton.setDisabled(True)    
        self.timer.timeout.connect(lambda:self.setup_control(arg))    
        self.timer.start(300)
    def setup_control(self,ser):     
        try:             
            ser.write(b'#01\r')
            list1 =ser.readline()                 
            ser.write(b'@02\r')
            list2 =ser.readline()
            data1=machine_7071Z(list1)
            data2=machine_7051(list2)
            refresh_ui(self,data1)
            refresh_ui2(self,data2)               
        except KeyboardInterrupt:
            ser.close() 
            self.timer.stop()   # 清除序列通訊物件
            print('再見！')

def refresh_ui2(self,data2):
        if(data2[0]=='1') :
            self.ui.widget_0.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-off-96.png);")             
        else : 
            self.ui.widget_0.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-on-96.png);")
        if(data2[1]=='1') :
            self.ui.widget_1.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-off-96.png);")             
        else : 
            self.ui.widget_1.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-on-96.png);")
        if(data2[2]=='1') :
            self.ui.widget_2.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-off-96.png);")             
        else : 
            self.ui.widget_2.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-on-96.png);")
        if(data2[3]=='1') :
            self.ui.widget_3.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-off-96.png);")             
        else : 
            self.ui.widget_3.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-on-96.png);")
        if(data2[4]=='1') :
            self.ui.widget_4.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-off-96.png);")             
        else : 
            self.ui.widget_4.setStyleSheet("border-radius: 10px;\n"
"image: url(:/unchecked-radio-button-on-96.png);")
        if(data2[5]=='1') :                  
            self.ui.widget_5.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_5.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[6]=='1') :                  
            self.ui.widget_6.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_6.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[7]=='1') :                  
            self.ui.widget_7.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_7.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[8]=='1') :                  
            self.ui.widget_8.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_8.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[9]=='1') :                  
            self.ui.widget_9.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_9.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[10]=='1') :                  
            self.ui.widget_10.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_10.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[11]=='1') :                  
            self.ui.widget_11.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_11.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[12]=='1') :                  
            self.ui.widget_12.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_12.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[13]=='1') :                  
            self.ui.widget_13.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_13.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[14]=='1') :                  
            self.ui.widget_14.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_14.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
        if(data2[15]=='1') :                  
            self.ui.widget_15.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-off-80.png);")             
        else : 
            self.ui.widget_15.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-on-80.png);")
def refresh_ui(self,data1):
        self.ui.lcdNumber_0.setDigitCount(7)
        self.ui.lcdNumber_0.display(data1[0])
        self.ui.lcdNumber_1.setDigitCount(7)
        self.ui.lcdNumber_1.display(data1[1])
        self.ui.lcdNumber_2.setDigitCount(7)
        self.ui.lcdNumber_2.display(data1[2])
        self.ui.lcdNumber_3.setDigitCount(7)
        self.ui.lcdNumber_3.display(data1[3])
        self.ui.lcdNumber_4.setDigitCount(7)
        self.ui.lcdNumber_4.display(data1[4])
        self.ui.lcdNumber_5.setDigitCount(7)
        self.ui.lcdNumber_5.display(data1[5])
        self.ui.lcdNumber_6.setDigitCount(7)
        self.ui.lcdNumber_6.display(data1[6])
        self.ui.lcdNumber_7.setDigitCount(7)
        self.ui.lcdNumber_7.display(data1[7])
        self.ui.lcdNumber_8.setDigitCount(7)
        self.ui.lcdNumber_8.display(data1[8])
        self.ui.lcdNumber_9.setDigitCount(7)
        self.ui.lcdNumber_9.display(data1[9])
        self.ui.lcdNumber_10.setDigitCount(7)
        self.ui.lcdNumber_10.display(data1[10])
        self.ui.lcdNumber_11.setDigitCount(7)
        self.ui.lcdNumber_11.display(data1[11])
        self.ui.lcdNumber_12.setDigitCount(7)
        self.ui.lcdNumber_12.display(data1[12])
        self.ui.lcdNumber_13.setDigitCount(7)
        self.ui.lcdNumber_13.display(data1[13])
        self.ui.lcdNumber_14.setDigitCount(7)
        self.ui.lcdNumber_14.display(data1[14])
        
        self.ui.widget_Dashboard_0.updateValue(float(data1[0]))
        self.ui.widget_Dashboard_1.updateValue(float(data1[1]))
        self.ui.widget_Dashboard_2.updateValue(float(data1[2]))
        self.ui.widget_Dashboard_3.updateValue(float(data1[3]))
        self.ui.widget_Dashboard_4.updateValue(float(data1[4]))
        self.ui.widget_Dashboard_5.updateValue(float(data1[5]))
        self.ui.widget_Dashboard_6.updateValue(float(data1[6]))
        self.ui.widget_Dashboard_7.updateValue(float(data1[7]))
        self.ui.widget_Dashboard_8.updateValue(float(data1[8]))
        self.ui.widget_Dashboard_9.updateValue(float(data1[9]))
        self.ui.widget_Dashboard_10.updateValue(float(data1[10]))
        self.ui.widget_Dashboard_11.updateValue(float(data1[11]))
        self.ui.widget_Dashboard_12.updateValue(float(data1[12]))

      

   
              
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       