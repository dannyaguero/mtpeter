import os
from datetime import datetime, timezone
import sys
import danitor as dt

os.system('cls' if os.name == 'nt' else 'clear')
print(" =============== ")
print("MT PETER - My Test Python Executable To Enhance Readiness")
print(" =============== ")
input("Press any key to continue")

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    selection = input("1. Load Danitor\n2. Exit\n")

    if selection.strip() == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        exitProg = 0
        while exitProg < 1:
            dt.progFunc()
    elif selection.strip() == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
