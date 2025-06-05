import subprocess
import time

def swipe_left_to_right():
    # Pixel 7a 螢幕尺寸是 1080x2400，根據這個模擬翻頁滑動
    x_start = 300
    x_end = 900
    y = 1200
    subprocess.run(["adb", "shell", "input", "swipe", str(x_start), str(y), str(x_end), str(y), "200"])

def swipe_right_to_left():
    x_start = 900
    x_end = 300
    y = 1200
    subprocess.run(["adb", "shell", "input", "swipe", str(x_start), str(y), str(x_end), str(y), "200"])

def main():
    print("開始左右滑動 100 次...")
    for i in range(100):
        if i % 2 == 0:
            swipe_right_to_left()
        else:
            swipe_left_to_right()
        time.sleep(0.5)  # 避免過快，看起來更自然
    print("完成滑動！")

if __name__ == "__main__":
    main()
