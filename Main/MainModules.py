import time, os, sqlite3
from subprocess import call

def openGuestPythonFile():
        call(["python", "Guest/Guest.py"])

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
| - Guest                  (1) |
| - User                   (2) |
| - QuizMaker              (3) |
| - Administrator          (4) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
    print("\------======------======------/")

    if accountOption == 1:
        openGuestPythonFile()
    elif accountOption == 2:
        openUserPythonFile()
    elif accountOption == 3:
        openQuizMakerPythonFile()
    elif accountOption  == 4:
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

def statisticsModule(accountType, credentials):

    username = str(credentials[0])
    password = str(credentials[1])

    conn = sqlite3.connect('QuizGameDataBase.db')
    cursor = sqlite3.Cursor(conn)

    # note for self: the code below is probably VERY reduntant, but I can't find a solution atm, come back to this later
    if accountType == 'User':
        cursor.execute("""SELECT * FROM User WHERE Username = ? AND Password = ?""",(username, password))

    elif accountType == 'QuizMaker':
        cursor.execute("""SELECT * FROM QuizMaker WHERE Username = ? AND Password = ?""",(username, password))
            
    elif accountType == 'Admin':
        cursor.execute("""SELECT * FROM Admin WHERE Username = ? AND Password = ?""",(username, password))

    sqlOutput = cursor.fetchall()[0]

    conn.commit()
    conn.close()

    print("""/------======------======------•------======------======------\                           
|                  Your Personal Statistics!                  |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Take a look...                                              |""")

    checkingAccountStatsList = ["""| Username: """+str(sqlOutput[0]),
        """| Password: """+str(sqlOutput[1]),
        """| """,
        """| Total XP: """+str(sqlOutput[2]),
        """| Quizzes Answered: """+str(sqlOutput[3]),
        """| Quizzes Answered Perfectly: """+str(sqlOutput[4])]

    for item in checkingAccountStatsList:
        print("""|                                                             |""", end='\r')
        print(item)
        
    input("""/------======------======------•------======------======------\                           
|                   Press any key to return                   |
\------======------======------•------======------======------/ """)
    
def aboutModule():
    print("""/------======------======------•------======------======------\                           
|                            About                            |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Welcome to the QuizGame!                                    |
|                                                             |
| Test your knowledge with our challenging trivia questions,  |
| about various topics and subjects. You will be able to gain |
| XP points if you answer the questions correctly, so make    |
| sure to gain as much points as possible!                    |
|                                                             |
| Have fun!                                                   |
\------======------======------•------======------======------/""")
            
    input("""/------======------======------•------======------======------\                           
|                   Press any key to return                   |
\------======------======------•------======------======------/ """)
     