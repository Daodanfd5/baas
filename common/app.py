import sys
import webbrowser
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


# 使用一个子线程打开浏览器
def open_baas():
    webbrowser.open_new('http://localhost:1117/')


def start():
    # 创建应用实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    window = QWidget()
    window.setWindowTitle('蔚蓝档案-BAAS')
    window.setFixedSize(660, 250)

    # 创建一个垂直布局器
    layout = QVBoxLayout()
    # 向布局中添加弹簧，以便在按钮上方添加空间
    layout.addStretch()

    lab = QLabel(
        '<html><head/><body><p align="center"><span style=" font-size:18pt; font-weight:600; font-style:italic; '
        'color:#999999;">【Baas】是一款完全免费开源的蔚蓝档案自动化脚本，如遇收费请立即退款！</span></p><p align="center"><span style=" '
        'font-size:18pt; font-weight:600; font-style:italic; color:#999999;">项目开源地址：'
        'https://github.com/baas-pro/baas</span></p><p align="center"><span style=" font-size:18pt; font-weight:600; '
        'font-style:italic; color:#999999;">QQ交流群：621628600</span></p></body></html>')
    lab.setAlignment(Qt.AlignCenter)
    lab.setTextInteractionFlags(Qt.TextSelectableByMouse)
    layout.addWidget(lab)
    btn = QPushButton('打开Baas')
    btn.clicked.connect(open_baas)
    btn.setFixedSize(200, 50)
    layout.addWidget(btn, 0, Qt.AlignCenter)

    layout.addWidget(btn)
    window.setLayout(layout)

    # 显示窗口
    window.show()
    # 运行程序
    sys.exit(app.exec())
