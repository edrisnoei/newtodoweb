import streamlit as slt

import functions
import os

if not os.path.exists(r"D:\Python_Programs\webupload\todos.txt"):
    with open(r"D:\Python_Programs\webupload\todos.txt", 'w') as file:
        pass

slt.title("My Todo App")
slt.subheader("Here is the todo list")
def add_todo():
    todos = functions.get_todos("todos.txt")
    if slt.session_state["new_todo"] + "\n" not in todos:
        todos.append(slt.session_state["new_todo"] + "\n")
        slt.session_state["new_todo"] = ""
        functions.write_todos(todos,filepath="todos.txt")
    else:
        slt.text("repeated todo")




todos = functions.get_todos('todos.txt')
for todo in todos:
    checkbox = slt.checkbox(todo,key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos,filepath="todos.txt")
        del slt.session_state[todo]
        slt.experimental_rerun()


slt.text_input(label="",key="new_todo",on_change=add_todo,placeholder="Enter a todo")

slt.session_state