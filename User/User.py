import time, sqlite3, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/VisualStudio/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class UserClass:

    unsuccessfulLogInAttempt = 0

    def userGUI(self):
        print("""/------======------======------\                              
|             User             |
\------======------======------/""")


    def SignUp(self, username, password):
        
        userPass = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO User VALUES (?,?)""", userPass,)

        conn.commit()
        conn.close()

    def LogIn(self, username, password, unsuccessfulLogInAttempt):

        userPass = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM User WHERE Username = ? AND Password = ?""", userPass,)
        logInAttempt =  cursor.fetchone()

        if logInAttempt:
            time.sleep(1)

            print("""/------======------======------\                              
|      Log In Successful!      |
\------======------======------/""")
            
        else:

            if unsuccessfulLogInAttempt > 2:
                print("""/------======------======------\                              
|   To many failed attempts!   |
|      Program Shutdown..      |
\------======------======------/""")
                
                MainModules.loadingModule()

            else: 
                time.sleep(1)
                print("""/------======------======------\                              
|    Log In Unsuccessful...    |
|          Try Again!          |
\------======------======------/""")
                
                MainModules.loadingModule()

                unsuccessfulLogInAttempt += 1
                username = MainModules.enterUsername()
                password = MainModules.enterPassword()
                user1 = UserClass()
                user1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
        
    def SignInAndLogInProcess(self):
        user1 = UserClass()

        MainModules.loadingModule()
        user1.userGUI()

        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            user1.userGUI()
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1.LogIn(username, password, UserClass.unsuccessfulLogInAttempt)

        elif signOrLogOption == 2:
            MainModules.loadingModule()

            user1.userGUI()
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1 = UserClass()
            user1.LogIn(username, password, UserClass.unsuccessfulLogInAttempt)

        else:
            MainModules.invalidInputModule()
            UserClass.SignInAndLogInProcess()

    def userMainMenuModule(self):

        MainModules.loadingModule()
        user1.userGUI()
        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| - Play a Quiz!           (1) |
| - View Statistics        (2) |
| - About                  (3) |
| - Exit                   (4) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 
        return mainMenuOption
    
user1 = UserClass()
user1.SignInAndLogInProcess()
user1.userMainMenuModule()


mainMenuOptions = user1.userMainMenuModule()
if mainMenuOptions != -345:
    print("waiting...")
    MainModules.loadingModule()

elif mainMenuOptions == 4:
    exit()