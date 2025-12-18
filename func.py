def r_wFromFile(file_name, mode = "r", todos=[]):
    '''Reads from or writes to ToDo.txt file based on mode parameter
    mode: "r" for read, "w" for write'''

    with open(file_name, mode) as file_local:
        match mode:
            case "r":
                todos = file_local.readlines()
                return todos
            case "w":
                file_local.writelines(todos)
                return todos

if __name__ == "__main__":
    pr = "No Error\n run cli.py or gui.py to\
    use the To-Do application.".replace('    ', ' ')
    print(pr)