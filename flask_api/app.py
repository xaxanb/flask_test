import fastapi
import uvicorn
import pymysql
from 类型 import *


app = fastapi.FastAPI()
con = pymysql.connect(host='localhost', user='root', password='123456', database='login')
cursor = con.cursor()



def create_data(name,pwd,new_pwd):
    result = create_if_uers(name,pwd,new_pwd)
    if result['status'] == 'success':
        cursor.execute("insert into user(name,pwd) values(%s,%s)",(name,pwd))
        con.commit()
        return "success"
    else:
        return result['message']

def index():
    return {
        'message': 'Hello World!'
    }

@app.get("/login")
def login(username: str, password: str, new_password: str):
    create_data(username,password,new_password)
    return {
        'username': username,
        'password': password,
        'new_password': new_password    
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)