from typing import List
from .todo_item import TodoItem
class TodoList():
    def __init__(self, items:List[TodoItem]):
        self.items = items

        