import MainModules, sqlite3, time, os

class PlayQuizClass:


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

    def countdown(self):

        countdownValue = 5
        for x in reversed(range(6)):
            time.sleep(1)
            os.system('cls')
            countdownValue -= 1
            print("""/------======------======------\                              
|       Game Starts In.. (""",countdownValue,""") |
\------======------======------/""")
        os.system('cls')
            
        return countdownValue

    def quizQuestionSQL(self, quizSelectionTypeOption, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""SELECT Answer FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))
            sqlAnswerOutput = list(cursor.fetchall())

            cursor.execute("""SELECT Question FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))
            sqlQuestionOutput = list(cursor.fetchall())

        elif quizSelectionTypeOption == 2:
            cursor.execute("""SELECT Answer FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))
            sqlAnswerOutput = list(cursor.fetchall())

            cursor.execute("""SELECT Question FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))
            sqlQuestionOutput = list(cursor.fetchall())

        sqlAnswerOutput = list(dict.fromkeys(sqlAnswerOutput))
        sqlQuestionOutput = list(dict.fromkeys(sqlQuestionOutput))
        conn.commit()
        conn.close()

        sqlQuestionOutput = sqlQuestionOutput[0]
        sqlAnswerOutput = sqlAnswerOutput[0]

        for item in sqlQuestionOutput:

            print("""/------======------======------•------======------======------\                           
|                        You Got This!                        |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Question: """+item)
            answerInput = input("""|                                                             |
| Enter your answer to the Question below! ↓↓↓                |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
            print("\------======------======------+------======------======------/")

    def PlayMainModule(self):
        QuizObject = PlayQuizClass()
                
        MainModules.loadingModule()
        quizSelectionTypeOption = QuizObject.quizSelectionTypeModule()
        stayInModule = quizSelectionTypeOption

        if stayInModule != 3:

            MainModules.loadingModule()
            quizDisplay, quizList = QuizObject.quizNameSQL(quizSelectionTypeOption)

            quizSelectionOption = QuizObject.quizSelectionModule(quizDisplay, quizList)

            MainModules.loadingModule()
            QuizObject.countdown()

            QuizObject.quizQuestionSQL(quizSelectionTypeOption, quizSelectionOption)

#--------------------------------------------------------------
#--------------------------------------------------------------

QuizObject = PlayQuizClass()
QuizObject.PlayMainModule()