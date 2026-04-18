import fastapi
import uvicorn


app = fastapi.FastAPI()
@app.get('/')
def index():
    return {
        'message': 'Hello World!'
    }

@app.get("/login")
def login(username: str, password: str):
    return {
        'username': username,
        'password': password
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)