## QT的UI設計-方法 :
* 下載Qt Designer
    * ![](https://hackmd.io/_uploads/rJw7UC_s3.png)
* 根據需求拉物件 : 下拉式選單(Combo Box)
    * ![](https://hackmd.io/_uploads/S1TtOROon.png)
* 修改物件顏色、自型大小等等
    * ![](https://hackmd.io/_uploads/SkyJYAdoh.png)
    * ![](https://hackmd.io/_uploads/BJMPtAdin.png)
    * ![](https://hackmd.io/_uploads/r1W8qAdjh.png)
* 儲存後會產生ui檔
    * ![](https://hackmd.io/_uploads/H1dl60di3.png)
    * ![](https://hackmd.io/_uploads/ByYo2Aush.png)
* 將ui轉成py檔 
    * 在ui檔案位置輸入cmd![](https://hackmd.io/_uploads/rysTaCdj3.png)
    * 在command輸入指令，<font color="#f00">**pyuic5 -x** *ui檔名稱* **-o** *產生py檔名稱*</font> ![](https://hackmd.io/_uploads/SJr5R0Oih.png)
## QT的UI設計-匯入icon : 
* 首先在圖片根目錄新增qrc檔 ![](https://hackmd.io/_uploads/ry_Biuk32.png)
* 拉一個Widget ![](https://hackmd.io/_uploads/HyXfDYy3n.png)
* 點選image ![](https://hackmd.io/_uploads/SkgtwF1nh.png)
* 點選qrc檔 ![](https://hackmd.io/_uploads/r1gButy32.png)
* ![](https://hackmd.io/_uploads/Skp3OK1hn.png)
* ![](https://hackmd.io/_uploads/SJRdYKk23.png)
* 最後，依序點選"ok"就完成
* 儲存後，轉成py檔後，程式碼會出現 ![](https://hackmd.io/_uploads/rJ9enFJh3.png)，需要將qrc檔轉成py檔

* 在command輸入指令，<font color="#f00"> **pyrcc5** *qrc檔案名稱* **-o** *icon_rc.py* </font>![](https://hackmd.io/_uploads/SkekAK132.png)







## VTK 3D物件 參考文章
[文章1](https://zhuanlan.zhihu.com/p/120256731)
[文章2](https://blog.csdn.net/q610098308/article/details/128777440)
[文章3](https://blog.csdn.net/weixin_43678417/article/details/121210583)

