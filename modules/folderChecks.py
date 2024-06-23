import os

# Use os.getcwd() to get the current working directory
current_directory = os.getcwd()
valid = os.path.join(current_directory, 'usernames', 'valid.txt')
invalid = os.path.join(current_directory, 'usernames', 'invalid.txt')
usernames = os.path.join(current_directory, 'usernames')
check = os.path.join(current_directory, 'check.txt')

def setup_directories() -> None:
    if not os.path.exists(usernames):
        os.mkdir(usernames)

    if not os.path.exists(valid):
        with open(valid, "w") as f:
            f.close()

    if not os.path.exists(invalid):
        with open(invalid, "w") as f:
            f.close()

def ask_to_continue(case: str) -> None:
    boolean = str(input(f"It seems '{case}' is not empty, would you like to continue?\nInput (y/N): ")).lower()
    
    if boolean == "" or boolean == "n":
        print("Exiting...")
        exit(0)
    else:
        print("Continuing without clearing the files.")

def check_if_files_empty() -> None:
    if not os.path.getsize(valid) == 0:
        ask_to_continue(".\\usernames\\valid.txt")

    if not os.path.getsize(invalid) == 0:
        ask_to_continue(".\\usernames\\invalid.txt")