
import sys

sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame/Main')
sys.path.append('c:/Users/Justin/Desktop/Coding/ObjectOrientedProgramming/QuizGame')

import MainModules, Play

class GuestClass:

    def guestGUI(self):
        print("""/------======------======------\                              
|            Guest             |
\------======------======------/""")

    def guestMainMenuModule(self):

        accountType = 0
        credentials = (0,0)

        MainModules.loadingModule()
        guestObject.guestGUI()

        print("""/------======------======------\                              
| Note: In order to have the   |
| full experience, make sure   |
| to make an account when you  |
| play the game again!         |
\------======------======------/""")

        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| - Play a Quiz!           (1) |
| - About                  (2) |
| - Exit                   (3) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 

        if mainMenuOption == 1:

            QuizObject = Play.PlayQuizClass()
            QuizObject.PlayMainModule(accountType, credentials)
            return guestObject.guestMainMenuModule()

        elif mainMenuOption == 2:

            MainModules.loadingModule()
            MainModules.aboutModule()
            return guestObject.guestMainMenuModule()
        
        elif mainMenuOption == 3:
            exit()

        else:
            
            MainModules.invalidInputModule()
            guestObject.guestMainMenuModule()    

guestObject = GuestClass()
guestObject.guestMainMenuModule()