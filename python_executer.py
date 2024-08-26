import os

class PythonExecutor():

    def execute_code(self,code):
        self.save_in_txt(code)
        return exec(code)
    
    def save_in_txt(self,code):
        if os.path.exists('/history.txt'):
            mode='a'
        else:
            mode='w'
        with open('/history.txt',mode) as file:
            file.write(code+'\n')

    def get_executions_history(self):
        with open("history.txt", 'r') as file:
            content=file.read()
            return content
    
executor=PythonExecutor()

executor.execute_code("""a=3+4 
print(a)""")
print(executor.get_executions_history())