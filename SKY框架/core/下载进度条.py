import os
import urllib.request
import ssl
from PyQt6.QtCore import QThread, pyqtSignal, QObject
from PyQt6.QtWidgets import QProgressBar, QLabel


class DownloadManager(QObject):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.progress_bar = None
            cls._instance.percent_label = None
        return cls._instance

    def set_ui_elements(self, progress_bar: QProgressBar, percent_label: QLabel):
        self.progress_bar = progress_bar
        self.percent_label = percent_label
        self._reset_ui()

    def _reset_ui(self):
        if self.progress_bar:
            self.progress_bar.setValue(0)
        if self.percent_label:
            self.percent_label.setText("0%")
            self.percent_label.setStyleSheet("color: #666;")

    def _update_progress(self, progress):
        if self.progress_bar:
            self.progress_bar.setValue(progress)
        if self.percent_label:
            self.percent_label.setText(f"{progress}%")
            if progress == 100:
                self.percent_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
            elif progress < 0:
                self.percent_label.setStyleSheet("color: #F44336; font-weight: bold;")
            else:
                self.percent_label.setStyleSheet("color: #2196F3;")


class DownloadThread(QThread):
    download_finished = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    progress_updated = pyqtSignal(int)

    def __init__(self, url, save_path):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self._is_running = True

    def run(self):
        temp_path = self.save_path + '.tmp'
        try:
            # 创建目录
            os.makedirs(os.path.dirname(self.save_path), exist_ok=True)

            # 删除已存在的临时文件
            if os.path.exists(temp_path):
                os.remove(temp_path)

            # 创建自定义opener处理SSL验证
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            https_handler = urllib.request.HTTPSHandler(context=ssl_context)
            opener = urllib.request.build_opener(https_handler)
            urllib.request.install_opener(opener)

            def progress_hook(count, block_size, total_size):
                if not self._is_running:
                    raise InterruptedError("下载被用户取消")

                if total_size > 0:
                    progress = min(int(count * block_size * 100 / total_size), 100)
                    self.progress_updated.emit(progress)

            # 执行下载
            urllib.request.urlretrieve(
                url=self.url,
                filename=temp_path,
                reporthook=progress_hook
            )

            # 重命名临时文件
            if os.path.exists(self.save_path):
                os.remove(self.save_path)
            os.rename(temp_path, self.save_path)

            if self._is_running:
                self.download_finished.emit(self.save_path)

        except Exception as e:
            if self._is_running:
                self.error_occurred.emit(f"下载错误: {str(e)}")
        finally:
            # 清理临时文件
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except:
                    pass

    def stop(self):
        self._is_running = False
        self.wait(1000)