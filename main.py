from pathlib import Path
import os
from datetime import datetime, timezone
import sys
import danitor as dt
import linecache
import user

newcfg = Path(".config")
newcfg.touch(exist_ok=True)

os.system('cls' if os.name == 'nt' else 'clear')
user.userFunc()
print(" =============== ")
print("MT PETER - My Test Python Executable To Enhance Readiness")
print(" =============== ")
input("Press any key to continue")

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    selection = input("1. Load Danitor\n2. Load Measurement Executable Gateway (UNAVAILABLE)\n3. Change Username\n4. Exit\n")

    if selection.strip() == "1":
        print("Loading Danitor...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("DANITOR 1.0 - 2026 Danny Aguero")
        exitProg = 0
        while exitProg < 1:
            dt.progFunc()
            
    elif selection.strip() == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("MEG is currently not available.")


    elif selection.strip() == "3":
        user.userChg()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Username changed successfully.")

    elif selection.strip() == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
