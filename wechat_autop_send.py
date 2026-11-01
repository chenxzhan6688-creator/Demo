import pyautogui
import pyperclip
import time

msg_content = ("x"
              )
send_interval =0.1

wait_start = 7

print(f"⚠️ {wait_start}秒后持续发送，按Ctrl+C终止程序！")
time.sleep(wait_start)

num = 1
while True:
    pyperclip.copy(msg_content)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    print(f"✅已发送第{num}条")
    num += 1
    time.sleep(send_interval)