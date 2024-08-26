import os
import sys 
from io import StringIO

class PythonExecutor():

    def execute_code(self,code):
        self.save_in_txt(code)
        print(f"running the following code: {code}")
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code)
        sys.stdout = old_stdout
        print(redirected_output.getvalue())
        return redirected_output.getvalue()
    
    def save_in_txt(self,code):
        if os.path.exists('/history.txt'):
            mode='a'
        else:
            mode='w'
        with open('history.txt',mode) as file:
            file.write(code+'\n')

    def get_executions_history(self):
        with open("history.txt", 'r') as file:
            content=file.read()
            return content