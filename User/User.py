
import time, sqlite3, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')
sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame')

import MainModules, Play

class UserClass:

    unsuccessfulLogInAttempt = 0

    def userGUI(self):
        print("""/------======------======------\                              
|             User             |
\------======------======------/""")

    def SignUp(self, username, password):
        
        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO User VALUES (?,?,0,0,0)""", credentials,)

        conn.commit()
        conn.close()

    def LogIn(self, username, password, unsuccessfulLogInAttempt):

        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM User WHERE Username = ? AND Password = ?""", credentials,)
        logInAttempt =  cursor.fetchone()

        if logInAttempt:
            time.sleep(1)

            print("""/------======------======------\                              
|      Log In Successful!      |
\------======------======------/""")
            
            return credentials
            
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
                credentials = user1.LogIn(username, password, unsuccessfulLogInAttempt)
        
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
            credentials = user1.LogIn(username, password, UserClass.unsuccessfulLogInAttempt)
            accountType = 'User'
            return accountType, credentials

        elif signOrLogOption == 2:
            MainModules.loadingModule()

            user1.userGUI()
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1 = UserClass()
            credentials = user1.LogIn(username, password, UserClass.unsuccessfulLogInAttempt)
            accountType = 'User'
            return accountType, credentials
  
        else:
            MainModules.invalidInputModule()
            UserClass.SignInAndLogInProcess()

    def userMainMenuModule(self, accountType, credentials):

        MainModules.loadingModule()
        userObject.userGUI()

        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| - Play a Quiz!           (1) |
| - View Personal Stats    (2) |
| - About                  (3) |
| - Exit                   (4) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 

        if mainMenuOption == 1:

            QuizObject = Play.PlayQuizClass()
            QuizObject.PlayMainModule(accountType, credentials)
            return userObject.userMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 2:

            MainModules.loadingModule()
            MainModules.statisticsModule(accountType, credentials)
            return userObject.userMainMenuModule(accountType, credentials)

        elif mainMenuOption == 3:

            MainModules.loadingModule()
            MainModules.aboutModule()
            return userObject.userMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 4:
            exit()

        else:
            
            MainModules.invalidInputModule()
            return userObject.userMainMenuModule(accountType, credentials)    

userObject = UserClass()
accountType, credentials = userObject.SignInAndLogInProcess()
userObject.userMainMenuModule(accountType, credentials)