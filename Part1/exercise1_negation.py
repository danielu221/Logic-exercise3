#!/usr/bin/python
# 
#

import sys
arguments = [int(i) for i in sys.argv[1:]]

if len(arguments)<6:
	print """\nJestes przed wejsciem na najniebezpiecznejsza kolejke gorska na swiecie.\n W linii komend podaj nastepujace dane:
	\n1)wzrost (w cm) 2)wage (w kg) 3)dlugosc wlosow (w cm)\n4)Wiek 5)Rozmiar buta (miara Europejska 6)Obwod w pasie (w cm)\n"""
else:
	height = arguments[0]
	weight = arguments[1]
	hairLength = arguments[2]
	age = arguments[3]
	shoeSize = arguments[4]
	waistline = arguments[5]

	if( ( height <=150 or height>=200) or (weight<=50 or weight>=120) or hairLength>=100 or (age<=18 or age>=75) or shoeSize<=35 or (waistline<=60 or waistline>=120) ):
  		print 1
	else:
  		print 0
