from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio
from datetime import datetime

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SSE clock stream
#evesourceresponse-It keeps the HTTP connection open and continuously sends data whenever new information is available.
#async--Because this function waits every second.While waiting,FastAPI should still handle other users.That's why it is asynchronous.
#yield--It sends one value, pauses, and can continue later.
async def clock():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")

        yield {
    "data": current_time
}
        await asyncio.sleep(1)

@app.get("/events")
async def events():
    return EventSourceResponse(clock())

#true--Then repeat the loop.Because it uses await, the server doesn't freeze while waiting
#clock--this tells FastAPI:Don't send a normal JSON response.Instead,start the clock() generator and stream everything it yields.