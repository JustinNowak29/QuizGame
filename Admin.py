import time, sqlite3, AccountManagement

class Admin:

    unsuccessfulLogInAttempt = 0

    def SignUp(self, username, password):
        
        adminPass = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO Admin VALUES (?,?)""", adminPass,)

        conn.commit()
        conn.close()

    def LogIn(self, username, password, unsuccessfulLogInAttempt):
        import MainModules

        adminPass = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM Admin WHERE Username = ? AND Password = ?""", adminPass,)
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
                admin1 = Admin()
                admin1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
    
    def SignInAndLogInProcess():
        import MainModules

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
            admin1 = Admin()
            admin1.LogIn(username, password, Admin.unsuccessfulLogInAttempt)

        elif signOrLogOption == 2:

            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            admin1 = Admin()
            admin1.LogIn(username, password, Admin.unsuccessfulLogInAttempt)

        else:
            
            MainModules.invalidInputModule()
            Admin.SignInAndLogInProcess()

Admin.SignInAndLogInProcess()

#use iteration if you want to do this below more than once
AccountManagement.spinaccountmanage()

print("uvfiesdgbfiawsdf")