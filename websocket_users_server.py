import asyncio

import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"

        for i in range(1, 6):
            await websocket.send(response)

async def lolo():
    server = await websockets.serve(echo, "localhost", "8765")
    print("Websocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(lolo())


