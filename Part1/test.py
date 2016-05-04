#!/usr/bin/python
#
#
import sys
import subprocess
import os 

height = [188,120,190,165,199,202,175,164,192,182]
weight = [79,30,100,63,92,100,71,55,130,91]
hairLength = [8,10,120,70,1,12,3,78,2,43]
age = [23,10,20,30,33,44,19,78,52,64]
shoeSize = [44,30,42,38,46,45,41,39,42,43]
waistline = [88,58,97,88,92,95,76,85,109,92]
result=[1,0,0,1,1,0,1,0,0,1]
result_neg=[0,1,1,0,0,1,0,1,1,0]

def test_exercise1():
	for ind in range(len(result)):
  		out="python exercise1.py"+" "+str(height[ind])+" "+str(weight[ind])+" "+str(hairLength[ind])+" "+str(age[ind])+" "+str(shoeSize[ind])+" "+str(waistline[ind])
  		print "\ninput: "+str(height[ind])+" "+str(weight[ind])+" "+str(hairLength[ind])+" "+str(age[ind])+" "+str(shoeSize[ind])+" "+str(waistline[ind] )
  		print "output actual: "
  		subprocess.call(out,shell=True)
  		print "output expected: "+str(result[ind])+"\n\n"
 
def test_exercise1_negation():
	for ind in range(len(result)):
  		out="python exercise1_negation.py"+" "+str(height[ind])+" "+str(weight[ind])+" "+str(hairLength[ind])+" "+str(age[ind])+" "+str(shoeSize[ind])+" "+str(waistline[ind])
  		print "\ninput: "+str(height[ind])+" "+str(weight[ind])+" "+str(hairLength[ind])+" "+str(age[ind])+" "+str(shoeSize[ind])+" "+str(waistline[ind] )
 		print "output actual: "
  		subprocess.call(out,shell=True)
  		print "output expected: "+str(result_neg[ind])+"\n\n"


if len(sys.argv) < 2:
	print("Wywolanie: python test.py [nazwa testowanego pliku]")
	sys.exit()
if sys.argv[1] == 'exercise1.py':
	test_exercise1()
elif sys.argv[1] == 'exercise1_negation.py':
	test_exercise1_negation()
else:
	print "Niepoprawna nazwa pliku"

