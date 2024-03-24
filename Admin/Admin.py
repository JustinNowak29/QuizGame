import time, sqlite3, AccountManagement, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class Admin:

    unsuccessfulLogInAttempt = 0

    def SignUp(self, username, password):
        
        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO Admiun VALUES (?,?,0,0,0)""", credentials,)

        conn.commit()
        conn.close()

    def LogIn(self, username, password, unsuccessfulLogInAttempt):

        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM Admin WHERE Username = ? AND Password = ?""", credentials,)
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
                admin1 = Admin()
                admin1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
    
    def SignInAndLogInProcess():

        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            admin1 = Admin()
            admin1.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            credentials = admin1.LogIn(username, password, Admin.unsuccessfulLogInAttempt)
            accountType = 'Admin'
            return accountType, credentials

        elif signOrLogOption == 2:

            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            credentials = admin1.LogIn(username, password, Admin.unsuccessfulLogInAttempt)
            accountType = 'Admin'
            return accountType, credentials

        else:
            
            MainModules.invalidInputModule()
            Admin.SignInAndLogInProcess()

Admin.SignInAndLogInProcess()

#use iteration if you want to do this below more than once
AccountManagement.spinaccountmanage()

print("uvfiesdgbfiawsdf")