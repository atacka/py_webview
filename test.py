import webview

class Api:
  def button_clicked(self, message):
    print(f"Received from JavaScript: {message}")
    # 必要に応じて処理を追加
    return "Message received by Python!"
  
api = Api()
webview.create_window('Hello world', 'index.html', js_api=api)
webview.start()