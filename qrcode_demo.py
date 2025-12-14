import gradio as gr
import qrcode
from PIL import Image

def generate_qr(text):
    """
    接收文字輸入，產生 QR Code 圖片
    """
    if not text:
        return None
        
    # 設定 QR Code 參數
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # 加入資料
    qr.add_data(text)
    qr.make(fit=True)
    
    # 產生圖片
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 轉換為 PIL Image 物件 (Gradio 可以直接處理)
    return img.get_image()

if __name__ == "__main__":
    # 建立 Gradio 介面
    demo = gr.Interface(
        fn=generate_qr,
        inputs=gr.Textbox(label="輸入文字或網址", placeholder="例如: https://www.google.com"),
        outputs=gr.Image(label="產生的 QR Code", type="pil"),
        title="QR Code 產生器",
        description="輸入任何文字或網址，立即產生 QR Code 圖片！",
        examples=["https://www.google.com", "Hello Gradio", "這是中文測試"]
    )
    
    print("正在啟動 QR Code 產生器...")
    demo.launch(share=True)
