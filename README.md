# py_webview

## state management

Redux Data Flow

```mermaid
flowchart LR
  C[Components]
  subgraph AC[Action Creator]
    A[Action]
  end
  subgraph P[python（store）]
    R[Reducers]
    n([new state])
    o([old state])
    R -->|update| n
    o --> R
  end

C -->|input| AC
A -->|dispatch| R
n -->|state| C
```

## wry in rust vs pywebview in python

||rust|python|note|
|:--|:--                   |:--                 |:--|
|   |window.ipc.postMessage| -                  | in wry/Electron |
|   | -                    |window.pywebview.api| in pywebview    |

```javascript

// for pywebview
const res = window.pywebview.api.postMessage({ 'foo' : 'bar' })

// for wry
async function postMessage(obj){
  function handler(e) {
    window.removeEventListener('customEvent', handler);
    resolve(e.detail);
  }
  window.addEventListener('customEvent', handler, false);
  window.ipc.postMessage(JSON.stringify(obj));
}

// for wry
async function postMessage(obj){
  await fetch("http://wry.localhost/", {
    method: "POST",
    body: JSON.stringify(obj),
  });
}

```