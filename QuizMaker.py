import time, sqlite3, MainModules, QuizConfiguration, QuizObject

class QuizMaker:

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
                quizMaker1 = QuizMaker()
                quizMaker1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
    
    def SignInAndLogInProcess():
        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMaker1 = QuizMaker()
            quizMaker1.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMaker1 = QuizMaker()
            quizMaker1.LogIn(username, password, QuizMaker.unsuccessfulLogInAttempt)

        elif signOrLogOption == 2:
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            quizMaker1 = QuizMaker()
            quizMaker1.LogIn(username, password, QuizMaker.unsuccessfulLogInAttempt)

        else:
            MainModules.invalidInputModule()
            QuizMaker.SignInAndLogInProcess()

QuizMaker.SignInAndLogInProcess()
quizName, quizDifficulty, questionLength, quizType = QuizConfiguration.QuizConfiguartion()
QuizObject = QuizObject.Quiz.quizCreationModule(quizName, quizDifficulty, questionLength, quizType)