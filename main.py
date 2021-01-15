'''
Py-Todo - The simplest to-do app
Thomas Gregory 2021
'''


# IMPORTS - todos to control the todolist in the database, user_data from the database, os to manipulate system files
from database import todos
from database import user_data
import os
import sys


# Simple function to clear the terminal screen at opportune times
def clear(): return os.system('clear')


# Function gets called when the user deletes all data, or a new user is introduced to py-todo
# This function will allow the user to set their name and it will be saved in the db
def new_user_greeting():
    user_name = input(
        'Hello, welcome to py-todo. Please enter your username: ')
    user = {"name": user_name}
    user_data.insert_one(user)
    print(f'Welcome, {user_name}')
    prompt_screen()


# The prompt screen where we get the command from the user to view todos, add a todo, or exit the application.
def prompt_screen():
    todo_amount = todos.count_documents({})
    print(f'You have {todo_amount} current todo(s)')
    command = input(
        'Would you like to [V]iew todos, [A]dd todos, [D]elete todos or [E]xit: ')
    command_logic(command)


# The deletion command logic for what to do when the user enters a certain command
def command_logic(command):
    if command.lower() == 'v' or command.lower() == 'view':
        view_todos()
    elif command.lower() == 'a' or command.lower() == 'add':
        add_todo()
    elif command.lower() == 'e' or command.lower() == 'exit':
        sys.exit(1)
    elif command.lower() == 'd' or command.lower() == 'del' or command.lower() == 'delete':
        clear()
        delete_prompt()
    else:
        print('Incorrect command, please try again.')
        prompt_screen()


# Add a todo to the database
def add_todo():
    clear()
    todo = input('Enter new todo: ')
    id = get_id()
    new_todo = {"title": todo, "id": id}
    todos.insert_one(new_todo)
    clear()
    print('Todo item added!')
    prompt_screen()


# A function to quickly access all current todos and return them in a list
def get_todos():
    todos_list = list(todos.find({}))
    return(todos_list)


# Uses get_todos() to display all of the available todos
def view_todos():
    clear()
    todos_list = get_todos()
    for todo in todos_list:
        print(todo['id'], '-', todo['title'])
    prompt_screen()


# This gets the delete command from the user and sends it to the delete_logic function
def delete_prompt():
    todos = get_todos()
    for todo in todos:
        print(todo['id'], '-', todo['title'])
    del_command = input(
        'Which [#] Todo would you like to delete? [A] for all, [D] to delete all data, [B] to go back: ')
    delete_logic(del_command)


# Very simple function that checks if the todo you want to delete exists in the database
def todo_exists(id):
    todo = todos.find({"id": id})
    if todo:
        return True
    else:
        return False


# Handles the logic of my delete command, letting the user pick what to delete.
def delete_logic(del_command):
    if del_command.isdigit():
        del_command = int(del_command)
        if todo_exists(del_command):
            delete_todo(del_command)
        else:
            clear()
            print('That todo does not exist... please try again.')
            delete_prompt()

    elif del_command.lower() == 'a' or del_command.lower() == 'all':
        todos.remove({})
        clear()
        print('All todos removed')
        prompt_screen()
    elif del_command.lower() == 'd' or del_command.lower() == 'delete' or del_command.lower() == 'del':
        todos.remove({})
        user_data.remove({})
        clear()
        print('Removed all data')
        new_user_greeting()
    elif del_command.lower() == 'b' or del_command.lower() == 'back':
        prompt_screen()
    else:
        clear()
        print('Sorry, command not recognized. Please try again.')
        delete_prompt()


# Generates a very simple ID for each todo based on how many todos we currently have
def get_id():
    id = todos.count_documents({})
    return id


# This function will loop through the current todos and change their IDs and re-order them. Then it will clear the db and repopulate it with the new todos.
# def refresh_ids():


# This handles the deletion of a specific todo item within my database
# After deletion, we will need to re-id each of the todos so the numbers don't skip.
# This is my next thing to do
def delete_todo(del_command):
    id = int(del_command)
    todos.delete_one({"id": id})
    clear()
    print('Todo item deleted...')
    # refresh_ids() - NEED TO ADD THIS FUNCTIONALITY SOON
    prompt_screen()


# Starting page of the application
def landing_page():
    if user_data.count_documents({}) == 0:
        new_user_greeting()
    else:
        clear()
        user = user_data.find_one({})
        user_name = user['name']
        print(f'Welcome back, {user_name}')
        prompt_screen()


# Start the application
landing_page()
