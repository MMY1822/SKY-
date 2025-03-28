from core.信号映射表 import 信号表
from 功能实现.ADB指令实现 import ADB指令实现

def ADB(main_window):
    # 使用单独的ADB功能实现属性
    if not hasattr(main_window, 'adb_功能实现'):
        main_window.adb_功能实现 = ADB指令实现(main_window)

    信号表.register("ADB_RB", main_window.adb_功能实现.ADB_RB)
