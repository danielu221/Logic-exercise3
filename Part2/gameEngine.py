from random import shuffle
import sys
import time
import globalVars

###### Initial conditions ############
nick=globalVars.nick
filePaths=globalVars.filePaths
numberOfQuestions=5
prize=1000000
######################################

###### Logic  ########################
andList=list()
orList=list()
implList=list()
notList=list()

def getLogicFromFile():
	globalVars.getArguments()
	with open(filePaths['--and'],'r') as f:
		k=0
		for line in f:
			if line!="\n":
				line=line.strip(' ').replace(' ','')
				andList.append([])
				for c in line[:3]:
					andList[k].append(c)
				k+=1

	with open(filePaths["--or"],'r') as f:
		k=0
		for line in f:
			if line!="\n":
				line=line.strip(' ').replace(' ','')
				orList.append([])
				for c in line[:3]:
					orList[k].append(c)
				k+=1

	with open(filePaths["--impl"],'r') as f:
		k=0
		for line in f:
			if line!="\n":
				line=line.strip(' ').replace(' ','')
				implList.append([])
				for c in line[:3]:
					implList[k].append(c)
				k+=1

	with open(filePaths["--not"],'r') as f:
		k=0
		for line in f:
			if line!="\n":
				line=line.strip(' ').replace(' ','')
				notList.append([])
				for c in line[:2]:
					notList[k].append(c)
				k+=1

def orResult(x1,x2):
	for p,q,r in orList:
		if p==x1 and q==x2:
			return r

def andResult(x1,x2):
	for p,q,r in andList:
		if p==x1 and q==x2:
			return r

def implResult(x1,x2):
	for p,q,r in implList:
		if p==x1 and q==x2:
			return r

def notResult(x1):
	for p,r in notList:
	  	if p==x1:
			return r


def answer(logicResult):
	if logicResult=='1':
		return 'A'
	if logicResult=='0':
		return 'B'
	if logicResult=='x':
		return 'C'

getLogicFromFile() 

questions =[
			("""Wloczega chodzi po parku i stwierdza, 
ze nie posiada papierosow. Poniewaz jest wloczega,
nie ma rowniez pieniedzy. 
Ale od czegoz jest glowa? Nasz wloczega zaczyna zbierac niedopalki.
Bibulke ma w kieszeni, a doswiadczenie go uczy, ze z siedmiu 
niedopalkow mozna zrobic jednego papierosa.
Po pewnym czasie uzbieral 49 niedopalkow.
Wloczega ma bardzo regularne przyzwyczajenia i 
pali jednego papierosa dokladnie co 3 kwadranse.
Na ile czasu wystarczy mu uzbierany zapas?\n""",'A)6h','B)5h 15min','C)1h 45min','A'), #last element is an answer
			
			("""Z burty statku zwiesza sie drabinka sznurowa w ten sposob, 
ze ledwie dosiega powierzchni wody. 
Szczeble drabinki rozmieszczone sa w odleglosci 25 centymetrow.
Ile szczebli znajdzie sie pod woda, gdy
podczas przyplywu morza woda podniesie sie o 90 centymetrow?\n""",'A)4','B)5','C)0','C'),
			
			("""Masz trzy torby: A, B, C. 
Na pierwszej masz napisane "JABLKA I POMARANCZE", 
na drugiej "JABLKA", a na trzeciej "POMARANCZE". 
Wszystkie etykiety sa niepoprawne. 
Twoim zadaniem jest poprawne rozmieszczenie etykiet na torbach. 
Mozesz jednak tylko raz siegnac do jednej z toreb i wyciagnac jeden owoc. 
Nie wolno zagladac do pozostalych toreb.
Siegasz do torby A i wyciagasz pomarancze.
\nJak powinny byc rozmieszczone pomarancze? \n""",'A) A-JABLKA I POMARANCZE, B-POMARANCZE, C-JABLKA',
'B)Nie da sie ustalic','C)A-POMARANCZE, B-JABLKA I POMARANCZE, C-JABLKA','C'),

 			("""x(stan nieokreslony)
\nJaka jest wartosc logiczna dla zdania:
~(1 & x) v (0 & x)?\n""",'A)1','B)0','C)X',answer (orResult(  notResult( andResult('1','x') ), andResult('0','x') ) ) ),

 			("""x(stan nieokreslony)
\nJaka jest wartosc logiczna dla zdania:
~(1 v x) v (x & x)?\n""",'A)1','B)0','C)X',answer (orResult(  
 																notResult( orResult('1','x') ), 
 																andResult('x','x') ) ) 
															),

 			("""Jaka jest wartosc logiczna dla zdania:
(0 v 1) => 1 ?\n""",'A)1','B)0','C)X',answer( implResult(orResult('0','1'), '1'  ) ) ),

 			("""x(stan nieokreslony)
\nJaka jest wartosc logiczna dla zdania:
(x=>(1 v 0)) v (1 v x)  ?\n""",'A)1','B)0','C)X',answer(orResult( 
 																    implResult( 'x',orResult('1','0') ),
 																	orResult('1','x')))
																),

 			("""x(stan nieokreslony)
\nJaka jest wartosc logiczna dla zdania:
(x & (1 v x))  v  ((1=>x)&(1 v x))  ?\n""",'A)1','B)0','C)X',answer(orResult( 
 																				andResult( 'x',orResult('1','x') ),
 																				andResult(implResult('1','x'),orResult('1','x'))))
																			)
		
]
######################################


