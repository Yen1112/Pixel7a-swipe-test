# Pixel Swipe Script

一支簡單的 Python 腳本，透過 ADB 讓 Pixel 7a 自動左右滑動螢幕 100 次，模擬翻頁動作。

## 使用方式

1. 確認你已安裝 ADB，且手機開啟 USB 偵錯。
2. 連接手機。
3. 執行腳本：

```bash
python swipe.py
```

## 注意
- 預設滑動位置是基於 Pixel 7a 螢幕（1080x2400）。
- 滑動時間為 200ms，可自行調整以模擬不同滑動速度。
