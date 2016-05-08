import os
import sys 

nick=""
fileNames=("not.txt","and.txt","impl.txt","or.txt")
options=("--not","--and","--impl","--or")
filePaths={
			'--and':'asdsd',
			'--or':'',
			'--not':'',
			'--impl':''
			}

########## Loading files #############
def getArguments():
	if len(sys.argv)!=9:
		printHelp()
		sys.exit()
	i=1
	for arg in sys.argv[1:]:
		 	if i%2==1:
		 		if arg not in options:
		 			printWrongOption(arg)
		 			sys.exit()
		 		else:
		 			filePaths[arg]=sys.argv[i+1]
		 	elif i%2==0:
		 		if getFilenameFromPath(arg) not in fileNames:
		 			printWrongFilename(arg)
		 			sys.exit()
		 	i+=1

def getFilenameFromPath(pathString):
	return os.path.basename(pathString)


def printOptions():
	for option in options:
		print option

def printFileNames():
	for f in fileNames:
		print f

def printWrongOption(wrongOption):
	print "Opcja "+"'"+wrongOption+"'"+" nie istnieje."
	print "Upewnij sie, ze wpisales opcje, a potem nazwe pliku"
	print "Zaimplementuj wszystkie opcje :"
	printOptions()

def printWrongFilename(wrongFilename):
 	print "Plik o nazwie "+"'"+wrongFilename+"'"+" nie zostal zdefiniowany w programie."
 	print "Upewnij sie, ze wpisales opcje, a potem nazwe pliku"
 	print "Pliki, z ktorych mozesz skorzystac: "
 	printFileNames()

def printHelp():
	print "BLAD, przeczytaj ponizsza instrukcje."
	print "\nUruchamianie: python main.py opcja1 plik1 opcja2 plik2..."
	print "Pamietaj, ze do poprawnego dzialania gry musisz najpierw wpisac opcje,"
	print "a nastepnie odpowiadajacy jej plik."
	print "Musisz wykorzystac wszystkie opcje: "
	printOptions()
	print "A takze wszystkie odpowiadajace im pliki: "
	printFileNames()
	print "\nPoprawne uzycie: \n\tpython main.py --and and.txt --or or.txt --impl impl.txt --not not.txt\n"
######################################

def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear')