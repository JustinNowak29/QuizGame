import sqlite3

quizSelectionOption = 'CapitalQuiz'

conn = sqlite3.connect('QuizGameDataBase.db')
cursor = sqlite3.Cursor(conn)

cursor.execute("""SELECT Question, Choice1, Choice2, Choice3, Choice4, Answer, AnswerLetter, QuizXPMultiplier FROM QuizMultipleChoice WHERE QuizName = ?""", (quizSelectionOption,))
sqlOutput = list(cursor.fetchall())

conn.commit()
conn.close()
letters = ['A','B','C','D']

xpMultiplier = sqlOutput[0][7]
print(xpMultiplier)

questionsCorrect = 0
questionsIncorrect = 0
xpGained = 0

for item in sqlOutput:
    print(item[0])

    answerInput = input("Enter the correct letter: ")

    if answerInput == item[6]:
        print("correct!")

    elif answerInput != item[6] and answerInput in letters:  
        print("false!")  

    else:
        print("invalid input")
