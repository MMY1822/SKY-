from typing import Dict, Callable

class SignalMapper:
    def __init__(self):
        self._signal_map = {}

    def register(self, signal_name: str, handler: Callable):
        self._signal_map[signal_name] = handler

    def 连接信号(self, main_window):
        for signal_name, handler in self._signal_map.items():
            if hasattr(main_window, signal_name):
                signal = getattr(main_window, signal_name)
                signal.triggered.connect(handler)
            else:
                print(f"警告: 未找到信号 {signal_name}")

信号表 = SignalMapper()