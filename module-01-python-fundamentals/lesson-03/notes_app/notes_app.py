import os

print('Welcome to Notes!')

exit_confirmation = False

while exit_confirmation == False:

    operation = int(input("""Select an option:
                    1. Create a new note
                    2. View notes
                    3. Append to an existing note
                    4. Delete a note
                    5. Exit 
                    Please select the number of your intended option:
    """))

    if operation == 1:
        note_name = input('Please name your new note: ')
        note_content = input('Please type your note: ')
        with open(f"{note_name}.txt", "w") as f:
            f.write(note_content)
        print(f"{note_name}.txt has been created!")

    elif operation == 2:
        note_to_read = input('Please enter which note you want to view: ')
        if not os.path.exists(f"{note_to_read}.txt") or os.path.getsize(f"{note_to_read}.txt") == 0:
            print('No notes yet!')
        else:
            with open(f"{note_to_read}.txt", "r") as f:
                print("\n" + f.read() + "\n")

    elif operation == 3:
        note_to_append = input('Please enter which note you want to append: ')
        append_content = input('Please enter your appended content: ')
        with open(f"{note_to_append}.txt", "a") as f:
            f.write(f"\n{append_content}")
        print('Append has been added!')

    
    elif operation == 4:
        note_to_delete = input("Enter the name of the note you want to delete: ")
        filename = f"{note_to_delete}.txt"
        
        if not os.path.exists(filename):
            print("That note does not exist!")
        else:
            confirmation = input(f"Are you sure you want to delete {filename}? (Y/N): ")
            if confirmation.upper() == "Y":
                os.remove(filename)
                print(f"{filename} has been deleted!")
            else:
                print("Delete cancelled.")

    elif operation == 5:
        print('Goodbye!')
        exit_confirmation = True