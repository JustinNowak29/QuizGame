
import sqlite3, time, os, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

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

    def quizUserInputGameModule(self, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""SELECT Question, Answer, QuizXPMultiplier FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))
        sqlOutput = list(cursor.fetchall())

        conn.commit()
        conn.close()

        xpMultiplier = sqlOutput[0][2]
        questionsCorrect = 0
        questionsIncorrect = 0
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

    def quizMultipleChoiceGameModule(self, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""SELECT Question, Choice1, Choice2, Choice3, Choice4, Answer, AnswerLetter, QuizXPMultiplier FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))
        sqlOutput = list(cursor.fetchall())

        conn.commit()
        conn.close()

        xpMultiplier = sqlOutput[0][7]
        questionsCorrect = 0
        questionsIncorrect = 0
        xpGained = 0

        for item in sqlOutput:

            print("""/------======------======------•------======------======------\                           
|                        You Got This!                        |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Question: """+item[0]+"""
|                                                             |
| (A) -> """+item[1]+"""
| (B) -> """+item[2]+"""
| (C) -> """+item[3]+"""
| (D) -> """+item[4])
            answerInput = input("""|                                                             |
| Enter the correct letter below! ↓↓↓                         |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
            print("\------======------======------+------======------======------/")

            if answerInput == item[6]:
                questionsCorrect += 1

                print("""/------======------======------•------======------======------\                           
|                         Correct!!                           |
\------======------======------•------======------======------/""")  

            elif answerInput != item[6]: 
                questionsIncorrect += 1

                print("""/------======------======------•------======------======------\                           
|                        Incorrect..                          |
| Correct Answer ---> """+item[5])
                print("""\------======------======------•------======------======------/""")  
                
            MainModules.loadingModule()
            xpGained = int(questionsCorrect * xpMultiplier * 10)
                
        return questionsCorrect, questionsIncorrect, xpGained

    def resultsModule(self, questionsCorrect, questionsIncorrect, xpGained, accountType, credentials):

        scorePercent = questionsCorrect / (questionsCorrect + questionsIncorrect) * 100
        scorePercent = round(scorePercent, 2)
        percentageMessage = MainModules.scorePercentageToMessageConveter(scorePercent)

        print("""/------======------======------•------======------======------\                           
|                           Results                           |
\------======------======------•------======------======------/                             
/------======------======------•------======------======------\ 
| Take a look...                                              |""")
        
        checkingQuizResultsList = ["""| Questions Answered Correctly: """+str(questionsCorrect),
            """| Questions Answered Incorrectly: """+str(questionsIncorrect),
            """| Overall Percentage: """+str(scorePercent)+"""%, """+str(percentageMessage),
            """| XP Gained: """+str(xpGained)]

        for item in checkingQuizResultsList:
            print("""|                                                             |""", end='\r')
            print(item)
        
        input("""/------======------======------•------======------======------\                           
|                  Press any key to continue                  |
\------======------======------•------======------======------/ """)
        
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        username = str(credentials[0])
        password = str(credentials[1])
        accountType = str(accountType)
        # print(accountType, username, password)

        # note for self: the code below is probably VERY reduntant, but I can't find a solution atm, come back to this later
        if accountType == 'User':
            cursor.execute("""UPDATE User SET XP = XP + ?, QuizzesAnswered = QuizzesAnswered + 1 WHERE Username = ? AND Password = ?""",(xpGained, username, password))
            if scorePercent == 100:
                cursor.execute("""UPDATE User SET QuizzesAnsweredPerfectly = QuizzesAnsweredPerfectly + 1 WHERE Username = ? AND Password = ?""",(username, password))
        elif accountType == 'QuizMaker':
            cursor.execute("""UPDATE QuizMaker SET XP = XP + ?, QuizzesAnswered = QuizzesAnswered + 1 WHERE Username = ? AND Password = ?""",(xpGained, username, password))
            if scorePercent == 100:
                cursor.execute("""UPDATE QuizMaker SET QuizzesAnsweredPerfectly = QuizzesAnsweredPerfectly + 1 WHERE Username = ? AND Password = ?""",(username, password))
        elif accountType == 'Admin':
            cursor.execute("""UPDATE Admin SET XP = XP + ?, QuizzesAnswered = QuizzesAnswered + 1 WHERE Username = ? AND Password = ?""",(xpGained, username, password))
            if scorePercent == 100:
                cursor.execute("""UPDATE Admin SET QuizzesAnsweredPerfectly = QuizzesAnsweredPerfectly + 1 WHERE Username = ? AND Password = ?""",(username, password))

        conn.commit()
        conn.close()

    def quizEndModule(self, quizSelectionTypeOption, quizSelectionOption, accountType, credentials):
        quizEndOption = int(input("""/------======------======------\                              
|           Continue:          |
\------======------======------/
/------======------======------\ 
| - Play Quiz Again        (1) |
| - Return to Menu         (2) |
| - Exit                   (3) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/")

        if quizEndOption == 1:
            return QuizObject.quizGameModule(quizSelectionTypeOption, quizSelectionOption, accountType, credentials)
        
        elif quizEndOption == 2:
            pass

        elif quizEndOption == 3:
            exit()

        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.quizEndModule(quizSelectionTypeOption, quizSelectionOption, accountType, credentials)
        
    def quizGameModule(self, quizSelectionTypeOption, quizSelectionOption, accountType, credentials):

        MainModules.loadingModule()
        QuizObject.countdown()

        if quizSelectionTypeOption == 1:
                questionsCorrect, questionsIncorrect, xpGained = QuizObject.quizUserInputGameModule(quizSelectionOption)

        elif quizSelectionTypeOption == 2:
            questionsCorrect, questionsIncorrect, xpGained = QuizObject.quizMultipleChoiceGameModule(quizSelectionOption)

        MainModules.loadingModule()
        QuizObject.resultsModule(questionsCorrect, questionsIncorrect, xpGained, accountType, credentials)

        MainModules.loadingModule()
        QuizObject.quizEndModule(quizSelectionTypeOption, quizSelectionOption, accountType, credentials)

    def PlayMainModule(self, accountType, credentials):
        QuizObject = PlayQuizClass()
                
        MainModules.loadingModule()
        quizSelectionTypeOption = QuizObject.quizSelectionTypeModule()
        stayInModule = quizSelectionTypeOption

        if stayInModule != 3:

            MainModules.loadingModule()
            quizDisplay, quizList = QuizObject.quizNameSQL(quizSelectionTypeOption)

            quizSelectionOption = QuizObject.quizSelectionModule(quizDisplay, quizList)

            QuizObject.quizGameModule(quizSelectionTypeOption, quizSelectionOption, accountType, credentials)

#--------------------------------------------------------------
#--------------------------------------------------------------

QuizObject = PlayQuizClass()
# QuizObject.PlayMainModule()