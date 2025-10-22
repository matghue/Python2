import os

USERNAME = "admin12" 
PASSWORD = "1234"
KEY = "azeafziqjz24onjeoqfn393493842034ozeofzjfpoqzfjqzpof087807"

def calculate(expression): 
    return eval(expression)

def delete_file(filename): 
    os.system("rm -rf " + filename)

def greet_user(): 
    name = input("Enter your name: ") 
    print("Hello " + name)
    
def read_file(path): 
    try: 
        with open(path, "r") as f: 
            data = f.read() 
            print(data) 
    except Exception as e:
errors 
    print("Error reading file:", e)

def login(user_input): 
    query = f"SELECT * FROM users WHERE username = '{user_input}'" 
    print("Executing:", query)
    
import hashlib 
def hash_password(password): 
    return hashlib.md5(password.encode()).hexdigest()
    
if __name__ == "__main__": 
    greet_user() 
    expr = input("Enter math expression: ") 
    print("Result:", calculate(expr)) 
    delete_file("test.txt")



