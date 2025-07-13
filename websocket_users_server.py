import asyncio

import websockets

from websockets import ServerConnection

# обработчик
async def echo(websocket:ServerConnection):
    async for message in websocket:
        for _ in range(5):
            print(f"{_+1} Сообщение пользователя: {message}")
            response = f"{_+1} Сообщение пользователя: {message}"
            await websocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("websocket server start ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())