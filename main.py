'''
Py-Todo - The simplest to-do app
Thomas Gregory 2021
'''
import os

# Simple function to clear the terminal screen at opportune times


def clear(): return os.system('clear')


# This function will be fired if the 'data.txt' file isn't found in the root directory of this program
# Function will get the user name from the user and add it to the first line of the data file


def new_user_greeting():
    user_name = input(
        'Hello, welcome to py-todo. Please enter your username: ')
    dataFile = open('data.txt', 'w')
    dataFile.writelines(f'{user_name} \n')
    dataFile.close()
    print(f'Welcome, {user_name}')


# Entry point of the application.
# If data file exists --> send to main prompt screen.
# If data file does not exist --> send to new user greeting screen.
if os.path.exists('./data.txt'):
    dataFile = open('data.txt', 'r')
    user_name = dataFile.readline()
    print(f'Welcome back, {user_name}')
    dataFile.close()
else:
    new_user_greeting()


# The prompt screen where we get the command from the user to view todos, add a todo, or exit the application.
def prompt_screen():
    dataFile = open('data.txt', 'r')
    todo_amount = (len(dataFile.readlines()) - 1)
    dataFile.close()
    print(f'You have {todo_amount} current todo(s)')
    command = input(
        'Would you like to [V]iew todos, [A]dd todos, [D]elete todos or [E]xit: ')
    command_logic(command, todo_amount)


# The command logic for what to do when the user enters a certain command
def command_logic(command, todo_amount):
    if command.lower() == 'v' or command.lower() == 'view':
        view_todos(todo_amount)
    elif command.lower() == 'a' or command.lower() == 'add':
        add_todo()
    elif command.lower() == 'e' or command.lower() == 'exit':
        exit()
    elif command.lower() == 'd' or command.lower() == 'del' or command.lower() == 'delete':
        clear()
        delete_prompt()
    else:
        print('Incorrect command, please try again.')
        prompt_screen()


# Add a todo to the datafile here
def add_todo():
    clear()
    new_todo = input('Enter new todo: ')
    dataFile = open('data.txt', 'a')
    dataFile.writelines(f'{new_todo} \n')
    dataFile.close()
    clear()
    print('Todo item added!')
    prompt_screen()


# Read the todos from the datafile here
def view_todos(todo_amount):
    clear()
    dataFile = open('data.txt', 'r')
    todos = dataFile.readlines()[1:]
    dataFile.close()
    for todo in todos:
        print(f'[{todos.index(todo)}] - {todo}')
    prompt_screen()

# This gets the delete command from the user and sends it to the delete_logic function


def delete_prompt():
    dataFile = open('data.txt', 'r')
    todos = dataFile.readlines()[1:]
    dataFile.close()
    for todo in todos:
        print(f'[{todos.index(todo)}] - {todo}')
    del_command = input(
        'Which [#] Todo would you like to delete? [A] for all, [D] to delete all data: ')
    delete_logic(del_command)

# Handles the logic of my delete command, letting the user pick what to delete.


def delete_logic(del_command):
    if del_command.isdigit():
        delete_todo(del_command)
    elif del_command.lower() == 'a' or del_command.lower() == 'all':
        dataFile = open('data.txt', 'r')
        user_name = dataFile.readline()
        dataFile.close()
        dataFile = open('data.txt', 'w+')
        dataFile.writelines(user_name)
        dataFile.close()
        clear()
        prompt_screen()
    elif del_command.lower() == 'd' or del_command.lower() == 'delete' or del_command.lower() == 'del':
        os.remove('./data.txt')
        clear()
        print('Removed all data')
        new_user_greeting()
    else:
        clear()
        print('Sorry, command not recognized. Please try again.')
        delete_prompt()

# This handles the deletion of a specific todo item within my list.
# !!!!! I need to find an easier/cleaner way to do this.
# Resource: https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-file


def delete_todo(del_command):
    id = int(del_command)
    dataFile = open('data.txt', 'r+')
    user_name = dataFile.readline()
    todos = dataFile.readlines()
    print(user_name)
    print(todos)
    dataFile.close()
    dataFile = open('data.txt', 'w+')
    todos.pop(id)
    print(todos)
    dataFile.writelines(user_name)
    dataFile.writelines(todos)
    dataFile.close()
    clear()
    print('Todo item deleted...')
    prompt_screen()


# !!!! Clean this up when I get the time
clear()
prompt_screen()
