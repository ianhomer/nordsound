from termcolor import colored

DEBUG = False

def error(s):
    print(colored("*** " + str(s) + " ***","red"))

def warn(s):
    print(colored("*** " + str(s),"red"))

def info(s):
    print(colored("... " + str(s),"green"))

def debug(s):
    if DEBUG:
        print("DEBUG : " + str(s))
