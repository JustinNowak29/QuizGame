import sqlite3, time, os, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class ViewAccountStatsClass:

    def viewAccountStatsGUI(self):
        print("""/------======------======------\         
|   View an Account's Stats!   |
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
    
    def statisticsModule(self, accountSelectionTypeOption, accountSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        # note for self: the code below is probably VERY reduntant, but I can't find a solution atm, come back to this later
        if accountSelectionTypeOption == 1:
            cursor.execute("""SELECT * FROM User WHERE Username = ?""",(accountSelectionOption,))

        elif accountSelectionTypeOption == 2:
            cursor.execute("""SELECT * FROM QuizMaker WHERE Username = ?""",(accountSelectionOption,))

        sqlOutput = cursor.fetchall()[0]

        conn.commit()
        conn.close()

        print("""/------======------======------•------======------======------\ """) 
        print("""|                                                             |""", end='\r')
        print("| "+accountSelectionOption+"""'s Statistics:
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Take a look...                                              |""")

        checkingAccountStatsList = ["""| Username: """+str(sqlOutput[0]),
            """| Password: """+str(sqlOutput[1]),
            """| """,
            """| Total XP: """+str(sqlOutput[2]),
            """| Quizzes Answered: """+str(sqlOutput[3]),
            """| Quizzes Answered Perfectly: """+str(sqlOutput[4])]

        for item in checkingAccountStatsList:
            print("""|                                                             |""", end='\r')
            print(item)
            
        input("""/------======------======------•------======------======------\                           
|                   Press any key to return                   |
\------======------======------•------======------======------/ """)

    def AccountStatisticsMainModule(self):
            AccountObject = ViewAccountStatsClass()
                    
            MainModules.loadingModule()
            accountSelectionTypeOption = AccountObject.accountSelectionTypeModule()
            stayInModule = accountSelectionTypeOption

            if stayInModule != 3:

                MainModules.loadingModule()
                accountDisplay, accountList = AccountObject.accountNameSQL(accountSelectionTypeOption)

                accountSelectionOption = AccountObject.accountSelectionModule(accountDisplay, accountList)
                
                MainModules.loadingModule()
                AccountObject.statisticsModule(accountSelectionTypeOption, accountSelectionOption)




                # confirmationOption = AccountObject.confirmationModule()

                # if confirmationOption == 1:

                #     MainModules.loadingModule()
                #     AccountObject.accountDeletionSQL(accountSelectionTypeOption, accountSelectionOption)

                #     AccountObject.accountDeletedGUI()
                #     MainModules.loadingModule()


#--------------------------------------------------------------
#--------------------------------------------------------------

AccountObject = ViewAccountStatsClass()
# AccountObject.AccountStatisticsMainModule()

#--------------------------------------------------------------
#--------------------------------------------------------------