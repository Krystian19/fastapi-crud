from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "API service is running" 

@app.get("/v1/users")
def get_users():
    return [{"here": "we are"}]

@app.get("/v1/users/{user_id}")
def get_user(user_id: int):
    return {"msg": "this is the user"} 

@app.post("/v1/users")
def create_user():
    return False 

@app.delete("/v1/users/{user_id}")
def destroy_user(user_id: int):
    return True

