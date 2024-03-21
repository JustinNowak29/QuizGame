
import sqlite3, MainModules

class Quiz:

    def createQuizID(self):

        newID = int()
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT QuizID FROM QuizUserInput""")
        quizIDs = cursor.fetchall()

        if len(quizIDs) == 0:
            newID = 1
        else:
            newQuizIDs = []
            for i in range(len(quizIDs)):
                newQuizIDs.append(quizIDs[i][0])

            quizIDs = newQuizIDs
            newID = max(quizIDs) + 1
            print(newID)

        conn.commit()
        conn.close()

        return newID
    
    def textToRealConverter(self, quizDifficulty):

        if quizDifficulty == "Easy        ":     
            quizDifficulty == 1 
    
        elif quizDifficulty == "Medium      " :
            quizDifficulty == 1.5

        elif quizDifficulty == "Hard        ":
            quizDifficulty == 2

        return quizDifficulty


    def quizCreationModule(quizName, quizDifficulty, questionLength, quizType):

        MainModules.loadingModule()
        QuizObject = Quiz()
        newID = QuizObject.createQuizID()
        quizMultiplier = QuizObject.textToRealConverter(quizDifficulty)
        print(quizName, quizDifficulty, quizMultiplier, quizType)

        if quizType == "User Input Quiz     ":

            MainModules.loadingModule()

            for i in range(questionLength):

                questionUserInput, answerUserInput = Quiz.userInputQuizModule(questionLength)
                Quiz.insertQuestionIntoDataBase(newID, questionUserInput, answerUserInput, quizName, quizMultiplier)
                MainModules.loadingModule()

        else:
#       elif chooseQuiz TypeOption == "Multiple Choice Quiz":
            print("! work in progress !")

    def createAQuizGUI():

        print("""/------======------======------•------======------======------\                           
|                        Create A Quiz                        |
\------======------======------•------======------======------/
/------======------======------•------======------======------\                              
|                   Type In Questions Below                   |
\------======------======------•------======------======------/                              
/------======------======------•------======------======------\ """)

    def userInputQuizModule(chooseQuestionLengthOption):

        Quiz.createAQuizGUI()
        questionUserInput = input("""| Be Creative! (Maxiumum Character Length is 56)              |      
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
        print("\------======------======------+------======------======------/")

        if len(questionUserInput) > 56:
            print("""/------======------======------\                              
|  Input exceeds 56 Character  |
|       Limit, Try Again       |
\------======------======------/""")
            
            MainModules.loadingModule()
            return Quiz.userInputQuizModule(chooseQuestionLengthOption)

        else:
            answerUserInput = input("""/------======------======------•------======------======------\      
|  Enter An Answer To The Question:                           |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
            print("\------======------======------+------======------======------/")

        return questionUserInput, answerUserInput

    def insertQuestionIntoDataBase(newID, questionUserInput, answerUserInput, quizName, quizMultiplier):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO QuizUserInput VALUES (?, ?, ?, ?, ?)""", (newID, questionUserInput, answerUserInput, quizName, quizMultiplier))

        conn.commit()
        conn.close()
