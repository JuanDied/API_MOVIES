from fastapi import APIRouter
from fastapi import  HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from utils.jwt_manager import create_token
from schemas.user import User


login_user = APIRouter()




@login_user.post("/login", tags=['Auth'], response_model=dict, status_code=200)
def login(user: User)-> dict:
    if user.email== "admin@gmail.com" and user.password == "admin":
        token:str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)
    raise HTTPException( status_code=401, detail="Unauthorized")
