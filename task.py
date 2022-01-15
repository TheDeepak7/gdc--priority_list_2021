import sys


def print(x):
    sys.stdout.buffer.write(str(x + '\n').encode('utf8'))


def perform_ls(file="task.txt", work=1):
    try:
        with open(file, "r") as current:
            lines = current.readlines()
            indexes = sorted(range(len(lines)), key=lambda x: int(lines[x].split('^_^')[0]))

        index = 1

        for send in indexes:
            yeet = lines[send].split('^_^')
            print(
                str(index) + '. ' +
                yeet[1][:-1] + work * (' [' +
                yeet[0] + ']')
            )
            index += 1
    except FileNotFoundError:
        print("There are no pending tasks!")


if len(sys.argv) == 1 or sys.argv[1] == 'help':
    print(
        'Usage :-\n'
        '$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list\n'
        '$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n'
        '$ ./task del INDEX            # Delete the incomplete item with the given index\n'
        '$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n'
        '$ ./task help                 # Show usage\n'
        '$ ./task report               # Statistics'
    )

elif sys.argv[1] == 'add':
    try:
        with open("task.txt", "a") as current:
            current.write(
                str(sys.argv[2]) +
                '^_^' +
                str(sys.argv[3]) +
                '\n'
            )

        print(''.join(["Added task: \"", sys.argv[3], "\" with priority ", sys.argv[2]]))

    except IndexError:
        print("Error: Missing tasks string. Nothing added!")

elif sys.argv[1] == 'ls': perform_ls()

elif sys.argv[1] == 'del':
    try:
        del_index = int(sys.argv[2])

        with open("task.txt", "r") as current:
            lines = current.readlines()

        if len(lines) < del_index or del_index == 0:
            print(
                    "Error: task with index #" +
                    str(del_index) +
                    " does not exist. Nothing deleted."
            )

        else:
            indexes = sorted(range(1, len(lines)+1), key=lambda x: int(lines[x-1].split('^_^')[0]))

            open('task.txt', 'w').close()

            for i, e in enumerate(indexes):
                if e != del_index:
                    with open("task.txt", "a") as current:
                        current.write(lines[i])

            print("Deleted task #"+str(del_index))

    except IndexError:
        print("Error: Missing NUMBER for deleting tasks.")

elif sys.argv[1] == 'done':
    try:
        done_index = int(sys.argv[2])

        with open("task.txt", "r") as current:
            lines = current.readlines()

        if len(lines) < done_index or done_index == 0:
            print("Error: no incomplete item with index #" + str(done_index) + " exists.")

        else:
            indexes = sorted(range(1, len(lines)+1), key=lambda x: int(lines[x-1].split('^_^')[0]))
            open('task.txt', 'w').close()

            for i, e in enumerate(indexes):

                if e != done_index:
                    with open("task.txt", "a") as current:
                        current.write(lines[i])
                    current.close()

                else:
                    with open("completed.txt", "a") as done:
                        done.write(lines[i])
                    done.close()

            print("Marked item as done.")

    except IndexError:
        print("Error: Missing NUMBER for marking tasks as done.")

elif sys.argv[1] == 'report':
    with open("task.txt", "r") as pending:
        print('Pending : ' + str(len(pending.readlines())))
    perform_ls()

    with open("completed.txt", "r") as done:
        print('\nCompleted : ' + str(len(done.readlines())))
    perform_ls("completed.txt", 0)