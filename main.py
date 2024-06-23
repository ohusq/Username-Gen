import modules.folderChecks as folderChecks  # Checks for directories to save in
import modules.saveToFile as saveToFile  # Saving to txt files that are stored in ./usernames
import os
from threading import Thread
import requests

roblox_api_username = 'https://auth.roblox.com/v1/usernames/validate?birthday=2013-05-04T00:00:00.000Z&context=Signup&username='

def check_username(username: str) -> None:
    """
    Checks the username with the Roblox API
    """
    try:
        request = requests.get(f"{roblox_api_username}{username.strip()}").json()
    except Exception as e:  # Something failed, can be anything
        print(f'Encountered an issue while sending a request,\nError: {e}')
        return

    if request.get('code') == 0:  # The username is valid, not used yet!
        saveToFile.valid(username)
    else:
        saveToFile.invalid(username)

def process_usernames(usernames: list) -> None:
    """
    Runs trough the list and checks every username
    """
    for username in usernames:
        check_username(username)

def get_file_lines(file: str) -> int:
    """
    Returns the total lines in a file
    """
    with open(file, 'r') as f:
        return len(f.readlines())

def main():
    """
    Main function for the script
    """
    folderChecks.setup_directories()  # setup for program, checks if all the files exist
    folderChecks.check_if_files_empty() # Checks if the files are empty

    if os.name != 'nt':
        print("Please use Windows / NT!")
        exit(1)
    
    os.system("title ohusq's Username Generator @ github.com/ohusq")
    print("Welcome to ohusq's username generator!")

    with open("check.txt", "r") as f:
        usernames = f.readlines()

    use_threads = input('Do you wish to use threads? (y/N)').strip().lower()
    if use_threads != 'y':
        print("Not using threads")
        print("Checking for usernames...")
        process_usernames(usernames)
    else:
        thread_amount = int(input('How many threads do you wish to use?\nAmount: ').strip())
        if thread_amount <= 0:
            print("Invalid number of threads. Exiting.")
            return

        # Split usernames into chunks for each thread
        chunk_size = len(usernames) // thread_amount
        threads = []

        for i in range(thread_amount):
            start_index = i * chunk_size
            end_index = None if i == thread_amount - 1 else (i + 1) * chunk_size
            thread_usernames = usernames[start_index:end_index]
            thread = Thread(target=process_usernames, args=(thread_usernames,))
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        print("All threads have completed processing.")
    print("Results:")
    print(f"\t- Invalid usernames: {get_file_lines('usernames\\invalid.txt')}")
    print(f"\t- Valid usernames: {get_file_lines('usernames\\valid.txt')}")
    print(f"\t- Total usernames: {get_file_lines('check.txt')}")

if __name__ == '__main__':
    main()
