import asyncio

from aiohttp import ClientSession, ClientWebSocketResponse, WSMsgType


url = "http://127.0.0.1:8000/ws"


async def main():
    sess = ClientSession()
    ws = await sess.ws_connect(url)
    print("write your messages...")
    await asyncio.gather(wait_for_msg(ws), prompt(ws))


async def wait_for_msg(ws: ClientWebSocketResponse):
    while True:
        rcv = await ws.receive()
        print("got something")
        if rcv.type in (WSMsgType.CLOSE, WSMsgType.ERROR):
            break
        elif rcv.type == WSMsgType.TEXT:
            print(f"- {rcv}")


async def prompt(ws: ClientWebSocketResponse):
    while True:
        print(ws.closed)
        inp = input("- ")
        if inp == "exit":
            break
        await ws.send_str(inp)


if __name__ == "__main__":
    asyncio.run(main())
