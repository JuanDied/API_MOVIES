from routers.movie import movie_router
from routers.user import login_user

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler






app = FastAPI()
app.title = "My First API"
app.description = "This is a very fancy project, with auto docs for the API and everything"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(login_user)

Base.metadata.create_all(bind=engine)




# set the action for an endpoint
@app.get("/", tags=['Home'])
def message():
    return HTMLResponse('<h1>Welcome to my API</h1>')




