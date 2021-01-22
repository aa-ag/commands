###--- IMPORTS ---###
import subprocess


###--- FUNCTIONS ---###
def list_commands_and_create_txt():
    all_commands = open('all_commands.txt', 'w+')
    subprocess.run('compgen -c', shell=True, stdout=all_commands)
    all_commands.close()


def count_commands():
    with open('all_commands.txt', 'r') as ac:
        commands_list = [i for i in ac.read().splitlines()]
        print(len(commands_list))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # list_commands_and_create_txt()
    count_commands()
