# 项目结构说明文档

## 目录结构
项目根目录/
│
├── 开.py # 程序主入口
├── core/ # 核心底层代码
├── png/ # 图片资源
├── ui文件/ # Qt Designer生成的.ui文件
├── 信号与槽连接/ # 信号与槽连接管理
├── 功能实现/ # 具体功能实现代码
└── README.md # 项目说明文档

复制

## 各目录详细说明

### 1. 开.py (程序主入口)

```python
"""
程序启动入口文件
职责：
1. 初始化QApplication
2. 创建并显示主窗口
3. 启动事件循环
"""
import sys
from PyQt6.QtWidgets import QApplication
from core.程序加载 import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
2. core/ (核心模块)
复制
core/
├── 信号映射表.py          # 全局信号-槽映射系统
├── 程序加载.py            # 主窗口加载逻辑
├── ui动态加载.py          # UI文件加载器
├── log配置.py            # 日志系统配置
├── 下载进度条.py          # 下载管理模块
├── 清屏.py              # 终端清屏功能
└── 路径全局修改.py        # 资源路径管理
3. png/ (图片资源)
复制
存放所有图片资源文件，如：
- 图标.ico
- 背景.png
- 按钮图标/
4. ui文件/ (界面设计文件)
复制
存放Qt Designer生成的.ui文件
修改说明：
1. 直接替换对应.ui文件即可更新界面
2. 命名规范：
   - 主窗口：main_window.ui
   - 对话框：dialog_*.ui
5. 信号与槽连接/ (信号连接管理)
复制
信号与槽连接/
├── 菜单.py              # 菜单栏信号连接
├── ADB常用指令.py        # ADB功能信号连接
└── 信号连接.py           # 集中式信号连接器

设计规范：
1. 每个文件只负责特定模块的信号注册
2. 不包含具体功能实现
3. 命名规范：信号名_模块.py
6. 功能实现/ (业务逻辑)
复制
功能实现/
├── 菜单功能实现.py        # 菜单功能实现
└── ADB指令实现.py        # ADB功能实现(Py版开发中)

开发规范：
1. 每个文件对应一个功能模块
2. 类名与文件名一致
3. 只关注业务逻辑，不处理信号连接
二次开发指南
界面修改流程
使用Qt Designer修改/创建.ui文件

将.ui文件放入ui文件/目录

如需新增信号：

在信号与槽连接/中添加对应连接

在功能实现/中添加具体实现

ADB模块开发说明
python
复制
# ADB指令实现.py 开发模板
class ADB指令实现:
    """Py版ADB功能实现(开发中)"""
    
    def __init__(self, main_window):
        self.main_window = main_window
    
    def ADB_RB(self):
        """ADB重启设备"""
        # 待实现逻辑
        pass
    
    # 添加其他ADB指令方法...
注意事项
资源引用统一使用路径全局修改.get_resource_path()

日志输出使用global_logger.append_log()

信号连接必须通过信号映射表统一管理

UI更新后需要重新运行开.py生效

版本记录
v1.0 初始版本

v1.1 新增ADB模块框架

v1.2 优化信号连接系统

复制
合并成一个md文件，我需要上传到仓库使用
markdown
复制
# Skybox 工具箱项目文档

## 📂 项目结构
Skybox/
├── 开.py # 程序主入口
├── core/ # 核心底层代码
├── png/ # 图片资源目录
├── ui文件/ # Qt Designer界面文件
├── 信号与槽连接/ # 信号与槽连接管理
├── 功能实现/ # 具体功能实现
└── README.md # 本说明文档

复制

## 🚀 快速开始

### 运行程序
```bash
python 开.py
开发环境
Python 3.11+

PyQt6

其他依赖见 requirements.txt

🧩 模块说明
1. 程序入口 (开.py)
python
复制
import sys
from PyQt6.QtWidgets import QApplication
from core.程序加载 import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
2. 核心模块 (core/)
文件	功能
程序加载.py	主窗口初始化逻辑
ui动态加载.py	UI文件动态加载器
信号映射表.py	全局信号槽管理系统
log配置.py	日志系统配置
下载进度条.py	下载管理功能
3. 资源目录
png/ - 存放所有图片资源

图标.ico

各类按钮/背景图片

ui文件/ - Qt Designer生成的界面文件

主界面.ui

对话框*.ui

4. 信号连接 (信号与槽连接/)
python
复制
# 示例：菜单.py
from core.信号映射表 import 信号表

def 菜单(main_window):
    信号表.register("shebei", main_window.功能实现.open_shebei)
    # 其他信号注册...
5. 功能实现 (功能实现/)
python
复制
# 示例：菜单功能实现.py
class 菜单功能实现:
    def open_shebei(self):
        """打开设备管理器"""
        # 具体实现代码
🔧 二次开发指南
修改UI界面
使用Qt Designer编辑.ui文件

替换ui文件/目录中的对应文件

无需修改代码即可生效

添加新功能
在功能实现/中添加实现类

在信号与槽连接/中注册信号

在UI中添加对应元素

ADB模块开发状态
python
复制
# ADB指令实现.py (开发中)
class ADB指令实现:
    def ADB_RB(self):
        """待实现的ADB重启功能"""
        pass
⚠️ 注意事项
所有资源引用请使用：

python
复制
from core.路径全局修改 import get_resource_path
日志输出请使用：

python
复制
from core.log配置 import global_logger
global_logger.append_log("日志内容")
信号连接必须通过信号映射表统一管理

📜 版本历史
版本	更新说明
v1.0	初始版本
v1.1	优化信号系统
v1.2	新增ADB模块框架
📌 提示：本项目采用模块化设计，各组件解耦，便于单独维护和更新。
