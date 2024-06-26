import json
import os
from pathlib import Path
from typing import Optional
from repo import Repository
from model import todo_list
from model import todo_item

class ToDoListRepository(Repository.RepositoryInterface[todo_list.TodoList]):

    
    def read(self, id: str) -> Optional[todo_list.TodoList]:
        path = os.getcwd() 
       
        # path = "C:/Users/zhenja/Desktop/test/CRUD/list_file/" # C:\Users\zhenja\Desktop\test\list_file
        all_path = f"{path}\list_file\{id}.json"
        isExist = os.path.exists(path)
        if isExist :
            open_file = open(all_path, "r")
            data = json.load(open_file)
            items = []
            for item in data['items']:
                items.append(todo_item.TodoItem(item["title"]))# item["title"] - сирі данні , todo_item.TodoItem(item["title"]) - передаєм екземплір моделі   
            return todo_list.TodoList(items)

        return None
    
    def write(self, id, obj: todo_list.TodoList):
        path = os.getcwd()
        all_path = f"{path}\list_file\{id}.json"
        isExist = os.path.exists(path)
        dict_w = {}
        
        write_file = open(all_path, "w")
        for item in obj.items:
            print(item.title)