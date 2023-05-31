import asyncio
import websockets
from uuid import uuid4


class ChatServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connections = set()

    async def handle_client(self, websocket: websockets, path):
        websocket.id = str(uuid4()).split("-")[1]
        for connection in self.connections:
            if websocket != connection:
                await connection.send(f"User {websocket.id}"
                                      " connected to the chat!")

        await websocket.send("Connected! Have fun chatting!")
        self.connections.add(websocket)
        try:
            async for message in websocket:
                await self.broadcast(websocket, message)
        finally:
            self.connections.remove(websocket)

    async def broadcast(self, websocket: websockets, message: str):
        for connection in self.connections:
            if websocket != connection:
                await connection.send(f"<User {websocket.id}>: {message}")

    async def start(self):
        async with websockets.serve(self.handle_client, self.host, self.port):
            print("The chat server is up and "
                  f"running at ws://{self.host}:{self.port}")
            await asyncio.Future()


if __name__ == "__main__":
    chat_server = ChatServer('localhost', 5555)
    asyncio.run(chat_server.start())
