#!/usr/bin/env python3
#Author: Darryl Beckham

import os
import sys
import json # Consider using for file contents io

class Task(object):
    def __init__(self, name, desc):
        self.contents['name'] = name
        self.contents['description'] = desc
    
    saved = False
    contents = {'name': None, 'description': None, 'due': None, 'priority': None, 'estimated_duration': None}
    
    def get_optional_data(self):
        print("Select one of the following to enter additional information or press Enter to continue: ")
        print("1. Due")
        print("2. Priority")
        print("3. Estimated Duration")
        select = str(input("Selection: "))
        for i in range(len(self.contents) - 2):
            if select == '1':
                self.contents['due'] = str(input("Enter due date: "))
                continue
            elif select == '2':
                self.contents['priority'] = str(input("Enter priority: "))
                continue
            elif select == '3':
                self.contents['Estimated duration'] = str(input("Enter estimated duration: "))
                continue
            else:
                break

filename = "/home/darrylb/darrylbckhm/mytasks.txt"
old_tasks = []
new_tasks = []

def create_task(name, desc):
    global new_tasks
    global old_tasks
    new_tasks.append(Task(name, desc))
    new_tasks[-1].get_optional_data()

def save_tasks(filename):
    global old_tasks
    global new_tasks
    found = False
    if not new_tasks:
        print("Tasks up to date!")
    else:
        with open(filename, 'a') as f:
            for new_task in new_tasks:
                for old_task in old_tasks:
                    if new_task.contents['name'] == old_task.contents['name']:
                        found = True
                        print("Task already exists!")
                if not found:
                    json.dump(new_task.contents, f)
                    f.write('\n')
                    new_task.saved = True
                found = False
        f.close()

def load_tasks(filename):
    global old_tasks
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            contents = f.read().splitlines()
            for line in contents:
                line = json.loads(line)
                old_tasks.append(Task(None, None))
                for key in line:
                    old_tasks[-1].contents[key] = line[key]
        f.close()
    else:
        print("No current task file!")

def search_tasks(string):
    for task in tasks:
        for key in task:
            if key == string:
                print(task)
            if not task[key]:
                continue
            elif task[key].find(string):
                print(task)

def update_task(name, key):
    for task in tasks:
        if task[name]:
            if task[key]:
                task[key] = str(input("Update", key, "in", name))
            else:
                print("Invalid key!")
        else:
            print("Task not found!")

def delete_task(name):
    global old_tasks
    global new_tasks
    found = False
    for old_task in old_tasks:
        if name == old_task[name]:
            found = True
            del old_task
            print(name, "has been deleted!")
            break
    for new_task in new_tasks:
        if name == new_task[name]:
            found = True
            del new_task
            print(name, "has been deleted!")
            break
    if not found:
        print("Task was not found!")

def print_tasks():
    global old_tasks
    global new_tasks

    for old_task in old_tasks:
        print(old_task.contents)

    for new_task in new_tasks:
        if new_task.saved == True:
            print(new_task.contents)

    for new_task in new_tasks:
        if new_task.saved == False:
            print("Unsaved: ", new_task.contents)

def menu():
    print("1. Create New Task")
    print("2. Search For Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Save tasks")
    print("6. Print tasks")
    print("7. Quit")
    get_user_selection()

def get_user_selection():
    while True:
        select = str(input("What would you like to do? "))
        if select == '1':
            name = str(input("Task name: "))
            desc = str(input("Task description: "))
            create_task(name, desc)
        elif select == '2':
            string = str(input("Keyword: "))
            search_tasks(string)
        elif select == '3':
            name = str(input("Task name: "))
            key = str(input("Field: "))
            update_task(name, key)
        elif select == '4':
            name = str(input("Task name: "))
            delete_task(name)
        elif select == '5':
            save_tasks(filename)
        elif select == '6':
            print_tasks()
        elif select == '7':
            sys.exit(0)
        menu()

if __name__ == "__main__":
    load_tasks(filename)
    menu()
