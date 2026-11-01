import pyautogui
import pyperclip
import time
import random
from PIL import Image
import win32clipboard
import io

# ==========修改这里==========
emoji_path = r"C:\emoji\cat.gif"  # 你的表情包本地路径
send_count = 10                   # 发送条数
send_interval = 2.5               # 间隔秒数
wait_start = 8                   # 启动倒计时
# ===========================

# 图片复制到剪贴板函数
def copy_image_to_clipboard(img_path):
    img = Image.open(img_path)
    output = io.BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

print(f"⚠️ {wait_start}秒后开始发送！光标放在微信输入框！")
time.sleep(wait_start)

try:
    for i in range(send_count):
        copy_image_to_clipboard(emoji_path)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)
        pyautogui.press("enter")
        print(f"✅已发送第{i+1}条表情包")
        time.sleep(send_interval)
    print("🎉全部发送完成！")
except KeyboardInterrupt:
    print("\n🛑程序已停止")