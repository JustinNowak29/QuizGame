
import MainModules, random, sqlite3

def quizMakerMainMenuModule():
        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| - Create a Quiz          (1) |
| - Manage a Quiz          (2) |
| - Delete a Quiz          (3) |
| - Test a Quiz            (4) |
| - Exit                   (5) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 
        return mainMenuOption

def createAQuizGUI():
    print("""/------======------======------•------======------======------\                           
|                        Create A Quiz                        |
\------======------======------•------======------======------/
/------======------======------+------======------======------\                              
|    Question Configuration    |       Quiz Type Output       |
\------======------======------+------======------======------/                              
/------======------======------+------======------======------\ """)
    
def chooseQuizNameModule():
    createAQuizGUI()
    chooseQuizNameOption = input("""| Input Question Name:         |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """)
    print("\------======------======------+------======------======------/") 

    return chooseQuizNameOption

def chooseQuizDifficultyModule():
    createAQuizGUI()
    chooseQuizDifficultyOption = int(input("""| Input Question Difficulty:   |                              |
| - Easy    // 1x EXP      (1) |                              |
| - Medium  // 1.5x EXP    (2) |                              |       
| - Hard    // 2x EXP      (3) |                              |
|                              |                              |                               
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
    print("\------======------======------+------======------======------/")

    if chooseQuizDifficultyOption == 1:
        chooseQuizDifficultyOption = "Easy        "     
    
    elif chooseQuizDifficultyOption == 2:
        chooseQuizDifficultyOption = "Medium      " 

    elif chooseQuizDifficultyOption == 2:
        chooseQuizDifficultyOption = "Hard        "
    
    else:
        MainModules.invalidInputModule()
        MainModules.loadingModule()
        return chooseQuizDifficultyModule()
    
    return chooseQuizDifficultyOption


def chooseQuestionLengthModule():
    createAQuizGUI()
    chooseQuestionLengthOption = int(input("""| Input Question Length:       |                              |
| - Input Value (From 3 To 15) |                              |
| - Random Value          (-1) |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
    print("\------======------======------+------======------======------/") 

    if chooseQuestionLengthOption >= 3 and chooseQuestionLengthOption <= 15:
        return chooseQuestionLengthOption
    
    elif chooseQuestionLengthOption == -1:
        chooseQuestionLengthOption = random.randint(3, 15)
        return chooseQuestionLengthOption
    
    else:
        MainModules.invalidInputModule()
        MainModules.loadingModule()
        return chooseQuestionLengthModule()

def chooseQuizTypeModule():
    createAQuizGUI()
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
        return chooseQuizTypeModule()

    return chooseQuizTypeOption

def confirmQuizFeaturesModule(quizName, quizDifficulty, questionLength, quizType):
    createAQuizGUI()
    confirmQuizFeaturesOption = int(input("""| Take a look... -->           | Quiz Name: """+str(quizName)+""" 
| Continue?                    | Quiz Difficutly: """+str(quizDifficulty)+"""|
| - Yes, Continue          (1) | Question Length: """+str(questionLength)+""" 
| - No, Return             (2) | """+str(quizType)+"""         |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
    print("\------======------======------+------======------======------/")
    
    if confirmQuizFeaturesOption != 1 and confirmQuizFeaturesOption != 2:
        MainModules.invalidInputModule()
        MainModules.loadingModule()
        return confirmQuizFeaturesModule(quizName, quizDifficulty, questionLength, quizType)

    return confirmQuizFeaturesOption

def QuizConfiguartion():
    MainModules.loadingModule()
    mainMenuOption = quizMakerMainMenuModule()

    if mainMenuOption == 1:

        MainModules.loadingModule()
        quizName = chooseQuizNameModule()
        MainModules.loadingModule()
        quizDifficulty = chooseQuizDifficultyModule()
        MainModules.loadingModule()
        questionLength = chooseQuestionLengthModule()
        MainModules.loadingModule()
        quizType = chooseQuizTypeModule()
        MainModules.loadingModule()
        confirmQuizFeaturesOption = confirmQuizFeaturesModule(quizName, quizDifficulty, questionLength, quizType)

        if confirmQuizFeaturesOption == 1:
            return quizName, quizDifficulty, questionLength, quizType
    
        elif confirmQuizFeaturesOption == 2:
            return QuizConfiguartion()

    else:
        print("! not finished !")
        MainModules.invalidInputModule()
        QuizConfiguartion()

# ↓↓↓ Code Below for Testing Purposes ↓↓↓ #


# chooseQuestionLengthOption, chooseQuizTypeOption = QuizConfiguartion()
# print(chooseQuestionLengthOption, chooseQuizTypeOption)
