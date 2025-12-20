USERS_FILE = "Users.txt"

def r_wFromFile(file_name, mode = "r", todos=None):
    '''Reads from or writes to ToDo.txt file based on mode parameter
    mode: "r" for read, "w" for write. It also requires the filepath as the file_name parameter.'''

    with open(file_name, mode) as file_local:
        match mode:
            case "r":
                return [line.strip() for line in file_local.readlines()]

            case "w":
                file_local.writelines([f'{todo}\n' for todo in todos])
                return todos

def checker(user_input, users_file=USERS_FILE):
    '''Checks if the username already exixts in a file or not. Returns True if it exists, False otherwise.'''

    with open(users_file, "r") as file_local:
        users = r_wFromFile(file_name=users_file, mode="r")
    if user_input in users:
        return True
    else:
        return False

if __name__ == "__main__":
    pr = "No Error\n run cli.py or gui.py to\
    use the To-Do application.".replace('    ', ' ')
    print(pr)