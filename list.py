###--- IMPORTS ---###
import os
import sys
import platform
import settings


###--- FUNCTIONS ---###
def user_name():
    print(os.name)
    print(sys.platform)
    print(platform.system())


###--- DRIVER CODE ---###
if __name__ == "__main__":
    user_name()
