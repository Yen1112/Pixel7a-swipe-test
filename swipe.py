import subprocess
import time

def swipe_left_to_right():
    
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
    print("swipe left or griht 100 times")
    for i in range(100):
        if i % 2 == 0:
            swipe_right_to_left()
        else:
            swipe_left_to_right()
        time.sleep(0.5)  # avoid too fast
    print("finish！")

if __name__ == "__main__":
    main()
