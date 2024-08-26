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