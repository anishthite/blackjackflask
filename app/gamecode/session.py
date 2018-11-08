'''
Created on Jul 1, 2018

author: anish
TODO: csv file, bot function, wrapper for people
'''
from deck import Deck as Deck
import player as pl
import enum, uuid
import game
'''
GAME: creates instances of round, holds the init and closing methods

Round: 1 round of BJ, including multiple plays
'''
'''
what data to insert:
Action:
game id, round id, money before round, betAmount,
dealer shown cards, count, player shown cards,count,
action,
===
final dealer cards, count, player cards, count
how much money after round, (if last action) end result

'''

class Session:

    def __init__(self, startingAmount, gameType):
        self.deck = Deck()
        self.player = p1.Player(startingAmount)
        self.dealer = p1.Dealer()
        self.gameType = gameType
        self.id = uuid.uuid4()
    #TODO: def people wrapper
    #roundresult: oldaccount, betmoney, newaccount, dealer card count, player card count

    def game(self,betAmount): #add gameid, roundid, money before,betamount, money after, end result
        this_game = Game(self.id, self.player, self.dealer,self.gameType,betAmount)
        gameLive = True
        while (continuePlay == True):
            continuePlay = this_game.play()#TODO: playtype
        this_round.cover()
        this_round.close()
        return roundResult

    def bot_play(playType):
            global player, dealer
        if (playType == "hit" or playType == "h"):
            deck.draw(1, player.hand)
            dealer.show()
            player.show()
            score_hit()
            return True
        if (playType == "stand" or playType == "s"):
            return False
    def player_play():
        global player, dealer
        playType = ""
        while (playType != "hit" and playType != "h" and playType != "stand" and playType != "s"):
            playType  = input("Would you like to hit, or stand").lower()
        if (playType == "hit" or playType == "h"):
            deck.draw(1, player.hand)
            dealer.show()
            player.show()
            score_hit()
            return True
        if (playType == "stand" or playType == "s"):
            return False

    def main_method():
        global player, deck, dealer, betAmount
        #setup
        setup()
        #loop
        print('Shuffling cards (1 deck)')
        gameLive = True
        while (gameLive == True):
            #dealer puts your cards
            print('Player Balance: ' + str(player.cash))
            betAmount = 0
        #dealer puts their cards
            deck.draw(2, dealer.hand)
            dealer.show()
            deck.draw(2,player.hand)
            player.show()
        #you bet
            bet()
        #you decide to get one more card
            continuePlay = True
            playerplaying = True
            while (continuePlay == True and playerplaying == True):
                continuePlay = player_play()
        #dealer takes the cards as they add up to at least 17
            cover()
            score()
            close()
if __name__ == "__main__":
    main_method()