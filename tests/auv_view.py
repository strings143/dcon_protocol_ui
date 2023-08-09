from PyQt5 import QtCore, QtGui, QtWidgets
import vtkmodules.all as vtk,time
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtCore import  QTimer ,QDateTime
import time,sys
import math
i=0
vx=[5.41,5.43,5.44,5.39,5.31,5.29,5.31,5.31,5.32,5.33,5.37,5.48,5.41,5.36,5.43,5.29,5.25,5.07,3.66,1.22,-1.01,-2.71,-3.95,-4.08,-5.64]
vy=[-5.08,-5.35,-5.66,-5.67,-5.64,-5.65,-5.67,-5.76,-5.8,-5.84,-5.96,-6.05,-6.27,-6.99,-7.68,-7.94,-8.15,-8.31,-7.52,-6.71,-5.88,-5.29,-4.97,-4.82,-4.74]
vz=[230.3,230.08,229.83,229.74,229.75,229.89,230.05,230.21,230.3,230.25,229.95,229.53,229.15,228.85,228.38,228.1,228.05,228.03,228.29,228.68,228.94,229.33,229.99,231.35,230.65]

        
class Airplane_controller(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__() 
        self.ui = Airplane_Ui_Form()
        self.ui.setupUi(self) 
        self.model = vtk.vtkPolyDataReader()
        self.model.SetFileName("AUV_3D.vtk")
        self.model.Update()
        self.init_vtk_view(self)
    def Position(self):
        global i
        self.actor.RotateX(vx[i])
        #self.actor.RotateY(vy[i])
        #self.actor.RotateZ(vz[i])
        x,y,z=self.actor.GetPosition()
        self.actor.SetPosition([x+1,y+1,z+1])
       
        self.iren.Render() #刷新畫面
        i=i+1
        print(vx[i])
        if (i==24):
            i=0
    def init_vtk_view(self,Form):
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

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.model.GetOutputPort())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetColor(1, 1, 0.6)

        #-----角度-------
        #self.transform = vtk.vtkTransform()
       
        #-----角度-------
       
       
       

        # x = self.pos().x()       # 取得新視窗目前 x 座標
        # y = self.pos().y()       # 取得新視窗目前 y 座標
        # self.move(x+250, y+80)  # 移動新視窗位置
        #self.show()
        # for i in range(1,100):
        #     x,y,z=self.actor.GetPosition()
        #     self.actor.SetPosition([x+1,y+1,z+1])
        #     self.iren.Render()
        #     time.sleep(0.1)
        self.ren.AddActor(self.actor)
        self.ren.ResetCamera()
        #self.container.setLayout(self.vl)
        #self.setCentralWidget(self.container)
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(lambda:self.Position())
        # self.timer.start(200)

        self.iren.Start()
    def closeEvent(self, QCloseEvent): #關閉視窗，沒有加無法重複關閉開啟
        #self.timer.stop()
        super().closeEvent(QCloseEvent)
        self.vtkWidget.Finalize()     

    
class Airplane_Ui_Form(object):
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
        self.progressBar.setRange(0, 1000)
        self.progressBar.setProperty("value", 500)
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
        Form.setWindowTitle(_translate("Form", "Airplane"))
        self.start.setText(_translate("Form", "start"))
        self.label.setText(_translate("Form", "Select COM to search :"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)   
    window2 = Airplane_controller()       # 連接新視窗
    window2.show()
    sys.exit(app.exec_())