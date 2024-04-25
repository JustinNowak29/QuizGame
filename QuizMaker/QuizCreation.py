
import random, sqlite3, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules


class CreateQuizClass:

    def createAQuizGUI(self):
        print("""/------======------======------\         
|        Create A Quiz!        |
\------======------======------/ """)

    def createAQuizGUI2(self):
        print("""/------======------======------•------======------======------\ 
|                        Create A Quiz                        |
\------======------======------•------======------======------/
/------======------======------+------======------======------\         
|    Question Configuration    |       Quiz Type Output       |
\------======------======------+------======------======------/
/------======------======------+------======------======------\ """)
        
    def createAQuizGUI3(self):
        print("""/------======------======------•------======------======------\                           
|                        Create A Quiz                        |
\------======------======------•------======------======------/
/------======------======------•------======------======------\                              
|                   Type In Questions Below                   |
\------======------======------•------======------======------/                              
/------======------======------•------======------======------\ """)
        
    def chooseQuizNameModule(self):
        QuizObject.createAQuizGUI2()
        chooseQuizNameOption = input("""| Input Quiz Name:             |                              |
| (Maxiumum Character Length   |                              |
|  is 26)                      |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """)
        print("\------======------======------+------======------======------/") 

        if len(chooseQuizNameOption) > 26:
            print("""/------======------======------\                              
|  Input exceeds 26 Character  |
|       Limit, Try Again       |
\------======------======------/""")
            
            MainModules.loadingModule()
            return QuizObject.chooseQuizNameModule()

        return chooseQuizNameOption

    def chooseQuizDifficultyModule(self):
        QuizObject.createAQuizGUI2()
        chooseQuizDifficultyList = [('Easy', 1), ('Medium', 1.5), ('Hard', 2)]
        chooseQuizDifficultyOption = int(input("""| Input Question Difficulty:   |                              |
| - Easy    // 1x   XP     (1) |                              |
| - Medium  // 1.5x XP     (2) |                              |       
| - Hard    // 2x   XP     (3) |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
        print("\------======------======------+------======------======------/")

        if chooseQuizDifficultyOption == 1:
            chooseQuizDifficultyList.remove(chooseQuizDifficultyList[2])
            chooseQuizDifficultyList.remove(chooseQuizDifficultyList[1])

        elif chooseQuizDifficultyOption == 2:
            chooseQuizDifficultyList.remove(chooseQuizDifficultyList[2])
            chooseQuizDifficultyList.remove(chooseQuizDifficultyList[0])

        elif chooseQuizDifficultyOption == 3:
            chooseQuizDifficultyList.remove(chooseQuizDifficultyList[1])
            chooseQuizDifficultyList.remove(chooseQuizDifficultyList[0])
        
        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.chooseQuizDifficultyModule()
        
        return chooseQuizDifficultyList

    def chooseQuestionAmountModule(self):
        QuizObject.createAQuizGUI2()
        chooseQuestionAmountOption = int(input("""| Input Question Amount:       |                              |
| - Input Value (From 3 To 15) |                              |
| - Random Value          (-1) |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
        print("\------======------======------+------======------======------/") 

        if chooseQuestionAmountOption >= 3 and chooseQuestionAmountOption <= 15:
            return chooseQuestionAmountOption
        
        elif chooseQuestionAmountOption == -1:
            chooseQuestionAmountOption = random.randint(3, 15)
            return chooseQuestionAmountOption
        
        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.chooseQuestionAmountModule()

    def chooseQuizTypeModule(self):
        QuizObject.createAQuizGUI2()
        chooseQuizTypeOption = int(input("""| Choose Quiz Type:            |                              |       
| - User Input             (1) |                              |
| - Multiple Choice        (2) |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
        print("\------======------======------+------======------======------/")

        if chooseQuizTypeOption == 1:
            chooseQuizTypeOption = "User Input Quiz     "
        
        elif chooseQuizTypeOption == 2:
            chooseQuizTypeOption = "Multiple Choice Quiz"
        
        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.chooseQuizTypeModule()

        return chooseQuizTypeOption

    def confirmQuizFeaturesModule(self, quizName, quizDifficulty, questionAmount, quizType):
        QuizObject.createAQuizGUI2()

        checkingQuizFeaturesList = ["""| Take a look... -->           | * """+quizName+" *",
                """| Continue?                    | Quiz Difficutly: """+(quizDifficulty[0][0]),
                """| - Yes, Continue          (1) | Question Length: """+str(questionAmount),
                """| - No, Return             (2) | """+quizType]

        for item in checkingQuizFeaturesList:
            print("""|                                                             |""", end='\r')
            print(item)

        confirmQuizFeaturesOption = int(input("""|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
        print("\------======------======------+------======------======------/")
        
        if confirmQuizFeaturesOption == 2:
            QuizObject.QuizCreationMainModule()

        elif confirmQuizFeaturesOption != 1 and confirmQuizFeaturesOption != 2:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.confirmQuizFeaturesModule(quizName, quizDifficulty, questionAmount, quizType)

    def createQuizID(self, quizType):

        newID = int()
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizType == "User Input Quiz     ":
            cursor.execute("""SELECT QuizID FROM QuizUserInput""")

        elif quizType == "Multiple Choice Quiz":
            cursor.execute("""SELECT QuizID FROM QuizMultipleChoice""")

        quizIDs = cursor.fetchall()

        if len(quizIDs) == 0:
            newID = 1

        else:
            newQuizIDs = []
            for i in range(len(quizIDs)):
                newQuizIDs.append(quizIDs[i][0])

            quizIDs = newQuizIDs
            newID = max(quizIDs) + 1

        conn.commit()
        conn.close()

        return newID

    def quizCreationModule(self, quizName, quizDifficulty, questionAmount, quizType):

        MainModules.loadingModule()
        newID = QuizObject.createQuizID(quizType)

        if quizType == "User Input Quiz     ":

            MainModules.loadingModule()

            for i in range(questionAmount):

                questionUserInput, answerUserInput = QuizObject.userInputQuizModule(questionAmount)
                QuizObject.insertUserInputQuizSQL(newID, questionUserInput, answerUserInput, quizName, quizDifficulty)
                MainModules.loadingModule()

        else:

            MainModules.loadingModule()

            for i in range(questionAmount):

                questionMultipleChoice, choicesList, correctChoice, correctChoiceLetter = QuizObject.multipleChoiceQuizModule(questionAmount)
                QuizObject.insertMultipleChoiceQuizSQL(newID, questionMultipleChoice, choicesList, correctChoice, correctChoiceLetter, quizName, quizDifficulty)
                MainModules.loadingModule()

        QuizObject.quizCreatedGUI()

        return QuizObject

    def userInputQuizModule(self, chooseQuestionLengthOption):

        QuizObject.createAQuizGUI3()
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
            return QuizObject.userInputQuizModule(chooseQuestionLengthOption)

        else:
            answerUserInput = input("""/------======------======------•------======------======------\      
| Enter An Answer To The Question:                            |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
            print("\------======------======------+------======------======------/")

        return questionUserInput, answerUserInput
    
    def insertUserInputQuizSQL(self, newID, questionUserInput, answerUserInput, quizName, quizDifficulty):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO QuizUserInput VALUES (?, ?, ?, ?, ?)""", (newID, questionUserInput, answerUserInput, quizName, quizDifficulty))

        conn.commit()
        conn.close()

    def multipleChoiceQuizModule(self, chooseQuestionLengthOption):

        QuizObject.createAQuizGUI3()
        questionMultipleChoice = input("""| Be Creative! (Maxiumum Character Length is 56)              |      
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
        print("\------======------======------+------======------======------/")

        if len(questionMultipleChoice) > 56:

            print("""/------======------======------\                              
|  Input exceeds 56 Character  |
|       Limit, Try Again       |
\------======------======------/""")
            
            return QuizObject.multipleChoiceQuizModule(chooseQuestionLengthOption)

        else:

            options = ["A","B","C","D"]
            choicesList = []

            for x in range(4):

                MainModules.loadingModule()
                letter = options[x]
                choiceInput = input("""/------======------======------•------======------======------\      
|  Enter the text for option """+letter+""":                               |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
                print("\------======------======------+------======------======------/")
                choicesList.append(choiceInput)

            MainModules.loadingModule()

            QuizObject.createAQuizGUI()
            correctChoiceLetter = int(input("""/------======------======------\                              
|        Correct Choice        |
\------======------======------/
/------======------======------\ 
| Which Option is correct?     |
| - A                      (1) |
| - B                      (2) |
| - C                      (3) |
| - D                      (4) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
            print("\------======------======------/")

            if correctChoiceLetter == 1:
                correctChoice = choicesList[0]
            
            elif correctChoiceLetter == 2:
                correctChoice = choicesList[1]

            elif correctChoiceLetter == 3:
                correctChoice = choicesList[2]

            elif correctChoiceLetter == 4:
                correctChoice = choicesList[3]

            return questionMultipleChoice, choicesList, correctChoice, correctChoiceLetter
        
    def insertMultipleChoiceQuizSQL(self, newID, questionMultipleChoice, choicesList, answerMutlipleChoice, answerMutlipleChoiceLetter,quizName, quizDifficulty):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO QuizMultipleChoice VALUES (?,?,?,?,?,?,?,?,?,?)""", (newID, questionMultipleChoice, choicesList[0],choicesList[1],choicesList[2],choicesList[3], answerMutlipleChoice, answerMutlipleChoiceLetter, quizName, quizDifficulty))

        conn.commit()
        conn.close()

    def quizCreatedGUI(self):

        QuizObject.createAQuizGUI()
        print("""/------======------======------\                              
|         Quiz Created         |
\------======------======------/""")

    def QuizCreationMainModule(self):
        QuizObject = CreateQuizClass()
            
        MainModules.loadingModule()
        quizName = QuizObject.chooseQuizNameModule()

        MainModules.loadingModule()
        quizDifficulty = QuizObject.chooseQuizDifficultyModule()

        MainModules.loadingModule()
        questionAmount = QuizObject.chooseQuestionAmountModule()

        MainModules.loadingModule()
        quizType = QuizObject.chooseQuizTypeModule()

        MainModules.loadingModule()
        QuizObject.confirmQuizFeaturesModule(quizName, quizDifficulty, questionAmount, quizType)

        QuizObject.createQuizID(quizType)
        quizDifficulty = float(quizDifficulty[0][1])

        QuizObject.quizCreationModule(quizName, quizDifficulty, questionAmount, quizType)

#--------------------------------------------------------------
#--------------------------------------------------------------

QuizObject = CreateQuizClass()
# QuizObject.QuizCreationMainModule()

#--------------------------------------------------------------
#--------------------------------------------------------------

# quizType = "User Input Quiz     "
# quizType = "Multiple Choice Quiz"
# newID = QuizObject.createQuizID(quizType)
# print(newID)