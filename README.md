# 水下載具人機介面
本專案使用現有自組遙控載具(Remote operated vehicle, ROV)開發操作搖桿模組，包含搖桿操作資料讀取、人機介面(User interface, UI)及水下載具3D模型的模擬。採用Python程式開發設計具有高可靠度的ROV操作搖桿模組及其UI，並使用方位感測器，模擬3D模型水下載具。
### 搖桿模組
將控制板上資料透過M-7051與M-7017Z傳送，透過DCON通訊協定進行資料傳送，資料到手後會有四組16進制格式的資料，需要將其轉為2進制格式即可判斷1/0來更改圖形介面。例如:7fff轉為二進制為0111 1111 1111 1111我們就可以知道Address[0]是關閉的。
![image](https://github.com/strings143/dcon_protocol_ui/assets/73727207/08779024-2dc1-4a1a-a5e5-e94ecb139e9b)
![image](https://github.com/strings143/dcon_protocol_ui/assets/73727207/d42c101b-77f4-4cfe-a9ea-999138bffe39)
### 方位感測器
感測器偵測自組遙控載具當前X,Y,Z軸，讀取到後即可已將資料串接給3D模型，就可以達到使用3D模型即時模擬自組遙控載具現在之方位
![image](https://github.com/strings143/dcon_protocol_ui/assets/73727207/562df74b-cade-4533-81e6-6154ee1996d8)
# 預覽畫面
### 操作搖桿模組介面
![image](https://github.com/strings143/dcon_protocol_ui/assets/73727207/9f1a73d1-9d07-4323-803e-51a494eebad1)
### 方位感測器介面
![image](https://github.com/user-attachments/assets/725af8a6-c8df-4388-b0f9-1546549c44c4)
# 建置
* download repository 
* open dist file
* Run start.exe
# 套件
* Python 3.9.13
* PyQt5 5.15.4
* PyQt5-tools 5.15.4.3.2 
* vtk 9.2.6
# 參考
參考了作者的儀錶板設計。
> https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main
