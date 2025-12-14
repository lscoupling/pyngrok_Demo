import requests
import gradio as gr

def catordog(a):
    """
    根據輸入回傳貓或狗的圖片 HTML 標籤
    """
    # 轉換輸入為小寫並去除空白，增加容錯率
    choice = str(a).lower().strip()
    
    imgurl = ""
    
    if choice == 'cat' or choice == '貓':
        url = 'https://api.thecatapi.com/v1/images/search'
        try:
            r = requests.get(url)
            datas = r.json()
            imgurl = datas[0]['url']
        except Exception as e:
            return f"取得貓咪圖片失敗: {e}"
            
    elif choice == 'dog' or choice == '狗':
        url = 'https://dog.ceo/api/breeds/image/random'
        try:
            r = requests.get(url)
            datas = r.json()
            imgurl = datas['message']
        except Exception as e:
            return f"取得狗狗圖片失敗: {e}"
            
    else:
        return "請輸入 'cat' (貓) 或 'dog' (狗)"
    
    # 回傳 HTML img 標籤，並限制最大寬高以免圖片太大
    return f"<img src='{imgurl}' style='max-width: 100%; max-height: 600px; object-fit: contain;'>"

if __name__ == "__main__":
    # 建立 Gradio 介面
    demo = gr.Interface(
        title="貓狗圖片顯示器",
        description="輸入 'cat' 或 'dog' (也可以輸入中文 '貓' 或 '狗') 來取得隨機圖片",
        fn=catordog,
        inputs=gr.Textbox(label="請輸入關鍵字", placeholder="例如: cat, dog, 貓, 狗"),
        outputs=gr.HTML(label="圖片結果"),
        examples=["cat", "dog", "貓", "狗"]
    )
    
    # 啟動 Gradio
    # share=True 會產生一個公開的 gradio.live 網址，方便分享
    print("正在啟動 Gradio...")
    demo.launch(share=True)
