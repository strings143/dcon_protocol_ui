import time,sys,serial,serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  QTimer ,QDateTime
from PyQt5.QtWidgets import QMessageBox,QListView
import vtkmodules.all as vtk,time
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
        
class  MouseInteractorHighLightActor(vtk.vtkInteractorStyleTrackballCamera): # 禁止3D vtk與滑鼠交互事件
    def __init__(self, parent = None):
               
        self.AddObserver("MouseMoveEvent", self.MouseMoveEvent)
       
        self.AddObserver("MouseWheelForwardEvent", self.MouseWheelForwardEvent)
      
        self.AddObserver("MouseWheelBackwardEvent", self.MouseWheelBackwardEvent)

    def MouseMoveEvent(self, obj, event):
        pass

    def MouseWheelBackwardEvent(self, obj, event):
        pass

    def MouseWheelForwardEvent(self, obj, event):
        pass


class RemoteOperatedVehicle_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = RemoteOperatedVehicle_Ui_Form()
        self.ui.setupUi(self) 

        self.chioces=[]
        self.find_port() 

        self.ui.start.clicked.connect(self.Run)#start按鈕，執行Run(self) function 

        self.model = vtk.vtkPolyDataReader()
        self.model.SetFileName("ROV_3D.vtk")
        self.model.Update()

        self.First_Run=True
        self.init_vtk_view(self)
    def find_port(self):
        COM_PORT = list(serial.tools.list_ports.comports())
        if(len(COM_PORT)<=0):
            self.chioces.append('NULL')           
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("發生錯誤")
            msg.setText("請確認有無正確連接序列埠")
            msg.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
            msg.exec_()  
            sys.exit(app.exec_())
        else :
            for i in range(0,len(COM_PORT)) :
                self.chioces.append(COM_PORT[i][0])
        self.ui.comboBox_port.addItems(self.chioces)
    def Run(self):
        self.port_serial=self.ui.comboBox_port.currentText()
        serialport = serial.Serial(self.port_serial, 115200, bytesize=8,parity='N',stopbits=1,timeout=0.1) 
        if self.check_port(serialport):
            msg = QMessageBox(self)
            msg.setWindowTitle("錯誤的通訊埠")
            msg.setText("請選擇正確的序列埠，或再試一次")
            msg.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
            msg.exec_()   
        else:
            self.refresh_data(serialport)
            
    def refresh_data(self,arg):
        self.ui.start.setDisabled(True)
        self.threadtime(arg)
    def threadtime(self,arg):
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:self.Update_3Dvtk(arg))
        self.timer.start(10)
    def check_port(self,ser):
        list =ser.readline(7)
        ser.close()
        if list==b'$Sensor': 
            return 0
        else:
            return 1
    def init_vtk_view(self,Form):
        #--------------------------------------------------------------------
        #-------------------------------初始化-------------------------------
        #--------------------------------------------------------------------

        #self.container = QtWidgets.QWidget(self.ui.VTKwidget)
        self.vl = QtWidgets.QVBoxLayout(self.ui.VTKwidget)
        self.vtkWidget = QVTKRenderWindowInteractor(self.ui.VTKwidget)
        self.vl.addWidget(self.vtkWidget)
        
        self.render_window  = self.vtkWidget.GetRenderWindow()
        self.ren= vtk.vtkRenderer()
        self.ren.SetBackground(0.1, 0.3, 0.5)
        #self.render_window.SetSize(800, 800)
        self.render_window.AddRenderer(self.ren)
        
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # add the custom style
        style = MouseInteractorHighLightActor()
        style.SetDefaultRenderer(self.ren)
        self.iren.SetInteractorStyle(style)

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.model.GetOutputPort())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetColor(1, 1, 0.6)

        self.ren.AddActor(self.actor)
        self.ren.ResetCamera()
        #--------------------------------------------------------------------
        #---------------------------調整初始角度------------------------------
        #--------------------------------------------------------------------

        #self.actor.RotateX()
        self.actor.RotateY(-90)
        #self.actor.RotateZ()

        self.iren.Render() 
        self.iren.Start()
        
    def Update_3Dvtk(self,serialport):
        #----------------------------------------------------------------
        #----------使用try except，當出現未知錯誤時報告錯誤資訊-----------
        #----------------------------------------------------------------
        try:
            #----------------------------------------------------------------
            #------------------------讀值與資料初步處理-----------------------
            #----------------------------------------------------------------
            global x,y,z
            serialport = serial.Serial(self.port_serial, 115200, bytesize=8,parity='N',stopbits=1,timeout=0.1) 
            data=serialport.readline()#讀
            data_str = data.decode() #byte資料格式轉為str
            parts = data_str.split(',') #切割

            #---------------------------------------------------------------
            #-------------資料轉換為可用數值，並且依照角度差旋轉模型---------
            #---------------------------待補try catch----------------------------------
            if(len(data)==51): #因資料有時候會缺失，導致錯誤，因此收到完整資料(51)才能進行作業
                # #sensor_id = parts[0]  # "Sensor"
                value1 = float(parts[1])*10  # - 深度  # *10為Demo方便觀測progressBar物件
                value2 = float(parts[2])  #  - y軸
                value3 = float(parts[3])  #  - x軸
                value4 = float(parts[4])  #  - z軸
                # #value5 = float(parts[5])  # -00.1
                # #checksum = parts[6]  # "*09"
                self.ui.progressBar.setValue(value1)
                self.ui.lcdNumber.setDigitCount(7)
                self.ui.lcdNumber.display(value1)
                
                if(self.First_Run):
                    self.First_Run=False #只執行第一次
                    
                    # 輸出初始角度
                    # print("X軸旋轉:",value3)
                    # print("Y軸旋轉:",value2)
                    # print("Z軸旋轉:",value4)

                    #Demo時初始角度為(-4,316,2)，初始角度減去value即可校正模型角度
                    self.actor.RotateX(-4-value3)
                    self.actor.RotateY(316-value2)
                    self.actor.RotateZ(2-value4)
                    self.iren.Render()
                else:
                    self.actor.RotateX(x-value3)
                    self.actor.RotateY(y-value2)
                    self.actor.RotateZ(z-value4)
                    self.iren.Render()

                serialport.close()
                y=value2
                x=value3
                z=value4
        except Exception as e:
            print("發生錯誤:", e)
    def closeEvent(self, QCloseEvent): #關閉視窗，沒有加無法重複關閉開啟
        super().closeEvent(QCloseEvent)
        self.vtkWidget.Finalize()     
    
