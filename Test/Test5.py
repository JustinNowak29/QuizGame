import sqlite3, sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')

import MainModules


questionsCorrect = 3
questionsIncorrect = 2
xpGained = 40

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


userPass = ('warsaw', 'poland')
accountType = 'User'
username = userPass[0]
password = userPass[1]
print(accountType, username, password)

conn = sqlite3.connect('QuizGameDataBase.db')
cursor = sqlite3.Cursor(conn)

# note for self: the code below is probably VERY reduntant, but I can't find a solution atm, come back to this later
if accountType == 'User':
    cursor.execute("""UPDATE User SET XP = XP + ?, QuizzesAnswered = QuizzesAnswered + 1 WHERE Username = ? AND Password = ?""",(xpGained, username, password))
    if scorePercent == 100:
        cursor.execute("""UPDATE User QuizzesAnsweredPerfectly = QuizzesAnsweredPerfectly + 1""")
elif accountType == 'QuizMaker':
    cursor.execute("""UPDATE QuizMaker SET XP = XP + ?, QuizzesAnswered = QuizzesAnswered + 1 WHERE Username = ? AND Password = ?""",(xpGained, username, password))
    if scorePercent == 100:
        cursor.execute("""UPDATE QuizMaker QuizzesAnsweredPerfectly = QuizzesAnsweredPerfectly + 1""")
elif accountType == 'Admin':
    cursor.execute("""UPDATE Admin SET XP = XP + ?, QuizzesAnswered = QuizzesAnswered + 1 WHERE Username = ? AND Password = ?""",(xpGained, username, password))
    if scorePercent == 100:
        cursor.execute("""UPDATE Admin QuizzesAnsweredPerfectly = QuizzesAnsweredPerfectly + 1""")

conn.commit()
conn.close()
