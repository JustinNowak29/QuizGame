
import sqlite3, time, os, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class DeleteAccountClass:

    def deleteAnAccountGUI(self):
        print("""/------======------======------\         
|      Delete an Account!      |
\------======------======------/ """)

    def accountSelectionTypeModule(self):

        accountSelectionTypeOption = int(input("""/------======------======------\                              
|         Account Type         |
\------======------======------/
/------======------======------\ 
| Enter a specific Account     |
| type:                        |
| - User                   (1) |
| - Quiz Maker             (2) |
| - Return to Main Menu    (3) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/")
        
        if accountSelectionTypeOption >= 1 or accountSelectionTypeOption <= 3:
            return accountSelectionTypeOption         
        
        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return AccountObject.accountSelectionTypeModule()
        
    def accountNameSQL(self, accountSelectionTypeOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if accountSelectionTypeOption == 1:
            cursor.execute("""SELECT Username FROM User ORDER BY Username ASC""")

        elif accountSelectionTypeOption == 2:
            cursor.execute("""SELECT Username FROM QuizMaker ORDER BY Username ASC""")

        sqlOutput = list(cursor.fetchall())
        sqlOutput = list(dict.fromkeys(sqlOutput))
        conn.commit()
        conn.close()

        accountList = []
        accountDisplay = []

        for item in sqlOutput:

            tupleToStringConveter = (list(item)[0])
            accountDisplay.append("| - " + str(tupleToStringConveter))
            accountList.append(tupleToStringConveter)

        return accountDisplay, accountList

    def accountSelectionModule(self, accountDisplay, accountList):
        print("""/------======------======------\                              
|         Account List         |
\------======------======------/
/------======------======------\ 
| Enter a specific Account:    |""")
        for accountName in accountDisplay:
            print("| -                            |", end='\r')
            print(accountName)
        accountSelectionOption = input("""|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """)
        
        print("\------======------======------/")

        correctInputChecker = 0

        for quizListe in accountList:
            if accountSelectionOption == quizListe:
                correctInputChecker = 1

        if correctInputChecker != 1:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return AccountObject.accountSelectionModule(accountDisplay, accountList)
        
        return accountSelectionOption
    
    def countdown(self):

        value = 5
        for x in reversed(range(5)):
            time.sleep(1)
            os.system('cls')
            value -= 1
            print("""/------======------======------\                              
|           Confirm:     (""",value,""") |
\------======------======------/""")
            
        return value
    
    def confirmationModule(self):

        AccountObject.countdown()
        AccountObject.deleteAnAccountGUI()
        confirmationOption = int(input("""/------======------======------\ 
| Are you sure?                |
| - Yes                    (1) |
| - No                     (2) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/")

        if confirmationOption == 1:
            MainModules.loadingModule()
            return confirmationOption
        
        elif confirmationOption == 2:
            MainModules.loadingModule()    
            return AccountObject.AccountDeletionMainModule()

        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()    
            return AccountObject.confirmationModule()
        
    def accountDeletionSQL(self, accountSelectionTypeOptionn, accountSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if accountSelectionTypeOptionn == 1:
            cursor.execute("""DELETE FROM User WHERE Username = ?""", (accountSelectionOption,))

        elif accountSelectionTypeOptionn == 2:
            cursor.execute("""DELETE FROM QuizMaker WHERE Username = ?""", (accountSelectionOption,))

        conn.commit()
        conn.close()

    def accountDeletedGUI(self):

        AccountObject.deleteAnAccountGUI()
        print("""/------======------======------\                              
|       Account Deleted!       |
\------======------======------/""")
    
    def AccountDeletionMainModule(self):
        AccountObject = DeleteAccountClass()
                
        MainModules.loadingModule()
        accountSelectionTypeOption = AccountObject.accountSelectionTypeModule()
        stayInModule = accountSelectionTypeOption

        if stayInModule != 3:

            MainModules.loadingModule()
            accountDisplay, accountList = AccountObject.accountNameSQL(accountSelectionTypeOption)

            accountSelectionOption = AccountObject.accountSelectionModule(accountDisplay, accountList)
            
            MainModules.loadingModule()
            confirmationOption = AccountObject.confirmationModule()

            if confirmationOption == 1:

                MainModules.loadingModule()
                AccountObject.accountDeletionSQL(accountSelectionTypeOption, accountSelectionOption)

                AccountObject.accountDeletedGUI()
                MainModules.loadingModule()


#--------------------------------------------------------------
#--------------------------------------------------------------

AccountObject = DeleteAccountClass()
# AccountObject.AccountDeletionMainModule()

#--------------------------------------------------------------
#--------------------------------------------------------------