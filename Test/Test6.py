

# listtesting = ["one","two","three","four","five","six"]

# print("| - Play a Quiz!           (1) |")
# for item in listtesting:
#     print("| -                            |", end='\r')
#     print("| -",item)

quizName = "TestingQuiz"
quizDifficulty = "Medium"
questionAmount = 9
quizType = "User Input"

checkingQuizFeaturesList = ["""| Take a look... -->           | * """+quizName+" *",
                            """| Continue?                    | Quiz Difficutly: """+quizDifficulty,
                            """| - Yes, Continue          (1) | Question Length: """+str(questionAmount),
                            """| - No, Return             (2) | """+quizType]

for item in checkingQuizFeaturesList:
    print("""|                                                             |""", end='\r')
    print(item)


questionAnswerList = ["| Question: """+item[0],
       "|                                                             |",
       "| (A) -> "+item[1],
       "| (B) -> "+item[2],
       "| (C) -> "+item[3],
       "| (D) -> "+item[4]]