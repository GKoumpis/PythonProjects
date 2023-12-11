# -*- coding: cp1253 -*-
import random
import string

a = [["None"]*100 for _ in range(100)]
b = []

for i in range(100):
    for j in range(100):
        if a[i][j] == "None":
            a[i][j] = random.choice(string.ascii_uppercase)

print "-----------------------------------------------WORDSEARCH-----------------------------------------------"            
print " ______________________________________________________________________________________________________"
print "|                                                                                                      |"
for k in range(100):
    line = "| "
    for l in range(100):
        line = line + a[k][l]
    line = line + " |"
    print line
print "|______________________________________________________________________________________________________|"    

f = open("american-english.txt","r")
for LineCnt in range(99171):
    word = f.readline()
    for m in range(100):
        for n in range(100):
            if (word[0] == a[m][n]):
                if (m + len(word) <= 100):
                    success = 1
                    LetterCnt = 1
                    while ((LetterCnt <= len(word)) and (success == 1)):
                        if (word[LetterCnt] != a[m + LetterCnt][n]):
                            success = 0
                        LetterCnt += 1
                    if (success == 1):
                        b.append(word)
                if (n + len(word) <= 100):
                    success = 1
                    LetterCnt = 1
                    while ((LetterCnt <= len(word)) and (success == 1)):
                        if (word[LetterCnt] != a[m][n + LetterCnt]):
                            success = 0
                        LetterCnt += 1
                    if (success == 1):
                        b.append(word)
                        
if (len(b) == 0):
    print "There are no results."
else:
    print "The words are:"                        
    print b                        
                            
f.close()
                            
                            
                           
                            
                        
                
                
                
                   
                   
               


    
