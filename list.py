###--- IMPORTS ---###
import subprocess
import csv


###--- FUNCTIONS ---###
def list_commands_and_create_txt():
    '''
     lists all commands using running "compgen -c" command
     in terminal, and "writes" output into .txt file
    '''
    subprocess.run('compgen -c > all_commands.txt', shell=True)


def count_commands():
    '''
     counts all commands obtained form terminal
    '''
    with open('all_commands.txt', 'r') as all_commands_txt:
        commands_list = [
            command for command in all_commands_txt.read().splitlines()]
        print(len(commands_list))  # 2320


def apropos_table():
    '''
     reads `all_commands.txt` and creates table with
     each command's "apropos."
    '''

    all_commands = open('all_commands.txt', 'r')

    commands_reader = all_commands.read()

    apropos_commands = ''

    for command in commands_reader.splitlines():
        apropos_commands += f'{command} '

    subprocess.run(
        f'apropos {apropos_commands}>> all_apropos.txt', shell=True)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # list_commands_and_create_txt()
    # count_commands()
    apropos_table()
