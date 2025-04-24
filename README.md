# py_webview

## wry in rust vs pywebview in python

||rust|python|note|
|:--|:--|:--|:--|
| |window.ipc.postMessage| - | wry/ElectronのJavaScript API |
| | - |window.pywebview.api.button_clicked| pywebview独自のJavaScript API |

共通化コード例

```javascript
const MyBridge = {
  call: async function (method, ...args) {
    if (window.ipc && typeof window.ipc.postMessage === 'function') {
      // Electron
      return new Promise((resolve) => {
        const callbackChannel = `response-${Date.now()}`;
        window.ipc.once(callbackChannel, (_event, response) => {
          resolve(response);
        });
        window.ipc.postMessage({
          method,
          args,
          callbackChannel,
        });
      });
    } else if (window.pywebview && window.pywebview.api && typeof window.pywebview.api[method] === 'function') {
      // PyWebView
      return window.pywebview.api[method](...args);
    } else {
      throw new Error("No supported bridge found");
    }
  }
};
```
