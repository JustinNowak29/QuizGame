import time, os
from subprocess import call

def openUserPythonFile():
        call(["python", "User.py"])

def openQuizMakerPythonFile():
        call(["python", "QuizMaker.py"])

def openAdminPythonFile():
        call(["python", "Admin.py"])

def loadingModule():
    time.sleep(1)
    for i in range(5):
        for i in '/—\\|':
            time.sleep(0.1)
            print('\b'+i, end = '', flush=True)
    print('\b', end = '')
    os.system('cls')

def invalidInputModule():
    print("""/------======------======------\ 
| Input isn't valid, try again |
\------======------======------/""")

def accountOptionModule():
    accountOption = int(input("""/------======------======------\                              
|   Choose your Account Type   |
\------======------======------/
/------======------======------\ 
| - User                   (1) |
| - QuizMaker              (2) |
| - Administrator          (3) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
    print("\------======------======------/")

    if accountOption == 1:
        openUserPythonFile()
    elif accountOption == 2:
        openQuizMakerPythonFile()
    elif accountOption  == 3:
        openAdminPythonFile()
    else:
        print("""/------======------======------\ 
| Input isn't valid, try again |
\------======------======------/""")
        
        loadingModule()
        accountOptionModule()

def signOrLogOptions():
    loadingModule()
    
    print('\b', end = '')
    signOrLogOption = int(input("""/------======------======------\                              
|      Sign Up or Log In?      |
\------======------======------/
/------======------======------\ 
| - Sign Up                (1) |
| - Log In                 (2) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
    print("\------======------======------/") 
    return signOrLogOption

def enterUsername():
    username = input("""/------======------======------\                              
| - Enter a Username:          |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """)
    return username

def enterPassword():
    password = input("""|                              |
| - Enter a Password:          |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """)
    print("\------======------======------/")
    return password


# +------======------======------+
# | Choose amount of XP Given:   |
# | - 5 XP                   (1) |
# | - 10 XP                  (2) |
# | - 20 XP                  (3) |
# |                              |
# |  __________________________  |"""