from fastapi import FastAPI

from router import network, event, system

app = FastAPI()

app.include_router(router=network.router, prefix='/networks')
app.include_router(router=event.router, prefix='/events')
app.include_router(router=system.router, prefix='/system')
