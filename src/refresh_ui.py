#icon 更新
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
        #三段式開關        
        if(data2[5]=='1' or data2[6]=='1') :                  
            self.ui.widget_5.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-two.png);")             
        if(data2[5]=='0') :
            self.ui.widget_5.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-three.png);")
        if(data2[6]=='0') :                          
            self.ui.widget_5.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-one.png);")
        #----------
        if(data2[7]=='1' or data2[8]=='1') :                  
            self.ui.widget_7.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-two.png);")             
        if(data2[7]=='0') :
            self.ui.widget_7.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-one.png);")
        if(data2[8]=='0') :                  
            self.ui.widget_7.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-three.png);")
        #----------
        if(data2[9]=='1' or data2[10]=='1') :                  
            self.ui.widget_9.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-two.png);")             
        if(data2[9]=='0') : 
            self.ui.widget_9.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-one.png);")
        if(data2[10]=='0') :                  
           self.ui.widget_9.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-three.png);")
        #----------
        if(data2[11]=='1' or data2[12]=='1') :                  
            self.ui.widget_11.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-two.png);")             
        if(data2[11]=='0') :
            self.ui.widget_11.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-one.png);")
        if(data2[12]=='0') :                  
           self.ui.widget_11.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-three.png);")
         #----------
        if(data2[13]=='1' or data2[14]=='1') :                  
            self.ui.widget_13.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-two.png);")             
        if(data2[13]=='0') :
            self.ui.widget_13.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-three.png);")
        if(data2[14]=='0') :                  
            self.ui.widget_13.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-one.png);")
         #----------
        if(data2[15]=='1') :                  
            self.ui.widget_15.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-three.png);")             
        else : 
            self.ui.widget_15.setStyleSheet("border-radius: 10px;\n"
"image: url(:/toggle-one.png);")
#icon 更新
def refresh_ui1(self,data1):
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

      

   
              
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       