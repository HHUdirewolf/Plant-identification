import sys
from PyQt5.QtWidgets import(QWidget,QApplication,QGridLayout,QLabel,
                            QLineEdit,QTextEdit,QPushButton,QFrame,QFileDialog)
from PyQt5.QtGui import QPixmap
#导入baiduAPI调用模块
import Request
class AIGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #关于表格类的相关初始化代码
        #setSpacing 就是设置每个控件的外边框
        grid=QGridLayout()
        grid.setSpacing(10)

        #各个控件
        #1号控件
        explain=QLabel('请选择您要识别的图片')
        #2号 单号文本框
        self.imgUrl=QLineEdit()
        #3号，按钮
        self.select=QPushButton("选择图片")
        #为按钮添加一个事件处理函数
        self.select.clicked.connect(self.openfile)
        #4号，图片框
        self.imgLab=QLabel("图片")
        self.imgLab.setFrameShape(QFrame.Box)
        #imgLab.setFrameShadow(QFrame.Raised)
        self.imgLab.setLineWidth(1)
        
        #imgLab.setPixmap(QPixmap(""))
        #5号，多行
        self.info=QTextEdit()

        #将控件进行合理布局
        grid.addWidget(explain,1,0)
        grid.addWidget(self.imgUrl,1,1)
        grid.addWidget(self.select,1,2)
        grid.addWidget(self.imgLab,2,0,5,3)
        grid.addWidget(self.info,1,3,6,1)

        #窗口最后的设置
        self.setLayout(grid)
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle("AIGUI")
        self.show()
    def openfile(self):
        #打开图片弹窗，选择图片
        self.select_path=QFileDialog.getOpenFileName(self,"选择要识别的图片","/","Imgae Files(*.jpg *.png)")
        #如果没选择图片，空过
        if not self.select_path[0].strip():
            pass
        else:
            #选择图片后执行下面的内容
            # 设置图片的路径
            self.imgUrl.setText(self.select_path[0])
            #在图片标签框中显示图片
            #1)根据路径pixmap解析图片
            pixmap=QPixmap(self.select_path[0])
            #2)缩放图片
            scalePixmap=pixmap.scaledToWidth(300)
            #scaledPixmap=pixmap.scaled(QSize(311,301))
            #3)显示
            self.imgLab.setPixmap(scalePixmap)
            result=self.identify()
            self.info.setText(result)
    #借助百度AI平台完成植物识别工作      
    def identify(self):
        result=Request.BaiduAPI(self.select_path[0])
        return result
            

def main():
    app=QApplication(sys.argv)
    ai=AIGUI()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()



    
        
        
