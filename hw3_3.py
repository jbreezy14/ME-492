#Jabril Cross-Ellis
#ME 492
#HW 3 - 3 

from matplotlib.pyplot import*
from numpy import *

VOWELS = ['a','e','i','o','u']

oword = raw_input("What is the word: ")
nword = oword[1:]
nletter = oword[:1]

if nletter in VOWELS: 
	latin = "hay"
	tran = oword+latin
else:
	latin = "ay"
	tran = nword+nletter+latin 

print "in pig latin "+tran+"!"
