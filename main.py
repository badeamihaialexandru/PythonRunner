from flask import Flask,request
from python_executer import *

app = Flask(__name__)

pythonEx = PythonExecutor()

@app.route('/execute',methods = ['POST'])
def execute():
    code = request.json["code"]
    return pythonEx.execute_code(code)
     

@app.route('/history', methods=['GET'])
def history():
    return "Empty"

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 4000, debug = True)
