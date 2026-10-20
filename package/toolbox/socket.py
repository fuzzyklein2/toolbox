import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        print("Received:", message)

server = await websockets.serve(handler, "127.0.0.1", 8765)