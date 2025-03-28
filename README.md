```markdown
# Skybox 工具箱项目文档

## 📂 项目结构

```
Skybox/
├── 开.py                 # 程序主入口
├── core/                # 核心底层代码
├── png/                 # 图片资源目录
├── ui文件/               # Qt Designer界面文件
├── 信号与槽连接/          # 信号与槽连接管理
├── 功能实现/             # 具体功能实现
└── README.md            # 本说明文档
```

## 🚀 快速开始

### 运行程序
```bash
python 开.py
```

### 开发环境
- Python 3.11+
- PyQt6
- 其他依赖见 `requirements.txt`

## 🧩 模块说明

### 1. 程序入口 (`开.py`)
```python
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
```

### 2. 核心模块 (`core/`)
| 文件 | 功能 |
|------|------|
| `程序加载.py` | 主窗口初始化逻辑 |
| `ui动态加载.py` | UI文件动态加载器 |
| `信号映射表.py` | 全局信号槽管理系统 |
| `log配置.py` | 日志系统配置 |
| `下载进度条.py` | 下载管理功能 |

### 3. 资源目录
- `png/` - 存放所有图片资源
  - 图标.ico
  - 各类按钮/背景图片
- `ui文件/` - Qt Designer生成的界面文件
  - 主界面.ui
  - 对话框*.ui

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
class 菜单功能实现:
    def open_shebei(self):
        """打开设备管理器"""
        # 具体实现代码
```

## 🔧 二次开发指南

### 修改UI界面
1. 使用Qt Designer编辑`.ui`文件
2. 替换`ui文件/`目录中的对应文件
3. 无需修改代码即可生效

### 添加新功能
1. 在`功能实现/`中添加实现类
2. 在`信号与槽连接/`中注册信号
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
| 版本 | 更新说明 |
|------|----------|
| v1.0 | 初始版本 |
| v1.1 | 优化信号系统 |
| v1.2 | 新增ADB模块框架 |

---

> 📌 提示：本项目采用模块化设计，各组件解耦，便于单独维护和更新。
