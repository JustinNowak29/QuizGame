
    # def quizContentSQL(self, quizSelectionTypeOption, quizFeature, variableModification, quizSelectionOption):

    #     conn = sqlite3.connect('QuizGameDataBase.db')
    #     cursor = sqlite3.Cursor(conn)

    #     if quizSelectionTypeOption == 1:
    #         cursor.execute("""UPDATE QuizUserInput SET ? = ?, WHERE QuizName = ?""", (quizFeature, variableModification, quizSelectionOption,))

    #     elif quizSelectionTypeOption == 2:
    #         cursor.execute("""UPDATE QuizMultipleChoice SET ? = ?, WHERE QuizName = ?""", (quizFeature, variableModification, quizSelectionOption,))

    #     conn.commit()
    #     conn.close()