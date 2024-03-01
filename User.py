import time, sqlite3, MainModules

class User:

    unsuccessfulLogInAttempt = 0

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
                user1 = User()
                user1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
        
    def SignInAndLogInProcess():

        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:
            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1 = User()
            user1.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1 = User()
            user1.LogIn(username, password, User.unsuccessfulLogInAttempt)

        elif signOrLogOption == 2:
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            user1 = User()
            user1.LogIn(username, password, User.unsuccessfulLogInAttempt)

        else:
            MainModules.invalidInputModule()
            User.SignInAndLogInProcess()

    def userMainMenuOptions():
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
    
User.SignInAndLogInProcess()

mainMenuOptions = User.userMainMenuOptions()
if mainMenuOptions != -345:
    print("waiting...")
    MainModules.loadingModule()

elif mainMenuOptions == 4:
    exit()