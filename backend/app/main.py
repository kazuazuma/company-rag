from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "hello ai Enginear!"
    }
    
@app.get("/users/{user_id}")
def get_user(user_id: int):
    
    return{
        "id": user_id,
        "name": "taro",
    }