from importlib.resources import files
import os
from pathlib import Path
from typing import Optional
from CRUD.repo.Repository import  RepositoryInterface
from CRUD.model.todo_list import TodoList

class ToDoListRepository(RepositoryInterface[TodoList]):
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def T_list(self):
        return self.todo_list
    
    def read(id: str) -> Optional[TodoList]:  
        path: Path = Path("C:/Users/zhenja/Desktop/test/list_file") # C:\Users\zhenja\Desktop\test\list_file
        path.is_dir()
        path.is_file()
        path.stat().st_size
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                return file
                
        for file in files("."):  
            file_info = file.split('.')
            if file_info[1] == 'txt':
                print(file)
    
