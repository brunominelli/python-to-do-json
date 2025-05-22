from models.task import Task
import os

task = Task()

def main_menu():
    os.system('cls')
    print('''
        TO DO LIST
        Menu
        
        1. Create Task
        2. Read Tasks
        3. Read Tasks by ID
        4. Update Task
        5. Delete Task
        6. Exit
        ''')

def select_option():
    try:
        option = int(input('Option: '))
        
        if option == 1:
            create_task()
        elif option == 2:
            read_tasks()
        elif option == 3:
            read_task_by_id()
        elif option == 4:
            update_task()
        elif option == 5:
            delete_task()
        elif option == 6:
            print('Exit app')
        else:
            print('Invalid option')
    except:
        print('Invalid option')

def create_task():
    os.system('cls')
    print('Create Task\n')
    task_title = input('Title: ')
    task_description = input('Description: ')
    task.create(task={'title':task_title, 'description':task_description})

    input('Press any key to continue...')
    main()

def read_tasks():
    os.system('cls')
    print('Read tasks\n')
    task.read()
    main()

def read_task_by_id():
    os.system('cls')
    print('Read Task By ID\n')
    try:
        task_id = int(input('Task ID: '))
    except ValueError:
        print('ID must be a number!')
        return
    found_task = task.read_by_id(id=task_id)
    print(found_task)
    main()

def update_task():
    os.system('cls')
    print('Update Task\n')
    try:
        task_id = int(input('Task ID: '))
    except ValueError:
        print('ID must be a number')
        return
    
    task_title = input('Title: ')
    task_description = input('Description: ')

    if task_title == '' or task_description == '':
        print('All fields required')
        return
    
    task.update(id=task_id, task={'title':task_title, 'description':task_description})
    main()

def delete_task():
    os.system('cls')
    print('Delete Task')
    try:
        task_id = int(input('Task ID: '))
    except ValueError:
        print('ID must be a number')
        return
    task.delete(id=task_id)
    main()

def main():
    os.system('cls')
    main_menu()
    select_option()

main()
# delete_task()
# update_task()
# task.read()
# task.read_by_id(id=10)
# task.update(id=10, task={'title':'Estudar Python', 'description':'Fazer CRUD em JSON'})
# task.delete(id=10)