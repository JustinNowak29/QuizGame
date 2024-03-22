import time, os
from subprocess import call

def openUserPythonFile():
        call(["python", "User/User.py"])

def openQuizMakerPythonFile():
        call(["python", "QuizMaker/QuizMaker.py"])

def openAdminPythonFile():
        call(["python", "Admin/Admin.py"])

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

def scorePercentageToMessageConveter(percentage):

    if percentage == 0:
        message = "You got nothing? Seriously???"
    elif percentage <= 10 and percentage > 0:
        message = "You need to catch up on a lot."
    elif percentage <= 20 and percentage > 10:
        message = "That's worriyng..."
    elif percentage <= 30 and percentage > 20:
        message = "Better luck next time!"
    elif percentage <= 40 and percentage > 30:
        message = "Meh."
    elif percentage <= 50 and percentage > 40:
        message = "It's okay, not good, not bad."
    elif percentage <= 60 and percentage > 50:
        message = "Nice"
    elif percentage <= 70 and percentage > 60:
        message = "That's good"
    elif percentage <= 80 and percentage > 70:
        message = "Great!"
    elif percentage <= 90 and percentage > 80:
        message = "You know what you're doing B)"
    elif percentage < 100 and percentage > 90:
        message = "I'm proud :)"
    elif percentage == 100:
        message = "Perfect Score!!!"

    return message

     


# +------======------======------+
# | Choose amount of XP Given:   |
# | - 5 XP                   (1) |
# | - 10 XP                  (2) |
# | - 20 XP                  (3) |
# |                              |
# |  __________________________  |"""