
import sqlite3, time, os, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class DeleteQuizClass:

    def deleteAQuizGUI(self):
        print("""/------======------======------\         
|        Delete A Quiz!        |
\------======------======------/ """)

    def quizSelectionTypeModule(self):

        QuizObject.deleteAQuizGUI()
        quizSelectionTypeOption = int(input("""/------======------======------\                              
|          Quiz Type:          |
\------======------======------/
/------======------======------\ 
| Enter type of Quiz:          |
| - User Input             (1) |
| - Multiple Choice        (2) |
| - Return to Main Menu    (3) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/")
        
        if quizSelectionTypeOption >= 1 or quizSelectionTypeOption <= 3:
            return quizSelectionTypeOption         
        
        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.quizSelectionTypeModule()
        
    def quizNameSQL(self, quizSelectionTypeOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""SELECT QuizName FROM QuizUserInput ORDER BY QuizName ASC""")

        elif quizSelectionTypeOption == 2:
            cursor.execute("""SELECT QuizName FROM QuizMultipleChoice ORDER BY QuizName ASC""")

        sqlOutput = list(cursor.fetchall())
        sqlOutput = list(dict.fromkeys(sqlOutput))
        conn.commit()
        conn.close()

        quizList = []
        quizDisplay = []

        for item in sqlOutput:

            tupleToStringConveter = (list(item)[0])
            quizDisplay.append("| - " + str(tupleToStringConveter))
            quizList.append(tupleToStringConveter)

        return quizDisplay, quizList

    def quizSelectionModule(self, quizDisplay, quizList):

        QuizObject.deleteAQuizGUI()
        print("""/------======------======------\                              
|          Quiz List:          |
\------======------======------/
/------======------======------\ 
| Enter a specific Quiz:       |""")
        for quizName in quizDisplay:
            print("| -                            |", end='\r')
            print(quizName)
        quizSelectionOption = input("""|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """)
        print("\------======------======------/")

        correctInputChecker = 0

        for quizListe in quizList:
            if quizSelectionOption == quizListe:
                correctInputChecker = 1

        if correctInputChecker != 1:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.quizSelectionModule(quizDisplay, quizList)
        
        return quizSelectionOption

    def countdown(self):

    # Located in quizSelectionModule() #

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

        QuizObject.countdown()
        QuizObject.deleteAQuizGUI()
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
            return QuizObject.QuizDeletionMainModule()

        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()    
            return QuizObject.confirmationModule()

    def quizDeletionSQL(self, quizSelectionTypeOption, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""DELETE FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))

        elif quizSelectionTypeOption == 2:
            cursor.execute("""DELETE FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))

        conn.commit()
        conn.close()

    def quizDeletedGUI(self):

        QuizObject.deleteAQuizGUI()
        print("""/------======------======------\                              
|         Quiz Deleted         |
\------======------======------/""")

    def QuizDeletionMainModule(self):
        QuizObject = DeleteQuizClass()
                
        MainModules.loadingModule()
        quizSelectionTypeOption = QuizObject.quizSelectionTypeModule()
        stayInModule = quizSelectionTypeOption

        if stayInModule != 3:

            MainModules.loadingModule()
            quizDisplay, quizList = QuizObject.quizNameSQL(quizSelectionTypeOption)

            quizSelectionOption = QuizObject.quizSelectionModule(quizDisplay, quizList)
            
            MainModules.loadingModule()
            confirmationOption = QuizObject.confirmationModule()

            if confirmationOption == 1:

                MainModules.loadingModule()
                QuizObject.quizDeletionSQL(quizSelectionTypeOption, quizSelectionOption)

                QuizObject.quizDeletedGUI()
                MainModules.loadingModule()


#--------------------------------------------------------------
#--------------------------------------------------------------

QuizObject = DeleteQuizClass()
# QuizObject.QuizDeletionMainModule()

#--------------------------------------------------------------
#--------------------------------------------------------------

# quizSelectionTypeOption = quizSelectionTypeModule()
# quizSelectionModule()

# quizSelectionTypeOption = 1
# w = sqlQuizNameModule(quizSelectionTypeOption)
# for w in w:
#     print(w)