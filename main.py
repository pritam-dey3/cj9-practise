from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_handler(ws: WebSocket):
    await ws.accept()
    while True:
        txt = await ws.receive_text()
        print(txt)
        await ws.send_text(txt)
