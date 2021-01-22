###--- IMPORTS ---###
import subprocess


###--- FUNCTIONS ---###
def list_commands_and_create_txt():
    all_commands = open('all_commands', 'w+')
    subprocess.run('compgen -c', shell=True, stdout=all_commands)
    all_commands.close()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    list_commands_and_create_txt()
