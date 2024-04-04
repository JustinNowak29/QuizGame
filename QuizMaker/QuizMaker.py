
import time, sqlite3, QuizCreation, QuizDeletion, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')
sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame')

import MainModules, Play


class QuizMakerClass:

    unsuccessfulLogInAttempt = 0

    def quizMakerGUI(self):
        print("""/------======------======------\                              
|          Quiz Maker          |
\------======------======------/""")

    def SignUp(self, username, password):
        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO QuizMaker VALUES (?,?,0,0,0)""", credentials,)

        conn.commit()
        conn.close()

    def LogIn(self, username, password, unsuccessfulLogInAttempt):
        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM QuizMaker WHERE Username = ? AND Password = ?""", credentials,)
        logInAttempt =  cursor.fetchone()

        if logInAttempt:
            time.sleep(1)

            print("""/------======------======------\                              
|      Log In Successful!      |
\------======------======------/""")
            
            MainModules.loadingModule()
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
                quizMaker1 = QuizMakerClass()
                credentials = quizMaker1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
    
    def SignInAndLogInProcess(self):
        quizMakerObject = QuizMakerClass()

        MainModules.loadingModule()

        quizMakerObject.quizMakerGUI()
        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMakerObject.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            quizMakerObject.quizMakerGUI()
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            credentials = quizMakerObject.LogIn(username, password, QuizMakerClass.unsuccessfulLogInAttempt)
            accountType = 'QuizMaker'
            return accountType, credentials

        elif signOrLogOption == 2:

            MainModules.loadingModule()

            quizMakerObject.quizMakerGUI()
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMakerObject = QuizMakerClass()
            credentials = quizMakerObject.LogIn(username, password, QuizMakerClass.unsuccessfulLogInAttempt)
            accountType = 'QuizMaker'
            return accountType, credentials

        else:

            quizMakerObject.quizMakerGUI()
            MainModules.invalidInputModule()
            QuizMakerClass.SignInAndLogInProcess(self)

    def quizMakerMainMenuModule(self, accountType, credentials):

        MainModules.loadingModule()
        quizMakerObject.quizMakerGUI()

        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| Quiz Management              |
| - Create a Quiz          (1) |
| - Manage a Quiz          (2) |
| - Delete a Quiz          (3) |
|                              |
| Default Options              |
| - Play a Quiz            (4) |
| - View Personal Stats    (5) |
| - About                  (6) |
| - Exit                   (7) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 

        if mainMenuOption == 1:

            QuizObject = QuizCreation.CreateQuizClass()
            QuizObject.QuizCreationMainModule()
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 2:
            
            print("not added yet!")
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials)

        elif mainMenuOption == 3:

            QuizObject = QuizDeletion.DeleteQuizClass()
            QuizObject.QuizDeletionMainModule()
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 4:

            QuizObject = Play.PlayQuizClass()
            QuizObject.PlayMainModule(accountType, credentials)
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials)
        
        # plan:
        # ask whether they want to change quiz content or the quiz settings

        elif mainMenuOption == 5:

            MainModules.loadingModule()
            MainModules.statisticsModule(accountType, credentials)
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials)

        elif mainMenuOption == 6:

            MainModules.loadingModule()
            MainModules.aboutModule()
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 7:
            exit()

        else:
            
            MainModules.invalidInputModule()
            return quizMakerObject.quizMakerMainMenuModule(accountType, credentials) 

quizMakerObject = QuizMakerClass()
accountType, credentials = quizMakerObject.SignInAndLogInProcess()
quizMakerObject.quizMakerMainMenuModule(accountType, credentials)
