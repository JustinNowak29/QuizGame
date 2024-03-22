import sqlite3

quizSelectionOption = 'MultiplicationQuiz'

conn = sqlite3.connect('QuizGameDataBase.db')
cursor = sqlite3.Cursor(conn)

cursor.execute("""SELECT Question, Answer FROM QuizUserInput WHERE QuizName = ?""", (quizSelectionOption,))
sqlAnswerOutput = list(cursor.fetchall())

for item in sqlAnswerOutput:
    print(item[0])