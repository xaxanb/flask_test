import json
import re


def check_pwd(pwd):
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#￥%&*!?.+\-=_,:;~^$()\[\]{}|\\/<>])[A-Za-z\d@#￥%&*!?.+\-=_,:;~^$()\[\]{}|\\/<>]{6,20}'
    return re.fullmatch(pattern, pwd) is not None
def create_if_uers(name,pwd,new_pwd):
    if (name,pwd,new_pwd) == None:
        return {"status": "error", "message": "用户名或密码不能为空"}
    elif pwd != new_pwd or len(pwd) < 6 or len(pwd) > 20:
        return {"status": "error", "message": "密码不一致或长度小于6"}
    elif check_pwd(pwd) == False:
        return {"status": "error", "message": "密码格式错误"}
    else:
        return {"status": "success", "message": "注册成功"}

if __name__ == '__main__':
 print(check_pwd('123456Zx.'))
 print(create_if_uers('123456Zx87234664264.', '123456Zx.', '123456Zx.')["message"])
