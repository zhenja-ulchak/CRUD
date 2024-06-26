
import os
from pathlib import Path
from typing import Optional
from repo import Repository
from model import todo_list

class ToDoListRepository(Repository.RepositoryInterface[todo_list.TodoList]):

    
    def read(self, id: str) -> Optional[todo_list.TodoList]:  
        path = "C:/Users/zhenja/Desktop/test/list_file/" # C:\Users\zhenja\Desktop\test\list_file
        all_path = f"{path}{id}.txt"
        print(all_path)
    
