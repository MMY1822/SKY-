from core.信号映射表 import 信号表
from 功能实现.菜单功能实现 import 菜单功能实现


def 菜单(main_window):
    # 初始化功能类
    if not hasattr(main_window, '功能实现'):
        raise ValueError("菜单功能实现未初始化")

    # 注册菜单信号映射
    信号表.register("shebei", main_window.功能实现.open_shebei)
    信号表.register("qudong1", main_window.功能实现.qudong1)
    信号表.register("qudong2", main_window.功能实现.qudong2)
    信号表.register("qudong3", main_window.功能实现.qudong3)
    信号表.register("qudong4", main_window.功能实现.qudong4)
    信号表.register("toupin1", main_window.功能实现.toupin)
    信号表.register("clear",main_window.功能实现.clear)
    信号表.register("clear_ADB", main_window.功能实现.clear_ADB)


