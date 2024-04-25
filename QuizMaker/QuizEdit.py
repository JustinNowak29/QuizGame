
import sqlite3, sys, random

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules

class EditQuizClass:

    def editAQuizGUI(self):
        print("""/------======------======------•------======------======------\ 
|                         Edit A Quiz                         |
\------======------======------•------======------======------/
/------======------======------•------======------======------\ """)
        
    def editAQuizGUI2(self):
        print("""/------======------======------•------======------======------\                           
|                         Edit A Quiz                         |
\------======------======------•------======------======------/
/------======------======------•------======------======------\                              
|                  Edit the Questions Below!                  |
\------======------======------•------======------======------/                              
/------======------======------•------======------======------\ """)

    def quizTypeModule(self):

        quizSelectionTypeOption = int(input("""/------======------======------\                              
|          Quiz Type:          |
\------======------======------/
/------======------======------\ 
| Enter type of Quiz:          |
| - User Input             (1) |
| - Multiple Choice        (~) |
|   (Unfinished)               |
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
            return QuizObject.quizFeaturesModule()
        
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

        for quiz in quizList:
            if quizSelectionOption == quiz:
                correctInputChecker = 1

        if correctInputChecker != 1:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.quizSelectionModule(quizDisplay, quizList)
        
        return quizSelectionOption
    
    def quizFeaturesModule(self):

        quizFeaturesOption = int(input("""/------======------======------\                              
|        Quiz Features:        |
\------======------======------/
/------======------======------\ 
| Enter the Feature you'd like |
| to Edit:                     |
| - Quiz Name              (1) |
| - Quiz Difficulty        (2) |
| - Question Length        (X) |
| - Questions & Answers    (X) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/")
        
        if quizFeaturesOption >= 1 or quizFeaturesOption <= 4:
            return quizFeaturesOption  

        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.quizFeaturesModule()
        
    def editQuizNameModule(self, quizSelectionTypeOption, quizSelectionOption):

        QuizObject.editAQuizGUI()
        variableModification = input("""| Input a new Quiz Name:       |                              |
| (Maxiumum Character Length   |                              |
|  is 26)                      |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """)
        print("\------======------======------+------======------======------/") 

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if len(variableModification) > 26:
            print("""/------======------======------\                              
|  Input exceeds 26 Character  |
|       Limit, Try Again       |
\------======------======------/""")
            
            MainModules.loadingModule()
            return QuizObject.editQuizNameModule(quizSelectionTypeOption, quizSelectionOption)

        if quizSelectionTypeOption == 1:
            cursor.execute("""UPDATE QuizUserInput SET QuizName = ? WHERE QuizName = ?""", (variableModification, quizSelectionOption,))

        elif quizSelectionTypeOption == 2:
            cursor.execute("""UPDATE QuizMultipleChoice SET QuizName = ? WHERE QuizName = ?""", (variableModification, quizSelectionOption,))

        conn.commit()
        conn.close()
    
    def editQuizDifficultyModule(self, quizSelectionTypeOption, quizSelectionOption, questionAmount):
        QuizObject.editAQuizGUI()
        editQuizDifficultyList = [('Easy', 1), ('Medium', 1.5), ('Hard', 2)]
        editQuizDifficultyOption = int(input("""| Input Question Difficulty:   |                              |
| - Easy    // 1x   XP     (1) |                              |
| - Medium  // 1.5x XP     (2) |                              |       
| - Hard    // 2x   XP     (3) |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
        print("\------======------======------+------======------======------/")

        if editQuizDifficultyOption == 1:
            editQuizDifficultyList.remove(editQuizDifficultyList[2])
            editQuizDifficultyList.remove(editQuizDifficultyList[1])

        elif editQuizDifficultyOption == 2:
            editQuizDifficultyList.remove(editQuizDifficultyList[2])
            editQuizDifficultyList.remove(editQuizDifficultyList[0])

        elif editQuizDifficultyOption == 3:
            editQuizDifficultyList.remove(editQuizDifficultyList[1])
            editQuizDifficultyList.remove(editQuizDifficultyList[0])
        
        else:
            MainModules.invalidInputModule()
            MainModules.loadingModule()
            return QuizObject.chooseQuizDifficultyModule()
        
        editQuizDifficultyList = editQuizDifficultyList[0][1]
        
        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""UPDATE QuizUserInput SET QuizXPMultiplier = ? WHERE QuizName = ?""", (editQuizDifficultyList, quizSelectionOption,))

        elif quizSelectionTypeOption == 2:
            cursor.execute("""UPDATE QuizMultipleChoice SET QuizXPMultiplier = ? WHERE QuizName = ?""", (editQuizDifficultyList, quizSelectionOption,))

        conn.commit()
        conn.close()

    def editUserInputQuizModule(self, questionAmount, quizSelectionOption):

        print("this doesn't work!!!")
        print("this doesn't work!!!")
        print("this doesn't work!!!")

        for x in range(questionAmount):
        
            QuizObject.editAQuizGUI2()
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
                return QuizObject.editUserInputQuizModule()

            else:
                answerUserInput = input("""/------======------======------•------======------======------\      
| Enter An Answer To The Question:                            |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
                print("\------======------======------+------======------======------/")

            conn = sqlite3.connect('QuizGameDataBase.db')
            cursor = sqlite3.Cursor(conn)
            cursor.execute("""UPDATE QuizUserInput SET Question = ?, Answer = ? WHERE QuizName = ?""", (questionUserInput, answerUserInput, quizSelectionOption))

            conn.commit()
            conn.close()

            MainModules.loadingModule()

    def editMultiplieChoiceQuizModule(self, questionAmount):
        pass

    def quizEditModule(self, quizSelectionTypeOption, quizSelectionOption):

        conn = sqlite3.connect('QuizGameDataBase.db')
        cursor = sqlite3.Cursor(conn)

        if quizSelectionTypeOption == 1:
            cursor.execute("""SELECT Question FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))
        elif quizSelectionTypeOption == 2:
            cursor.execute("""SELECT Question FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))

        questionAmount = len(cursor.fetchall())
        print(questionAmount)

        conn.commit()
        conn.close()

        if quizSelectionTypeOption == 1:
            QuizObject.editUserInputQuizModule(questionAmount, quizSelectionOption)

        elif quizSelectionTypeOption == 2:
            QuizObject.editMultiplieChoiceQuizModule(questionAmount, quizSelectionOption)

    def QuizEditMainModule(self):

        QuizObject = EditQuizClass()
                
        MainModules.loadingModule()
        quizSelectionTypeOption = QuizObject.quizTypeModule()
        stayInModule = quizSelectionTypeOption

        if stayInModule != 3:
            
            MainModules.loadingModule()
            quizDisplay, quizList = QuizObject.quizNameSQL(quizSelectionTypeOption)

            quizSelectionOption = QuizObject.quizSelectionModule(quizDisplay, quizList)

            MainModules.loadingModule()
            quizFeaturesOption = QuizObject.quizFeaturesModule()

            MainModules.loadingModule()

            if quizFeaturesOption == 1:
                QuizObject.editQuizNameModule(quizSelectionTypeOption, quizSelectionOption)
                return QuizObject.QuizEditMainModule()

            elif quizFeaturesOption == 2:
                QuizObject.editQuizDifficultyModule(quizSelectionTypeOption, quizSelectionOption)
                return QuizObject.QuizEditMainModule()

            elif quizFeaturesOption == 3:
                pass

            elif quizFeaturesOption == 4:
                pass
                # QuizObject.quizEditModule(quizSelectionTypeOption, quizSelectionOption)
                # return QuizObject.QuizEditMainModule()

            # MainModules.loadingModule()
            # QuizObject.quizContentSQL(quizSelectionTypeOption, quizFeature, variableModification, quizSelectionOption)

            # quizList = QuizObject.quizContentSQL(quizSelectionTypeOption, quizSelectionOption)
            # print(quizList)

QuizObject = EditQuizClass()
QuizObject.QuizEditMainModule()

# quizSelectionTypeOption = 1
# quizSelectionOption = 'ef'
# QuizObject.quizContentSQL(quizSelectionTypeOption, quizSelectionOption)
# # QuizObject.quizNameSQL(quizSelectionTypeOption)