v = "Variable"

import sqlite3

print(v[0:5])


# chooseQuizDifficultyList = [('Easy', 1), ('Medium', 1.5), ('Hard', 2)]
# sss = int(input("wwww"))
# chooseQuizDifficultyList2 = [('Easy', 1)]
# chooseQuizDifficultyList2 = chooseQuizDifficultyList2[0][0]
# print(chooseQuizDifficultyList2)

# // Tkinter
# // Turtle
# // PyQt

# # ↓ ↓ ↓ ↓ ↓ Things I have learnt already

# // Python (Understanding of pgramming basics & OOP)
# // SQL (Basic)

# # ↓ ↓ ↓ ↓ ↓ Things to consider later down the line

# // Web Development (HTML, CSS, JavaScript)
# // App Development (Anroid, Flutter, React Native)
# // Programming Languages (C, C++, JavaScript)

def functione():

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

    else:

        options = ["A","B","C","D"]
        choicesList = []

        for x in range(4):

            letter = options[x]
            choiceInput = input("""/------======------======------•------======------======------\      
|  Enter the text for option """+letter+""":                               |
|                                                             |
|  _________________________________________________________  |
\------======------======------+------======------======------/\x1B[1F\r| """)
            print("\------======------======------+------======------======------/")
            choicesList.append(choiceInput)
            print(choicesList)


        correctChoiceOption = int(input("""/------======------======------\                              
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

        if correctChoiceOption == 1:
            correctChoice = choicesList[0]
        
        elif correctChoiceOption == 2:
            correctChoice = choicesList[1]

        elif correctChoiceOption == 3:
            correctChoice = choicesList[2]

        elif correctChoiceOption == 4:
            correctChoice = choicesList[3]

functione()