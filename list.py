###--- IMPORTS ---###
import subprocess


###--- FUNCTIONS ---###
def list_commands_and_create_txt():
    all_commands = open('all_commands.txt', 'w+')
    subprocess.run('compgen -c', shell=True, stdout=all_commands)
    all_commands.close()


def count_commands():
    with open('all_commands.txt', 'r') as all_commands_txt:
        commands_list = [
            command for command in all_commands_txt.read().splitlines()]
        print(len(commands_list))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # list_commands_and_create_txt()
    count_commands()
