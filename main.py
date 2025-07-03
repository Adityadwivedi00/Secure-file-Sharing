from fastapi import FastAPI
from .database import Base, engine
from routes import ops_user, client_user

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(ops_user.router)
app.include_router(client_user.router)
