#!/usr/bin/env python3
import os
import sys
from ppadb.client import Client as AdbClient


def push_file(local_path, remote_dir):
    try:
        # 连接ADB
        adb = AdbClient(host="127.0.0.1", port=5037)
        device = adb.devices()[0]
        print(f"✓ 设备已连接: {device.serial}")

        # 标准化路径
        local_path = os.path.normpath(local_path)
        remote_path = os.path.join(remote_dir.rstrip('/'), os.path.basename(local_path)).replace('\\', '/')

        # 验证文件
        if not os.path.isfile(local_path):
            print(f"✗ 文件不存在: {local_path}")
            return False

        # 执行推送
        print(f"• 本地文件: {local_path}")
        print(f"• 设备路径: {remote_path}")
        print(f"• 文件大小: {os.path.getsize(local_path) / 1024 / 1024:.2f} MB")

        device.push(local_path, remote_path)

        # 验证结果
        remote_size = device.shell(f"stat -c %s {remote_path}").strip()
        if remote_size.isdigit() and int(remote_size) == os.path.getsize(local_path):
            print("✓ 推送成功")
            return True
        print("⚠ 推送完成但大小不匹配")
        return False

    except Exception as e:
        print(f"✗ 错误: {str(e)}")
        return False


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "push":
        # 合并可能被空格分割的路径
        local_path = ' '.join(sys.argv[2:-1])
        remote_dir = sys.argv[-1]
        success = push_file(local_path, remote_dir)
        sys.exit(0 if success else 1)
    else:
        print("使用方法:")
        print("  adb文件推送模块.py push <本地路径> <设备目录>")
        print("示例:")
        print(r"  adb文件推送模块.py push C:\Users\test.img /sdcard")
        sys.exit(1)