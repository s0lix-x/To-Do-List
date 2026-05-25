RED = "\033[91m"
WHITE = "\033[0m"

tasks = []

def display_menu():
    print("\n========== TO DO LIST ==========")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print(f"5. {RED}REMOVE ALL TASK!{WHITE}")
    print("6. Exit")

def add_task():
    task = input("Enter a new task: ")
    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append({
            "name": task,
            "done": False
        })
        print("Task added successfully!")
        
def show_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("Here are your tasks:")
        number = 1
        for i in tasks:
            if i["done"] == True:
                status = "[X]"
            else:
                status = "[ ]"
            print(f"{number}. {status} {i['name']}")
            number += 1

def remove_tasks():
    try:
        user_remove = int(input("What number do you want to remove? "))
        user_remove -= 1
        if user_remove in range(len(tasks)):
            print(f"Task has been removed")
            tasks.pop(user_remove)
        else:
            print(f"Task number {user_remove + 1} does not exist.")
    except:
        print("Invalid input.")

def remove_all_tasks():
    confirm = input("Are you sure? (y/n) ")
    if confirm.lower() == "y":
        print("All tasks have been removed")
        tasks.clear()
    else:
        print("Cancelled")

def mark_tasks():
    try:
        user_done = int(input("Which task number is completed? "))
        user_done -= 1
        if user_done in range (len(tasks)):
            tasks[user_done]["done"] = True
            print("Task marked as completed")
        else:
            print("Task number does not exist.")
    except:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose menu: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_tasks()
        elif choice == "4":
            mark_tasks()
        elif choice == "5":
            remove_all_tasks()
        elif choice == "6":
            print("Program closed")
            break
        else:
            print("Menu does not exist")

main()