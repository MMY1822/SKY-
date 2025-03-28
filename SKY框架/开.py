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