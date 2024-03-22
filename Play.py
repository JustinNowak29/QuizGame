import sqlite3, time, os, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/VisualStudio/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

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

    def quizUserInputGameModule(self, quizSelectionTypeOption, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""SELECT Question, Answer, QuizXPMultiplier FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))

        elif quizSelectionTypeOption == 2:
            cursor.execute("""SELECT Question, Answer, QuizXPMultiplier FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))

        sqlOutput = list(cursor.fetchall())

        conn.commit()
        conn.close()

        questionsCorrect = 0
        questionsIncorrect = 0
        xpMultiplier = sqlOutput[0][2]
        xpGained = 0

        for item in sqlOutput:

            print("""/------======------======------•------======------======------\                           
|                        You Got This!                        |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Question: """+item[0])
            answerInput = input("""|                                                             |
| Enter your answer to the Question below! ↓↓↓                |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
            print("\------======------======------+------======------======------/")

            if answerInput == item[1]:
                questionsCorrect += 1

                print("""/------======------======------•------======------======------\                           
|                         Correct!!                           |
\------======------======------•------======------======------/""")  

            elif answerInput != item[1]:
                questionsIncorrect += 1

                print("""/------======------======------•------======------======------\                           
|                        Incorrect..                          |
| Correct Answer ---> """+item[1])
                print("""\------======------======------•------======------======------/""")  
                
            MainModules.loadingModule()
            xpGained = int(questionsCorrect * xpMultiplier * 10)
                
        return questionsCorrect, questionsIncorrect, xpGained

    def resultsModule(self, questionsCorrect, questionsIncorrect, xpGained):

        scorePercent = questionsCorrect / (questionsCorrect + questionsIncorrect) * 100
        scorePercent = round(scorePercent, 2)
        percentageMessage = MainModules.scorePercentageToMessageConveter(scorePercent)

        print("""/------======------======------•------======------======------\                           
|                           Results                           |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Take a look...                                              |
| Questions Answered Correctly: """+str(questionsCorrect)+"""
| Questions Answered Incorrectly: """+str(questionsIncorrect)+"""
| Overall Percentage: """+str(scorePercent)+"""%, """+str(percentageMessage)+"""
| XP Gained: """+str(xpGained)+"""
\------======------======------•------======------======------/""")
        
    def quizEndModule():
        quizEndOption = int(input("""/------======------======------\                              
|           Continue:          |
\------======------======------/
/------======------======------\ 
| - Play Quiz Again        (1) |
| - QuizMaker              (2) |
| - Administrator          (3) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
    print("\------======------======------/")


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

            questionsCorrect, questionsIncorrect, xpGained = QuizObject.quizUserInputGameModule(quizSelectionTypeOption, quizSelectionOption)
            # multiple choice needs to be added

            QuizObject.resultsModule(questionsCorrect, questionsIncorrect, xpGained)


#--------------------------------------------------------------
#--------------------------------------------------------------

QuizObject = PlayQuizClass()
QuizObject.PlayMainModule()