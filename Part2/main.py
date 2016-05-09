import gameEngine
import globalVars
import sys

prize=gameEngine.prize
numberOfQuestions=gameEngine.numberOfQuestions

######### Intro ######################
def introduceYourself():
	globalVars.clearTerminal()
	
	while globalVars.nick=="" or globalVars.nick.isspace() or ',' in globalVars.nick:
		globalVars.nick=raw_input("\n\nPodaj swoj nick (unikaj \",\"): ")
		globalVars.nick=globalVars.nick.strip()

def welcomeMessage():
	globalVars.clearTerminal()
	print globalVars.nick+" witaj w grze POLSCY LOGICY!"
	print "\nZasady gry sa nastepujace:\n"
	print "Na poczatku masz na koncie "+str(prize)+" zl."
	print "Jesli odpowiesz na "+str(numberOfQuestions)+" pytan, dostaniesz nagrode."  
	print "Brzmi prosto, prawda? Jest jednak jeden haczyk...."
	print "Przy kazdej odpowiedzi musisz wpisac kwote obstawiana na dana odpowiedz."
	print "Pieniadze postawione na niepoprawne odpowiedzi zostaja zniszczone (spadaja do niszcarki)."
	print "Istnieje tylko jedna poprawna odpowiedz."
	print "Gra konczy sie kiedy stan konta wyniesie 0 lub kiedy odpowiesz na wszystkie pytania."
	print "o ostatnim pytaniu mozesz zachowac wygrane pieniadze dla siebie"
	print "\nAKTUALNY REKORD: "+gameEngine.printHighestScore()
	print "\nCzy chcesz sprobowac swoich sil w grze? ((R)ozpocznij/(W)yjdz)?\n"
######################################

###### Main ##########################
gameEngine.getLogicFromFiles()
introduceYourself()
welcomeMessage()
while(1):
   	userInput=raw_input()
   	userInput=userInput.upper()
    	if userInput=='R':
   		gameEngine.initGame()
    		break
    	elif userInput=='W':
    		sys.exit(0)
    	else:
    		print "Mozesz wcisnac tylko R lub W !"
########################