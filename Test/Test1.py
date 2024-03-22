

# my_list = []
# for x in range(2):
#     new_items = list(input("put in value"))

#     my_list.extend(new_items)

#     print(my_list)


# for item in quizDisplay:
#     print(item)
# print(quizList)

# def testfunc():
#     vall = 0
#     testlist = ["wow","wow2","wow3"]
#     z = input("type here:")
#     for testlis in testlist:
#         if z == testlis:
#             vall = 1
#             print("pass")
        
#     if vall != 1:
#         return testfunc()
# testfunc()

# varr = 0
# def func(varr):
#     varr = int(input("enter input:"))
#     if varr == 0:
#         print("run program")
#     else:
#         print("!")

# func(0)

quizSelectionTypeOption = 1

import sqlite3

conn = sqlite3.connect('QuizGameDataBase.db')
cursor = sqlite3.Cursor(conn)

if quizSelectionTypeOption == 1:
    cursor.execute("""SELECT QuizName FROM QuizUserInput ORDER BY QuizName ASC""")

elif quizSelectionTypeOption == 2:
    cursor.execute("""SELECT QuizName FROM QuizMultipleChoice""")

    sqlOutput = cursor.fetchall()
    sqlOutput = list(dict.fromkeys(sqlOutput))
    conn.commit()
    conn.close()

    sqlOutput = sqlOutput[0]
    quizList = []
    quizDisplay = []

    for item in sqlOutput:
        quizDisplay.append("| - " + str(item))
        print(item)

    print(quizDisplay)
