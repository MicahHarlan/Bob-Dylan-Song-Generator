import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

f = open("corpus.txt")
a = f.read()


a = a.replace("?"," ")
a = a.replace("\n"," ")
a = a.replace('"'," ")
a = a.replace(","," ")
a = a.lower()
a = a.replace("-"," ")
a = a.replace("."," ")
a = a.replace(":"," ")
a = a.replace(";"," ")
a = a.replace("("," ")
a = a.replace(")"," ")
a = a.replace("!"," ")
b = a.split(' ') 

unigrams = {}

for word in b:
	if word != "":
		if unigrams.get(word, "!@#$") == "!@#$":
			unigrams[word] = 1		
		else: 
			num = unigrams[word]
			unigrams[word] = num + 1

key = list(unigrams.keys())
val = list(unigrams.values())
sentence = random.choices(key, weights = val, k = 100) 
str2 =  " ".join(sentence)
#print("UNIGRAMS MODEL")
#print(str2)
bigrams = {}
for i in range(len(b)):
	if b[i] != "" and b[i+1] != "":
		if bigrams.get(b[i],"!@#$") == "!@#$":	
			
			second = {b[i+1] :1}
			bigrams[b[i]] = second
											
		elif bigrams.get(b[i],"!@#$") != "!@#$": 


			temp = bigrams[b[i]]
			if(temp.get(b[i+1],"!@#$") == "!@#$" ):	
				temp[b[i + 1]] = 1
				bigrams[b[i]] = temp	
			else:
				num = temp[b[i+1]]
				temp[b[i+1]] = num + 1	
				bigrams[b[i]] = temp	
			
		elif bigrams.get(b[i][i+1],"!@#$") == "!@#$":
			temp = bigrams[b[i]]




i = 0
uni = random.choices(key,weights = val, k = 1)
nextWord = " ".join(uni)
song = []
while i < 100:

	if bigrams.get(nextWord,"!@#$") == "!@#$":
		uni = random.choices(key,weights = val, k = 1)
		nextWord = " ".join(uni)
	else: 
		temp = bigrams.get(nextWord,"!@#$")
		temp
		key2 = (list(temp.keys() ))
		vals2 = (list(temp.values() ))
		phrase = random.choices(key2, weights = vals2, k = 1)
		song.append(" " + " ".join(phrase)) 
		nextWord = " ".join(phrase)	
		i+= 1	

print("".join(song).strip())

