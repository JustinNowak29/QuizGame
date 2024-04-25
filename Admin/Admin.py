
import time, sqlite3, sys, AccountDeletion, AccountStatistics

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')
sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame')

import MainModules, Play

class AdminClass:

    unsuccessfulLogInAttempt = 0

    def adminGUI(self):
        print("""/------======------======------\                              
|            Admin             |
\------======------======------/""")

    def SignUp(self, username, password):
        
        credentials = username, password
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO Admin VALUES (?,?,0,0,0)""", credentials,)

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
                admin1 = AdminClass()
                admin1.LogIn(username, password, unsuccessfulLogInAttempt)
        
        conn.commit()
        conn.close()
    
    def SignInAndLogInProcess(self):

        MainModules.loadingModule()
        signOrLogOption = MainModules.signOrLogOptions()

        if signOrLogOption == 1:

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            AdminObject.SignUp(username, password)
            time.sleep(1)

            print("""/------======------======------\                              
|       Sign Up Complete       |
\------======------======------/""")
            
            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            credentials = AdminObject.LogIn(username, password, AdminClass.unsuccessfulLogInAttempt)
            accountType = 'Admin'
            return accountType, credentials

        elif signOrLogOption == 2:

            MainModules.loadingModule()

            username = MainModules.enterUsername()
            password = MainModules.enterPassword()
            credentials = AdminObject.LogIn(username, password, AdminClass.unsuccessfulLogInAttempt)
            accountType = 'Admin'
            return accountType, credentials

        else:
            
            MainModules.invalidInputModule()
            AdminObject.SignInAndLogInProcess()

    def AdminMainMenuModule(self, accountType, credentials):
        AdminObject = AdminClass()

        MainModules.loadingModule()
        AdminObject.adminGUI()

        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| Account Management           |
| - Edit Accounts          (1) |
| - Delete Accounts        (2) |
| - View all Player Stats  (3) |
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
            pass
        
        elif mainMenuOption == 2:
                        
            AccountObject = AccountDeletion.DeleteAccountClass()
            AccountObject.AccountDeletionMainModule()
            return AdminObject.AdminMainMenuModule(accountType, credentials)

        elif mainMenuOption == 3:

            AccountObject = AccountStatistics.ViewAccountStatsClass()
            AccountObject. AccountStatisticsMainModule()
            return AdminObject.AdminMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 4:

            QuizObject = Play.PlayQuizClass()
            QuizObject.PlayMainModule(accountType, credentials)
            return AdminObject.AdminMainMenuModule(accountType, credentials)

        elif mainMenuOption == 5:

            MainModules.loadingModule()
            MainModules.statisticsModule(accountType, credentials)
            return AdminObject.AdminMainMenuModule(accountType, credentials)

        elif mainMenuOption == 6:

            MainModules.loadingModule()
            MainModules.aboutModule()
            return AdminObject.AdminMainMenuModule(accountType, credentials)
        
        elif mainMenuOption == 7:
            exit()

        else:
            
            MainModules.invalidInputModule()
            return AdminObject.AdminMainMenuModule(accountType, credentials)

AdminObject = AdminClass()
accountType, credentials = AdminObject.SignInAndLogInProcess()
AdminObject.AdminMainMenuModule(accountType, credentials)

# #use iteration if you want to do this below more than once
# AccountManagement.spinaccountmanage()