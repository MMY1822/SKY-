from PyQt6.uic import loadUi
import os
from .路径全局修改 import get_resource_path

class UiLoader:
    @staticmethod
    def load_ui(ui_name, parent):
        ui_path = os.path.join('ui文件', f'{ui_name}.ui')
        ui_file = get_resource_path(ui_path)

        if not os.path.exists(ui_file):
            raise FileNotFoundError(f"UI文件不存在: {ui_file}")

        loadUi(ui_file, parent)
        return parent

#这个脚本不要动他