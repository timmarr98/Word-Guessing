import random
import time as t
import threading
import pygame as pgame
from scrabbleWordsDict import scrabbleWords
import collections

seconds = 5

#Array that will be randomly pulled from (by index) for scrabble like annagram
alphabet = ['b','c','d','f','g','h','i','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
anagrams = []
alphaScore = {'a' : 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'g': 2 ,'h': 4,'i': 1,'j': 8,'k': 5,'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,'q':10,'r': 1,'s':1,'t': 1,'u': 1,'v': 4,'w':4,'x': 8,'y':4,'z':10}
anagramString = ""
player1 = True
playerScore = 0
playerText = ''
textRectangle = pgame.Rect(330,500,100,30)
dic = {}
dic2 = {}
scrabbleDictionary = {}
anagramCount = collections.Counter()
scoreKeep = 0
level = 1
count = 0

# txtFile = open('ScrabbleWords.txt','r')
# lines = txtFile.readlines()

# for line in lines:
#     print(line.strip())
#     scrabbleDictionary[line.strip()] = 1
# print(scrabbleDictionary)
# print('Done') 

pgame.init()
screen = pgame.display.set_mode((800,800))


def main():
    global playerText
    global playerScore
    global anagramCount
    global screen
    global scoreKeep
    global level
    global count

    messageDisplay = ""
    gray = pgame.Color('gray19')
    blue = pgame.Color('dodgerblue')
    font = pgame.font.Font(None,40)

    done = False
    intro = True #The intro screen before playing
    flag = True #if the word is valid
    gameOver1 = False
    flagger = False
    while intro:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                intro = False
                break
            if event.type == pgame.MOUSEBUTTONDOWN:
                done = True
                intro = False
        screen.fill(gray)
        gamename = font.render("WORD FINDER!", True, blue)

        clickwhere = font.render("CLICK ANYWHERE TO START", True, blue)
        text_rect_center = clickwhere.get_rect(center = (400,600))
        text_welcome_center = gamename.get_rect(center = (400,300))
        screen.blit(clickwhere, text_rect_center)
        
        screen.blit(gamename, text_welcome_center)
        pgame.display.flip()


    clock = pgame.time.Clock()
    seconds = 30 #change this for testing
    dt = 0

    while done:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                done = False
                break
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_RETURN:
                    anagramCount = collections.Counter(anagramString)
                    for x in playerText:
                        if x not in anagramCount or anagramCount[x] <1:
                            print("TRY AGAIN!")
                            flag = False
                        anagramCount[x] -= 1
                    
                    if playerText not in dic2 and flag and playerText in scrabbleWords:
                        playerScore += scrabbleWords[playerText]
                        dic2[playerText] = 1
                        messageDisplay = f'{playerText} has given {scrabbleWords[playerText]} points!'
                        playerText= ""
                        flagger = True
                    else:
                        messageDisplay = f'{playerText} is not a word!'

                    flag = True
                    
                if event.key == pgame.K_BACKSPACE:
                    playerText = playerText[:-1]
                else:
                    if event.key != pgame.K_RETURN:
                        playerText += event.unicode
        seconds -=dt
        if seconds <= 0:
            messageDisplay= ""
            anagram()
            seconds = 30
            scoreKeep = 0
            done = False
            gameOver1= True
            # break
        
        if playerScore > scoreKeep:
            if flagger == True:
                seconds = 30
                anagram()
                flagger = False
            

        # if seconds <=0 and scoreKeep


        screen.fill(gray)
        pgame.draw.rect(screen, blue, textRectangle,2)
        txt = font.render(str(round(seconds,2)),True,blue)
        inputText = font.render(playerText, True, blue)
        anagramz = font.render(anagramString, True, blue)
        playersScore = font.render(str(playerScore),True, blue)
        playerMessage = font.render(messageDisplay, True, blue)
        text_player_message = playerMessage.get_rect(center = (400,600))

        levelScore = font.render(str(scoreKeep),True, blue)
        text_level_score = levelScore.get_rect(center = (400,100))
        screen.blit(levelScore,text_level_score )


        screen.blit(playerMessage, text_player_message)
        screen.blit(inputText, (textRectangle.x + 5, textRectangle.y + 3))
        screen.blit(anagramz, anagramz.get_rect(center = (400,200)))
        screen.blit(playersScore, (500,500))
        screen.blit(txt, (50,50))
        pgame.display.flip()
        textRectangle.w = max(100, inputText.get_width() + 10)
        dt = clock.tick(30)/1000
    while gameOver1:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                gameOver1 = False
                break
        screen.fill(gray)
        gameOver = font.render("GAME OVER", True, blue)
        text_game_over  = gameOver.get_rect(center = (400,400))
        screen.blit(gameOver, text_game_over)
        pgame.display.flip()


def anagram():
    #the number of letters in the anagram
    i = 0
    global anagramString
    global anagramCount
    global scoreKeep
    anagramString = ""
    anagramCount = collections.Counter()
    while i <8:
        if i == 2 or i == 5 or i == 7:
            randoIndex = vowels[random.randrange(0,len(vowels)-1)]
            anagrams.append(randoIndex)
            scoreKeep += alphaScore[randoIndex]
            anagramString = anagramString + randoIndex + " "
        else:
            randoIndex = alphabet[random.randrange(0,len(alphabet)-1)]
            scoreKeep += alphaScore[randoIndex]
            anagramString = anagramString + randoIndex + " "
   
        i+=1

def playScrambler():
    anagram()

# def secondsLeft():
#     for i in range(seconds):
#         print(str(seconds-i) + " seconds left ")
#         t.sleep(1)
#     print("Game is over, your score is {playerScore}" )

if __name__ == '__main__':
    playScrambler()
    main()
    pgame.quit()



