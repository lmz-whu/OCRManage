# OCRManage
项目需求：使用SQLite数据库管理OCR识别结果

## 文件说明
Ui_MainForm.py 是软件界面实现部分 </br>
MainForm.py 是软件的消息响应，事件处理部分 </br>
my_run.py是整个程序的入口 </br>
resource.py 是软件使用到的资源 </br>

该软件使用python3.6+PyQt4编写，实现了OCR检测结果(.txt文件)的自动导入、原始图片和检测图片的导入、以及人工识别的文字结果导入(.xlsx文件)

## 数据库结构为：
ocr_records {type, pic_name, ocr_text, consume_time, comment} 分别表示图片种类、原始名称、检测结果、耗时、结果评价</br>
original_pictures {type, pic_name, image, real_text} 分别表示种类、原始名称、图片数据、人工识别结果</br>
picture {type, pic_name, image}</br>


