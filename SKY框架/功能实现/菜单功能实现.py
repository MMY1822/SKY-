import subprocess
import traceback
import psutil
from PyQt6.QtGui import  QKeySequence, QShortcut
from core.清屏 import ScreenCleaner
from core.下载进度条 import DownloadManager, DownloadThread
from PyQt6.QtCore import QStandardPaths, QCoreApplication, pyqtSignal, QThread
import os
import sys
from core.log配置 import global_logger



class 菜单功能实现:
    def __init__(self, main_window):
        self.adb_fastboot_dir = None
        self.main_window = main_window
        self.download_thread = None
        self.cleaner = ScreenCleaner()
        self.快捷键清屏()
        self._setup_dirs()
        self._setup_dirs2()


    def open_shebei(self):
        global_logger.append_log("<font color='blue'>正在打开设备管理器...</font>")
        try:
            # 使用shell=False更安全
            subprocess.Popen('devmgmt.msc', shell=True)
            global_logger.append_log("<font color='green'>✓ 设备管理器已打开</font>")
        except Exception as e:
            global_logger.append_log(f"<font color='red'>✗ 打开失败: {str(e)}</font>")
            traceback.print_exc()

    def _setup_dirs(self):
        desktop = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        self.download_dir = os.path.join(desktop, "skybox", "temp")
        os.makedirs(self.download_dir, exist_ok=True)
        self.driver_path = os.path.join(self.download_dir, "sky.exe")

    def _setup_dirs2(self):
        desktop = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        self.download_dir = os.path.join(desktop, "skybox", "temp")
        os.makedirs(self.download_dir, exist_ok=True)
        self.driver_path2 = os.path.join(self.download_dir, "ADB-FASTBOOT.zip")


    def qudong1(self):
        try:
            if self.download_thread and self.download_thread.isRunning():
                self._safe_stop_download()
            url = 'https://pan.skybox.mom/d/%E9%85%8D%E7%BD%AE%E7%9B%B4%E9%93%BE/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E5%AE%89%E5%8D%93%E9%A9%B1%E5%8A%A8.exe'
            save_path = self.driver_path

            global_logger.append_log("<font color='blue'>开始下载驱动...</font>")
            DownloadManager()._reset_ui()

            self.download_thread = DownloadThread(url, save_path)
            self.download_thread.progress_updated.connect(DownloadManager()._update_progress)
            self.download_thread.download_finished.connect(self._on_download_finished)
            self.download_thread.error_occurred.connect(self._on_download_error)

            QCoreApplication.processEvents()

            self.download_thread.start()

        except Exception as e:
            global_logger.append_log(f"<font color='red'>初始化下载失败: {str(e)}</font>")
            traceback.print_exc()

    def qudong2(self):
        try:
            if self.download_thread and self.download_thread.isRunning():
                self._safe_stop_download()
            url = 'https://pan.skybox.mom/d/%E9%85%8D%E7%BD%AE%E7%9B%B4%E9%93%BE/%E9%80%9A%E7%94%A8%E9%A9%B1%E5%8A%A8.exe'
            save_path = self.driver_path
            global_logger.append_log("<font color='blue'>开始下载驱动...</font>")
            DownloadManager()._reset_ui()
            self.download_thread = DownloadThread(url, save_path)
            self.download_thread.progress_updated.connect(DownloadManager()._update_progress)
            self.download_thread.download_finished.connect(self._on_download_finished)
            self.download_thread.error_occurred.connect(self._on_download_error)
            QCoreApplication.processEvents()
            self.download_thread.start()
        except Exception as e:
            global_logger.append_log(f"<font color='red'>初始化下载失败: {str(e)}</font>")
            traceback.print_exc()

    def qudong3(self):
        try:
            if self.download_thread and self.download_thread.isRunning():
                self._safe_stop_download()
            url = 'https://pan.skybox.mom/d/%E9%85%8D%E7%BD%AE%E7%9B%B4%E9%93%BE/%E9%AB%98%E9%80%9A%E5%AE%98%E6%96%B9%E5%85%A8%E7%AB%AF%E5%8F%A3usb%E9%A9%B1%E5%8A%A8-qud.win.1.1_installer_10061.1.exe'
            save_path = self.driver_path
            global_logger.append_log("<font color='blue'>开始下载驱动...</font>")
            DownloadManager()._reset_ui()
            self.download_thread = DownloadThread(url, save_path)
            self.download_thread.progress_updated.connect(DownloadManager()._update_progress)
            self.download_thread.download_finished.connect(self._on_download_finished)
            self.download_thread.error_occurred.connect(self._on_download_error)
            QCoreApplication.processEvents()
            self.download_thread.start()
        except Exception as e:
            global_logger.append_log(f"<font color='red'>初始化下载失败: {str(e)}</font>")
            traceback.print_exc()

    def qudong4(self):
        try:
            if self.download_thread and self.download_thread.isRunning():
                self._safe_stop_download()
            url = 'https://pan.skybox.mom/d/%E9%85%8D%E7%BD%AE%E7%9B%B4%E9%93%BE/%E5%BE%AE%E8%BD%AF%E8%BF%90%E8%A1%8C%E5%BA%93.exe'
            save_path = self.driver_path
            global_logger.append_log("<font color='blue'>开始下载驱动...</font>")
            DownloadManager()._reset_ui()
            self.download_thread = DownloadThread(url, save_path)
            self.download_thread.progress_updated.connect(DownloadManager()._update_progress)
            self.download_thread.download_finished.connect(self._on_download_finished)
            self.download_thread.error_occurred.connect(self._on_download_error)
            QCoreApplication.processEvents()
            self.download_thread.start()
        except Exception as e:
            global_logger.append_log(f"<font color='red'>初始化下载失败: {str(e)}</font>")
            traceback.print_exc()

    def toupin(self):
        try:
            if self.download_thread and self.download_thread.isRunning():
                self._safe_stop_download()
            url = 'https://pan.skybox.mom/d/%E9%85%8D%E7%BD%AE%E7%9B%B4%E9%93%BE/%E6%8A%95%E5%B1%8FPRO.exe'
            save_path = self.driver_path
            global_logger.append_log("<font color='blue'>开始下载投屏面板...</font>")
            DownloadManager()._reset_ui()
            self.download_thread = DownloadThread(url, save_path)
            self.download_thread.progress_updated.connect(DownloadManager()._update_progress)
            self.download_thread.download_finished.connect(self._on_download_finished)
            self.download_thread.error_occurred.connect(self._on_download_error)
            QCoreApplication.processEvents()
            self.download_thread.start()
        except Exception as e:
            global_logger.append_log(f"<font color='red'>初始化下载失败: {str(e)}</font>")
            traceback.print_exc()

    def 快捷键清屏(self):
        self.clear_shortcut = QShortcut(QKeySequence("Ctrl+L"), self.main_window)
        self.clear_shortcut.activated.connect(self.clear)

    def clear(self):
        try:
            self.cleaner.execute()

        except Exception as e:
            print(f"清屏错误: {e}")

    def _safe_stop_download(self):
        try:
            if self.download_thread:
                self.download_thread.stop()
                self.download_thread.wait(2000)  # 等待2秒
                if self.download_thread.isRunning():
                    self.download_thread.terminate()
                self.download_thread.deleteLater()
                self.download_thread = None
        except Exception as e:
            global_logger.append_log(f"<font color='orange'>停止下载时出错: {str(e)}</font>")

    def _on_download_finished(self, path):
        try:
            # 验证文件
            if not os.path.exists(path):
                raise FileNotFoundError(f"下载文件不存在: {path}")

            file_size = os.path.getsize(path)
            if file_size == 0:
                raise ValueError("下载文件为空")

            global_logger.append_log(
                f"<font color='green'>✓ 下载完成: {path} (大小: {file_size / 1024 / 1024:.2f}MB)</font>")
            DownloadManager()._update_progress(100)

            # 处理事件队列
            QCoreApplication.processEvents()

            # 跨平台打开方式
            try:
                if sys.platform == 'win32':
                    os.startfile(os.path.normpath(path))
                elif sys.platform == 'darwin':
                    subprocess.Popen(['open', path], shell=False)
                else:
                    subprocess.Popen(['xdg-open', path], shell=False)
            except Exception as open_error:
                global_logger.append_log(f"<font color='orange'>⚠ 无法自动打开，请手动运行: {path}</font>")
                traceback.print_exc()

        except Exception as e:
            global_logger.append_log(f"<font color='red'>✗ 完成处理失败: {str(e)}</font>")
            traceback.print_exc()
        finally:
            self.download_thread = None

    def _on_download_error(self, error):
        try:
            global_logger.append_log(f"<font color='red'>❌ 下载错误: {error}</font>")
            DownloadManager()._update_progress(-1)
            QCoreApplication.processEvents()
        except Exception as e:
            traceback.print_exc()
        finally:
            self.download_thread = None

    def clear_ADB(self):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'].lower() in ['adb.exe', 'fastboot.exe']:
                    global_logger.append_log(f"找到进程 {proc.info['name']}, PID: {proc.info['pid']}, 正在终止")
                    proc.terminate()
                    proc.wait()
                    global_logger.append_log(f"进程 {proc.info['name']} 已成功终止")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

