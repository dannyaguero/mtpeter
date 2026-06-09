import os
import linecache

def userFunc():

    os.chmod(".config", 0o666)
    global cfgfile
    cfgfile = ".config"
    preuser = ""
    global username
    username= ""
    
    if os.path.exists(cfgfile):
        with open(cfgfile, "r") as file:
            for line in file:
                if "USER:" in line:
                    preuser = (line.strip())
                    username = preuser.replace("USER:", "")

    if not username:
        username = input("Please enter a username: ")
    
        with open(cfgfile, "w") as file:
            file.write("USER: " + username)
            print("Welcome, " + username.strip() + "!")
    else:
        print("Welcome back," + username + "!")

def userChg():

    os.chmod(".config", 0o666)
    username = ""
    preuser = ""
    cfgtemp = ""
    
    if os.path.exists(cfgfile):
        username = input("Please enter a new username: ")
        with open(cfgfile, "r") as file:
            cfgtemp = file.readlines()
            
        for index, line in enumerate(cfgtemp):
            if "USER:" in line:
                cfgtemp[index] = "USER: " + username

            with open(cfgfile, "w") as file:
                file.writelines(cfgtemp)
                
    if not username:
        username = input("Please enter a new username: ")
        with open(cfgfile, "r") as file:
            cfgtemp = file.readlines()
            
        for index, line in enumerate(cfgtemp):
            if "USER:" in line:
                cfgtemp[index] = "USER: " + username

            with open(cfgfile, "w") as file:
                file.writelines(cfgtemp)
