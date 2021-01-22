###--- IMPORTS ---###
import os


###--- FUNCTIONS ---###
def list_commands_and_create_txt():
    os.system('compgen -c')


###--- DRIVER CODE ---###
if __name__ == "__main__":
    list_commands_and_create_txt()
