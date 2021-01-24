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


def create_csv():
    '''
     opens txt created with all apropos, and creates csv
    '''
    all_apropos = open('all_apropos.txt', 'r')

    apropos_reader = all_apropos.read()

    with open('apropos_table.csv', 'w') as csvfile:
        fields = ['#', 'command', 'apropos']

        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writeheader()

        for i, apropo in enumerate(apropos_reader.splitlines()):
            writer.writerow({'#': i + 1, 'command': apropo.split(
                '-')[0], 'apropos': apropo.split('-')[1]})


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # list_commands_and_create_txt()
    # count_commands()
    # apropos_table()
    create_csv()
