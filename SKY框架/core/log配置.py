from PyQt6.QtWidgets import QTextBrowser
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor


class LogManager:
    def __init__(self):
        self.log_widget = None

    def set_log_widget(self, log_widget: QTextBrowser):
        self.log_widget = log_widget
        if self.log_widget:
            # 设置为不可编辑、不可选择
            self.log_widget.setReadOnly(True)
            self.log_widget.setTextInteractionFlags(
                Qt.TextInteractionFlag.NoTextInteraction
            )
            # 设置基础样式
            self.log_widget.setStyleSheet("""
                QTextBrowser {
                    background-color: #f5f5f5;
                    border: 1px solid #ddd;
                    padding: 5px;
                    font-family: Consolas, 'Courier New', monospace;
                    font-size: 10pt;
                }
            """)

    def append_log(self, message: str, scroll_to_end=True):
        if self.log_widget is not None:
            self.log_widget.append(message)
            if scroll_to_end:
                self._scroll_to_end()
        else:
            print(f"[LOG FALLBACK] {message}")

    def _scroll_to_end(self):
        cursor = self.log_widget.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.log_widget.setTextCursor(cursor)
        self.log_widget.ensureCursorVisible()

    def clear_log(self):
        if self.log_widget is not None:
            self.log_widget.clear()


global_logger = LogManager()