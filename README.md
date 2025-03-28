这里是你给出的项目文档，已经根据需求进行了排版和格式上的改进：

---

# Sky框架项目文档

## 📂 项目结构
```
Skybox/
├── 开.py               # 程序主入口
├── core/               # 核心底层代码
│   ├── 程序加载.py      #所有信号与资源都要在这里加载 
│   ├── ui动态加载.py    # UI文件加载的位置，没事不要动
│   ├── 信号映射表.py     # 信号管理系统
│   ├── 下载进度条.py     # 一个已经写好了的下载URL的进度条
│   ├── 清屏.py          # 清理屏幕日志
│   └── log配置.py       # 屏幕日志的配置，可直接使用
├── png/                # 图片资源
│   ├── 图标.ico        # 应用图标
│   └── ...             # 其他图片资源
├── ui文件/             # Qt Designer 文件
│   ├── 功能.ui       # 主窗口 UI
│   └── ...             # 其他 UI 文件
├── 信号与槽连接/        # 信号管理
│   ├── 菜单.py         # 菜单信号
│   └── ADB 常用指令.py  # ADB 信号
├── 功能实现/            # 业务逻辑
│   ├── 菜单功能实现.py   # 菜单功能
│   └── ADB 指令实现.py   # ADB 功能
└── 开发文档.md           # 项目文档
```

## 🚀 快速开始

### 运行程序
```bash
python 开.py
```

### 开发环境
- Python 3.11+
- PyQt6
## 🧩 模块说明

### 1. 程序入口 (`开.py`)
```python
import sys
import os
from core.程序加载 import MainWindow
from PyQt6.QtWidgets import QApplication
import traceback


def main():
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        app = QApplication(sys.argv)
        app.setApplicationName("SkyBox")
        app.setApplicationVersion("1.0.0")
        window = MainWindow()
        window.setWindowTitle("SkyBox")
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(f"应用程序崩溃: {e}")
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### 2. 核心模块 (`core/`)
| 文件               | 功能                 |
|--------------------|----------------------|
| `程序加载.py`        | 主窗口初始化逻辑     |
| `ui动态加载.py`      | UI文件动态加载器     |
| `信号映射表.py`      | 全局信号槽管理系统   |
| `log配置.py`        | 日志系统配置         |
| `下载进度条.py`      | 下载管理功能         |

### 3. 资源目录
- `png/` - 存放所有图片资源
  - `图标.ico` - 应用图标
  - 各类按钮/背景图片
- `ui文件/` - Qt Designer生成的界面文件
  - `主界面.ui` - 主窗口 UI
  - 对话框 `*.ui`

### 4. 信号连接 (`信号与槽连接/`)
```python
# 示例：菜单.py
from core.信号映射表 import 信号表

def 菜单(main_window):
    信号表.register("shebei", main_window.功能实现.open_shebei)
    # 其他信号注册...
```

### 5. 功能实现 (`功能实现/`)
```python
# 示例：菜单功能实现.py
from core.log配置 import global_logger
import subprocess
import traceback
class 菜单功能实现:
    def open_shebei(self):
        global_logger.append_log("<font color='blue'>正在打开设备管理器...</font>")
        try:
            # 使用shell=False更安全
            subprocess.Popen('devmgmt.msc', shell=True)
            global_logger.append_log("<font color='green'>✓ 设备管理器已打开</font>")
        except Exception as e:
            global_logger.append_log(f"<font color='red'>✗ 打开失败: {str(e)}</font>")
            traceback.print_exc()
```

## 🔧 二次开发指南

### 修改UI界面
1. 使用Qt Designer编辑`.ui`文件
2. 替换`ui文件/`目录中的对应文件
3. 修改信号与槽的连接部分

### 添加新功能
1. 在`信号与槽连接/`中注册信号
2. 在`功能实现/`实现功能
3. 在UI中添加对应元素

### ADB模块开发状态
```python
# ADB指令实现.py (开发中)
class ADB指令实现:
    def ADB_RB(self):
        """待实现的ADB重启功能"""
        pass
```

## ⚠️ 注意事项

1. 所有资源引用请使用：  
   ```python 
   from core.路径全局修改 import get_resource_path
   ```

2. 日志输出请使用：  
 ```python
from core.log配置 import global_logger
global_logger.append_log("日志内容")
```

3. 信号连接必须通过信号映射表统一管理

## 📜 版本历史
| 版本 | 更新说明             |
|------|----------------------|
| v1.0 | 初始版本             |

---

> 📌 提示：本项目采用模块化设计，便于共同维护和更新。

> QQ一群：702829749

> QQ二群：837987389

> 开发者QQ:1822481266 邮箱：1822481266@qq.com

---
