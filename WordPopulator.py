
# from guessingwords import scrabbleDictionary
# from guessingwords import alphaScore


# txtFile = open('guessingScrabble\ScrabbleWords.txt','r')
# lines = txtFile.readlines()
# wordFile = open('guessingScrabble\scarbbleWordsDict.txt','w')
# words = []
# def scrabblePoints(word):
#     playerScore = 0
#     for x in word:
#         playerScore += alphaScore[x]
#     return playerScore

# for line in lines:
#     line = line.lower()
#     words.append(line.strip())
#     scrabbleDictionary[line.strip()] = scrabblePoints(line.strip())


# for y in words:
#     wordFile.write(f'"{y}" : {scrabbleDictionary[y]}, \n')

# txtFile.close()
# wordFile.close()

# # print(scrabbleDictionary)
# print('Done') 




# alphaScore = {'a' : 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'g': 2 ,'h': 4,'i': 1,'j': 8,'k': 5,'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,'q':10,'r': 1,'s':1,'t': 1,'u': 1,'v': 4,'w':4,'x': 8,'y':4,'z':10}