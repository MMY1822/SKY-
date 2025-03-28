import sys
import os
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTextBrowser, QProgressBar, QLabel
from PyQt6.QtGui import QIcon

from 功能实现.ADB指令实现 import ADB指令实现
from .下载进度条 import DownloadManager
from .ui动态加载 import UiLoader
from .路径全局修改 import get_resource_path
from .log配置 import global_logger

# 主模块导入
from 功能实现.菜单功能实现 import 菜单功能实现
from 信号与槽连接.菜单 import 菜单
from 信号与槽连接.ADB常用指令 import ADB
from 信号与槽连接.信号总连接 import 连接所有信号


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_resources()
        self.init_ui_elements()
        self.功能实现 = 菜单功能实现(self)
        self.ADB实现 = ADB指令实现(self)

        # 然后连接信号（只调用一次）
        self.init_signal_connections()

        连接所有信号(self)


        # 测试日志
        #global_logger.append_log("<font color='green'>应用程序初始化完成</font>")

    def load_resources(self):
        UiLoader.load_ui('功能', self)
        icon_path = get_resource_path(os.path.join('png', '图标.ico'))
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    def init_ui_elements(self):
        # 设置日志控件
        log_widget = self.findChild(QTextBrowser, "log")
        global_logger.set_log_widget(log_widget)

        # 设置进度条和百分比标签
        progress_bar = self.findChild(QProgressBar, "jindutiao")
        percent_label = self.findChild(QLabel, "jindutiao2")  # 新增百分比标签

        # 配置进度条不显示内置文本
        if progress_bar:
            progress_bar.setTextVisible(False)

        # 配置百分比标签
        if percent_label:
            percent_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            percent_label.setMinimumWidth(50)  # 确保足够显示"100%"

        # 设置到下载管理器
        DownloadManager().set_ui_elements(progress_bar, percent_label)

    def init_signal_connections(self):
        菜单(self)  # 注册菜单相关信号
        ADB(self)  # 注册ADB相关信号