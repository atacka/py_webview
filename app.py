import webview
import threading
import time

state = { "cnt" : 10, "name" : "world" }

def worker(name):
  global window
  global state
  print(f"スレッド {name} 開始")

  state["name"] = "good night"
  yield state
  time.sleep(3)

  print(f"スレッド {name} 終了")
  state["name"] = "wake up!!!"
  window.run_js(f"""
    var customEvent = new CustomEvent('stateChanged', {{
      'detail': { state }
    }});
    window.dispatchEvent(customEvent);
  """)
  yield state

class App:
  threads = []
  
  #getter
  @property
  def state(self):
    global state
    return state
  #setter
  @state.setter
  def state(self, value):
    global state
    state = value

  #method
  def postMessage(self, message):
    print(f"Received from JavaScript: {message}")
    match message['kind']:
      case 'init':
        return state
      case 'inc':
        self.state['cnt'] += 1
        return self.state
      case 'dec':
        self.state['cnt'] -= 1
        return self.state
      case 'sleep':
        self.state['name'] = "good night"
        generator = worker("sleep")
        first_yield_value = next(generator)
        t = threading.Thread(target=lambda: list(generator))
        self.threads.append(t)
        t.start()
        return first_yield_value
      case _:
        return self.state

api = App()
window = webview.create_window('Hello world', 'index.html', js_api=api)
webview.start() # webview.start(debug=True)