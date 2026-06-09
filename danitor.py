import os
from datetime import datetime, timezone
import sys

def progFunc():

    # USER-INPUT COMMANDS
    
    inst = input("Ready. ")

    # PARSE INPUT INTO SECTIONS (COMMANDS & ARGUMENTS
    
    instParts = inst.split(",")

    cmd = instParts[0]
    arg1 = None
    arg2 = None

    if len(instParts) > 1:
        arg1 = instParts[1]
    if len(instParts) > 2:
        arg2 = instParts[2]

    # UNCOMMENT THIS FOR DEBUGGING
    
    # print(cmd)
    # print(arg1)
    # print(arg2)
    
    # COMMAND EXECUTION

    if cmd.strip() == "time":
        if arg1 == None:
            arg1 = "0"
        if arg1.strip() == "12":
            print(datetime.now().strftime("%I:%M %p"))
        else:
            print(datetime.now().strftime("%H:%M"))
            
    if cmd.strip() == "exit":
        sys.exit()

    if cmd.strip() == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')

    if cmd.strip() == "about":
        print("MT PETER - My Test Python Executable To Enhance Readiness")
        print("Danitor 1.0")
        print("(c) 2026 Danny Aguero")
        print("You may find me on most social medias at @quenzartne.")
            
# LOOP
