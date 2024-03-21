import time, sqlite3, MainModules, QuizCreation, QuizDeletion

class QuizMakerClass:

    unsuccessfulLogInAttempt = 0

    def SignUp(self, username, password):
        quizMakerPass = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO QuizMaker VALUES (?,?)""", quizMakerPass,)

        conn.commit()
        conn.close()

    def LogIn(self, username, password, unsuccessfulLogInAttempt):
        quizMakerPass = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM QuizMaker WHERE Username = ? AND Password = ?""", quizMakerPass,)
        logInAttempt =  cursor.fetchone()

        if logInAttempt:
            time.sleep(1)

            print("""/------======------======------\                              
|      Log In Successful!      |
\------======------======------/""")
            
            MainModules.loadingModule()
            
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
                quizMaker1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
    
    def SignInAndLogInProcess(self):
        quizMakerObject = QuizMakerClass()
        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMakerObject = QuizMakerClass()
            quizMakerObject.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMakerObject = QuizMakerClass()
            quizMakerObject.LogIn(username, password, QuizMakerClass.unsuccessfulLogInAttempt)

        elif signOrLogOption == 2:
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMakerObject = QuizMakerClass()
            quizMakerObject.LogIn(username, password, QuizMakerClass.unsuccessfulLogInAttempt)

        else:
            MainModules.invalidInputModule()
            QuizMakerClass.SignInAndLogInProcess()

    def quizMakerMainMenuModule(self):
        quizMakerObject = QuizMakerClass()
        MainModules.loadingModule()
        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| - Create a Quiz          (1) |
| - Manage a Quiz          (2) |
| - Delete a Quiz          (3) |
| - Test a Quiz            (4) |
| - Exit                   (5) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 

        if mainMenuOption == 1:

            QuizObject = QuizCreation.CreateQuizClass()
            QuizObject.QuizCreationMainModule()
            return quizMakerObject.quizMakerMainMenuModule()
        
        elif mainMenuOption == 2:
            pass

        elif mainMenuOption == 3:

            QuizObject = QuizDeletion.DeleteQuizClass()
            QuizObject.QuizDeletionMainModule()
            return quizMakerObject.quizMakerMainMenuModule()
        # plan:
        # ask if quiz is mult choice or user input
        # allow user to choose a specific quiz
        # ask whether they want to change quiz content or the quiz settings

        elif mainMenuOption == 5:
            exit()


        else:
            
            print("! not finished !")
            MainModules.invalidInputModule()
            quizMakerObject.quizMakerMainMenuModule()    

quizMakerObject = QuizMakerClass()
quizMakerObject.SignInAndLogInProcess()
quizMakerObject.quizMakerMainMenuModule()
