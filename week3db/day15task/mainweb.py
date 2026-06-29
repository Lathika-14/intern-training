"""
from fastapi import FastAPI, WebSocket
app = FastAPI()
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept connection
    await websocket.accept()
    while True:
        # Receive message from client
        message = await websocket.receive_text()
        # Send the same message back
        await websocket.send_text(message)

"""
from fastapi import FastAPI, WebSocket
from typing import List
app = FastAPI()
clients: List[WebSocket] = []
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)    #saves conncted client in list
    print("Client connected. Total clients:", len(clients))
    try:
        while True:
            message = await websocket.receive_text()
            print("Message received:", message)
            for client in clients:
                await client.send_text(message)
    except Exception:
        if websocket in clients:
            clients.remove(websocket)
        print("Client disconnected")




