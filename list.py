###--- IMPORTS ---###
import subprocess
import csv


###--- FUNCTIONS ---###
def list_commands_and_create_txt():
    '''
     lists all commands using running "compgen -c" command
     in terminal, and "writes" output into .txt file
    '''
    all_commands = open('all_commands.txt', 'w+')
    subprocess.run('compgen -c', shell=True, stdout=all_commands)
    all_commands.close()


def count_commands():
    '''
     counts all commands obtained form terminal
    '''
    with open('all_commands.txt', 'r') as all_commands_txt:
        commands_list = [
            command for command in all_commands_txt.read().splitlines()]
        print(len(commands_list))


def apropos_table():
    '''
     reads `all_commands.txt` and creates table with
     each command's "apropos."
    '''

    fields = ['command', 'apropos']

    all_commands_txt = open('all_commands.txt', 'r')
    commands_reader = all_commands_txt.read().splitlines()

    with open('all_commands_apropos.csv', 'w+', newline='') as commands_csv:
        commands_csv_writer = csv.DictWriter(commands_csv, fieldnames=fields)

        commands_csv_writer.writeheader()

        for command in commands_reader:
            commands_csv_writer.writerows(
                [{'command': command, 'apropos': 'test'}])


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # list_commands_and_create_txt()
    # count_commands()
    apropos_table()
