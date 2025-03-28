from PyQt6.QtCore import QObject
from core.log配置 import global_logger

class ScreenCleaner(QObject):
    def execute(self):
        try:
            global_logger.clear_log()
            global_logger.append_log("<font color='gray'>[系统] 日志已清空，按Ctrl+L可快捷清屏</font>")
            return True
        except Exception as e:
            global_logger.append_log(f"<font color='red'>清屏失败: {str(e)}</font>")
            return False