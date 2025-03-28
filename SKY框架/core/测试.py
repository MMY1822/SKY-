import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from 信号与槽连接.菜单 import 连接菜单信号
    print("✅ 导入成功！")
except ImportError as e:
    print(f"❌ 导入失败: {e}")