class RemoteOperatedVehicle_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 730)
#       Form.setStyleSheet("background-color: rgb(0, 0, 0);\n"
# "")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(530, 20, 81, 31))
        self.start.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                "background-color: rgb(206, 221, 255);\n"
                                "")
        self.start.setObjectName("start")
        self.comboBox_port = QtWidgets.QComboBox(Form)
        self.comboBox_port.setView(QListView())
        self.comboBox_port.setGeometry(QtCore.QRect(350, 20, 161, 31))
        self.comboBox_port.setObjectName("comboBox_port")
        self.comboBox_port.setStyleSheet('''
                        QComboBox{
                                background-color:#5B5B5B; 
                                selection-background-color:#9780AC;
                                color:#ACF6E1
                        }   
                        QListView{
                                background:#5B5B5B;
                                font-size: 10pt;
                                font-weight: bold;
                                padding-left:3px;
                                padding-right:3px;
                                padding-bottom:2px;
                                padding-top:2px;
                        }  
                        QListView::item{
                                background:#5B5B5B;
                                color:#ACF6E1;
                        }
                        QListView::item:selected{
                                background-color:#9780AC;
                        }            
                '''
                )
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 41))
        self.label.setStyleSheet("color: rgb(27, 130, 141);\n"
                                "font: 50 20pt \"Berlin Sans FB Demi\";\n"
                                "")
        self.label.setObjectName("label")
        self.VTKwidget = QtWidgets.QWidget(Form)
        self.VTKwidget.setGeometry(QtCore.QRect(10, 70, 701, 641))
        self.VTKwidget.setStyleSheet("")
        self.VTKwidget.setObjectName("VTKwidget")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(760, 130, 91, 571))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        #測試用為0~10方便觀測，實際應改為0~1000
        self.progressBar.setRange(0, 10)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setStyleSheet('''
                                    QProgressBar {
                                        border: 2px solid #000;
                                        border-radius: 5px;
                                        text-align:center;
                                    }
                                    QProgressBar::chunk {
                                        background: #66B3FF;
                                        height: 1px;
                                        width:1px;
                                    }
                                ''')
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(750, 80, 111, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(154, 131, 158);\n"
                                    "color: rgb(255, 255, 127);")
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RemoteOperatedVehicle"))
        self.start.setText(_translate("Form", "start"))
        self.label.setText(_translate("Form", "Select COM to search :"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)   
    window2 = RemoteOperatedVehicle_controller()       # 連接新視窗
    window2.show()
    sys.exit(app.exec_())
    
    #---------------------------------------------------------------
    #------保留vtk模型移動程式碼，當需要移動模型時可Google試試---------
    #---------------------------------------------------------------
    #     self.transform = vtk.vtkTransform() #忘了
    #     x,y,z=self.actor.GetPosition() #返回座標
    #     self.actor.SetPosition([x+1,y+1,z+1]) #設定座標
