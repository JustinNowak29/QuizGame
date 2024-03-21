
import MainModules, sqlite3


class EditQuizClass:

    def quizSelectionTypeModule(self):

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

    
        print("""/------======------======------\                              
|          Quiz List:          |
\------======------======------/
/------======------======------\ 
| Enter a specific Quiz:       |""")
        for quizName in quizDisplay:
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

    def quizContentSQL(self, quizSelectionTypeOption, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""SELECT * FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))

        elif quizSelectionTypeOption == 2:
            cursor.execute("""SELECT QuizName FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))

        sqlOutput = cursor.fetchall()
        sqlOutput = list(dict.fromkeys(sqlOutput))
        conn.commit()
        conn.close()

        sqlOutput = sqlOutput[0]
        quizList = []

        for item in sqlOutput:
            quizList.append(str(item))
            print(item)

        return quizList

    def QuizEditMainModule(self):

        QuizObject = EditQuizClass()
                
        MainModules.loadingModule()
        quizSelectionTypeOption = QuizObject.quizSelectionTypeModule()
        stayInModule = quizSelectionTypeOption

        if stayInModule != 3:
            
            MainModules.loadingModule()
            quizDisplay, quizList = QuizObject.quizNameSQL(quizSelectionTypeOption)

            quizSelectionOption = QuizObject.quizSelectionModule(quizDisplay, quizList)

            MainModules.loadingModule()


            quizList = QuizObject.quizContentSQL(quizSelectionTypeOption, quizSelectionOption)
            print(quizList)


QuizObject = EditQuizClass()
QuizObject.QuizEditMainModule()



# quizSelectionTypeOption = 1
# quizSelectionOption = 'ef'
# QuizObject.quizContentSQL(quizSelectionTypeOption, quizSelectionOption)
# # QuizObject.quizNameSQL(quizSelectionTypeOption)