# OCRManage
项目需求：使用SQLite数据库管理OCR识别结果

Ui_MainForm.py 是软件界面实现部分
MainForm.py 是软件的消息响应，事件处理部分
my_run.py是整个程序的入口
resource.py 是软件使用到的资源

该软件使用python3.6+PyQt4编写，实现了OCR检测结果(.txt文件)的自动导入、原始图片和检测图片的导入、以及人工识别的文字结果导入(.xlsx文件)
数据库结构为：

