import webview

class Api:
  state = { "cnt" : 10, "name" : "world" }
  def postMessage(self, message):
    print(f"Received from JavaScript: {message}")
    match message['kind']:
      case 'init':
        return self.state
      case 'inc':
        self.state['cnt'] += 1
        return self.state
      case 'dec':
        self.state['cnt'] -= 1
        return self.state
      case _:
        return self.state

api = Api()
webview.create_window('Hello world', 'index.html', js_api=api)
webview.start() # webview.start(debug=True)