###### Game mechanism ############

def isPossibleBet(bet,currentPrize):
	if(bet>=0 and bet<=currentPrize):
		return True
	else:
		return False

def singleBet(bet,currentPrize):
	if isPossibleBet(bet,currentPrize):
		currentPrize-=bet
		print "\nPozostala kwota do obstawienia: "+str(currentPrize)+"zl\n"
		return True
	else:
		print 'Podano niepoprawna kwote do obstawienia.'
		return False

def waitingText(lines,timeSleep):
	for waiting in range(lines):	
			time.sleep(timeSleep)
			print '.....'

def initGame():
	shuffle(questions)
	global prize
	global numberOfQuestions
	global nick
	i=1
	for question,ans1,ans2,ans3,goodAnswer in questions[:numberOfQuestions]:
		globalVars.clearTerminal()
		print "\nAktualny STAN KONTA TO: "+str(prize)+" zl"
		print "\nPYTANIE "+str(i)+" z "+str(numberOfQuestions)
		if i==numberOfQuestions:
			waitingText(3,1)
			print "TO JUZ FINALOWE PYTANIE! SKUP SIE!"
			waitingText(3,1)
		print "\n"+question+'\n'+ans1+'\n'+ans2+'\n'+ans3+'\n'
		print "\nObstaw odpowiednia odpowiedz."

		flagA=False
		flagB=False
		while(flagA!=True):
			betA=raw_input("A) ")
			if betA.isdigit():
				betA=int(betA)
				flagA=singleBet(betA,prize)
			else:
				print "\nPodano nieobslugiwany ciag znakow.Popraw sie"

		while(flagB!=True):
			betB=raw_input("B) ")
			if betB.isdigit():
				betB=int(betB)
				flagB=singleBet(betB,prize-betA)
			else:
				print "\nPodano nieobslugiwany ciag znakow.Popraw sie"	

		print "Na odpowiedz C stawiasz "+str(prize-betA-betB)+" zl\n\n"
		betLast=prize-betA-betB

		if goodAnswer=='A':
			prize=betA
		elif goodAnswer=='B':
			prize=betB
		else:
			prize=betLast
		
		waitingText(3,1)	
		print 'Poprawna odpowiedz to: '+ goodAnswer
		if(prize>0 and i!=numberOfQuestions):
			print '\nPo Twoim obstawianiu pozostaje Ci do wygrania '+str(prize)+"zl"
			raw_input("\nNacisnij ENTER, aby przejsc dalej...")
			i+=1
		elif (prize>0 and i==numberOfQuestions):
			print "\nBRAWO "+nick+", to bylo ostatnie pytanie. TWOJA WYGRANA TO: "+str(prize)+"zl!!!"
		else:
			print "Niestety, na twoim koncie nic juz nie ma. Przegrywasz."
			break

######################################


