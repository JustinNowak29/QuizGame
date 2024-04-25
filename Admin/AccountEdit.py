
import sqlite3, time, os, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class EditAccountClass:

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
        
    def accountFeaturesModule(self):

        accountFeaturesOption = int(input("""/------======------======------\                              
|       Account Features       |
\------======------======------/
/------======------======------\       
| Edit Account Credentials     |
| - Username               (X) |
| - Password               (X) |
|                              |
| Edit Account Statistics      |
| - Total XP               (X) |
| - Quizzes Answered       (X) |
| - Quizzes Answered           |
|   Perfectly              (X) |
| - Wipe all Stats         (6) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/")
        
        if accountFeaturesOption >= 1 or accountFeaturesOption <= 6:
            return accountFeaturesOption  

        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return AccountObject.quizFeaturesModule()
        
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
    
    def confirmationModule(self, accountSelectionTypeOption, accountSelectionOption):

        AccountObject.countdown()
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
            AccountObject.accountStatsDeletionSQL(accountSelectionTypeOption, accountSelectionOption)
            return confirmationOption
        
        elif confirmationOption == 2:
            MainModules.loadingModule()    
            return AccountObject.AccountEditMainModule()

        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()    
            return AccountObject.confirmationModule()

    def accountStatsDeletionSQL(self, accountSelectionTypeOption, accountSelectionOption):

            conn = sqlite3.connect('QuizGameDataBase.db')
            cursor = sqlite3.Cursor(conn)

            if accountSelectionTypeOption == 1:
                cursor.execute("""UPDATE User SET XP = 0, QuizzesAnswered = 0, QuizzesAnsweredPerfectly = 0 WHERE Username = ?""", (accountSelectionOption,))

            elif accountSelectionTypeOption == 2:
                cursor.execute("""UPDATE QuizMaker SET XP = 0, QuizzesAnswered = 0, QuizzesAnsweredPerfectly = 0 WHERE Username = ?""", (accountSelectionOption,))

            conn.commit()
            conn.close()

#     def editUserInputQuizModule(self, questionAmount, quizSelectionOption):

#         print("this doesn't work!!!")
#         print("this doesn't work!!!")
#         print("this doesn't work!!!")

#         for x in range(questionAmount):
        
#             QuizObject.editAQuizGUI2()
#             questionUserInput = input("""| Be Creative! (Maxiumum Character Length is 56)              |      
# |                                                             |
# |  _________________________________________________________  |
# \------======------======------+------======------======------/\x1B[1F\r| """)
#             print("\------======------======------+------======------======------/")

#             if len(questionUserInput) > 56:
#                 print("""/------======------======------\                              
# |  Input exceeds 56 Character  |
# |       Limit, Try Again       |
# \------======------======------/""")
            
#                 MainModules.loadingModule()
#                 return QuizObject.editUserInputQuizModule()

#             else:
#                 answerUserInput = input("""/------======------======------•------======------======------\      
# | Enter An Answer To The Question:                            |
# |                                                             |
# |  _________________________________________________________  |
# \------======------======------+------======------======------/\x1B[1F\r| """)
#                 print("\------======------======------+------======------======------/")

#             conn = sqlite3.connect('QuizGameDataBase.db')
#             cursor = sqlite3.Cursor(conn)
#             cursor.execute("""UPDATE QuizUserInput SET Question = ?, Answer = ? WHERE QuizName = ?""", (questionUserInput, answerUserInput, quizSelectionOption))

#             conn.commit()
#             conn.close()

#             MainModules.loadingModule()

    def AccountEditMainModule(self):
        AccountObject = EditAccountClass()
                
        MainModules.loadingModule()
        accountSelectionTypeOption = AccountObject.accountSelectionTypeModule()
        stayInModule = accountSelectionTypeOption

        if stayInModule != 3:

            MainModules.loadingModule()
            accountDisplay, accountList = AccountObject.accountNameSQL(accountSelectionTypeOption)

            accountSelectionOption = AccountObject.accountSelectionModule(accountDisplay, accountList)

            MainModules.loadingModule()
            accountFeaturesOption = AccountObject.accountFeaturesModule()

            if accountFeaturesOption == 1:
                pass
                return AccountObject.AccountEditMainModule()

            elif accountFeaturesOption == 2:
                pass
                return AccountObject.AccountEditMainModule()

            elif accountFeaturesOption == 3:
                pass
                return AccountObject.AccountEditMainModule()
            
            elif accountFeaturesOption == 6:

                MainModules.loadingModule()
                AccountObject.confirmationModule(accountSelectionTypeOption, accountSelectionOption)

                return AccountObject.AccountEditMainModule()
        

      


AccountObject = EditAccountClass()
AccountObject.AccountEditMainModule()