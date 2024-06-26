from repo import ToDoListRepository
from model import todo_list, todo_item


list_todo =  todo_list.TodoList([todo_item.TodoItem("1"),todo_item.TodoItem("11111")])
To_Do_List_Repository = ToDoListRepository.ToDoListRepository()
# To_Do_List_Repository.read('test')
To_Do_List_Repository.write('test',list_todo)