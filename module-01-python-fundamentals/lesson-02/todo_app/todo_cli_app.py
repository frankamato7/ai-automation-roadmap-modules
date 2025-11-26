
#Define and create a blank task list
tasks = []
#Welcome the user
menu = "Hello, welcome to your to-do list app!"
continue_option = True

while continue_option is True:
    #Give user an option to proceed
    menu_option = int(input(""" Please start by selecting an action (type the number):
    1. Add task
    2. View tasks
    3. Remove task
    4. Clear all tasks
    5. Exit
    """))

    #Add task execution
    if menu_option == 1:
        new_task = input("Please enter your new task: ")
        tasks.append(new_task)
        print(f"{new_task} has been added to your to-do list!")
    #View task(s) execution
    elif menu_option == 2:
        if len(tasks) != 0:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif len(tasks) == 0:
            print(f"You have no tasks yet!")
    #Remove task execution
    elif menu_option == 3:
            if len(tasks) != 0:
                remove_choice = int(input("Please select which task # you would like to remove: "))
                confirmation = input("Are you sure? (Y/N)")
                if confirmation == "Y":
                    tasks.pop(remove_choice-1)
                    print("Task removed!")
                elif confirmation == "N":
                    print("Task Removal cancelled")
            elif len(tasks) == 0:
                print('There are no tasks to remove!')
    #Clear all tasks execution
    elif menu_option == 4:
        tasks.clear()
        print('All tasks have been cleared!')
    #Exit operation
    elif menu_option == 5:
        print("Goodbye!")
        continue_option = False
