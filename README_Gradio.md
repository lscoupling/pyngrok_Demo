# Gradio 範例專案

這個部分展示了如何使用 [Gradio](https://gradio.app/) 快速建立互動式的 Web 應用程式。Gradio 非常適合用於展示機器學習模型、資料視覺化或是簡單的工具型應用。

## 專案列表

目前包含以下兩個範例：

### 1. 貓狗圖片顯示器 (`gradio_demo.py`)
一個簡單的圖片瀏覽器，串接了公開的 API。
- **功能**：輸入 "cat" (貓) 或 "dog" (狗)，即時顯示隨機的貓咪或狗狗圖片。
- **技術**：使用 `requests` 呼叫 API，並透過 Gradio 的 `HTML` 元件顯示圖片。

### 2. QR Code 產生器 (`qrcode_demo.py`)
實用的工具型應用。
- **功能**：輸入任何文字或網址，立即產生對應的 QR Code 圖片供下載。
- **技術**：使用 `qrcode` 套件生成圖片，並透過 Gradio 的 `Image` 元件顯示。

## 如何執行

1. **安裝依賴套件**
   請確保您已經安裝了 `requirements.txt` 中的套件：
   ```bash
   pip install -r requirements.txt
   ```

2. **執行貓狗顯示器**
   ```bash
   python gradio_demo.py
   ```
   執行後點擊終端機顯示的 `https://xxxx.gradio.live` 連結。

3. **執行 QR Code 產生器**
   ```bash
   python qrcode_demo.py
   ```
   執行後點擊終端機顯示的 `https://xxxx.gradio.live` 連結。

## 關於 Gradio
Gradio 的特色在於只需要幾行 Python 程式碼，就能產生可分享的網頁介面 (Shareable UI)。設定 `launch(share=True)` 後，會自動產生一個公開網址，有效期為 72 小時，非常適合快速展示成果給他人看。
