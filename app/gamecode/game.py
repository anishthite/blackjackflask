import enum, uuid

class Result(enum.Enum):
    """ Possible results for a round    """
    playerBusted = "You got Busted"
    dealerBusted = "The Dealer got Busted"
    dealerMore = "The Dealer had more than you"
    playerMore = "You had more than the Dealer"
    draw = "Congratulations, you drew. Should've bought a lottery ticket with that luck"

    def get_name(self):
        return self.name

class PlayType(enum.Enum):
    """ Possible types of plays    """
    hit = 0
    stand = 1

    def get_name(self):
        return self.name

class Game:
    """ One round of a Blackjack game, """

    def __init__(self, session_id, player, dealer,deck, gameType,betAmount):
        """ Creates the round, and draws 2 cards from the deck
            for the dealer, and 2 cards for the player. Also creates
            response to input in  csv"""
        self.response = []
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.gameType = gameType
        self.betAmount = betAmount
        self.id = uuid.uuid4()
        self.session_id = session_id
        self.result = None

        #draw cards
        self.deck.draw(2, self.dealer.hand)
        self.deck.draw(2, self.player.hand)

    def response_init(self):
        self.response.clear()
        self.response.extend((str(self.session_id), str(self.id), self.player.cash, self.betAmount))

    def display_final(self):
        self.response.extend(('-'.join(str(item) for item in self.dealer.show_final()), self.dealer.count()))
        self.response.extend(('-'.join(str(item) for item in self.player.show()), self.player.count()))
        return self.dealer.show_final(), self.player.show()
    def display(self):
        self.response.extend(('-'.join(str(item) for item in self.dealer.show()), self.dealer.count()))
        self.response.extend(('-'.join(str(item) for item in self.player.show()), self.player.count()))
        return self.dealer.show(), self.player.show()

    def action(self, playType):
        self.response.append(playType.get_name())
        if (playType == PlayType.hit):
            self.deck.draw(1, self.player.hand)
            return self.score_hit()
        self.cover()
        return False

    def score_hit(self):
        if (self.player.count() > 21):
            self.dealer_wins()
            self.close(Result.playerBusted)
            return False
        return True

    def score(self):
        playerCount = self.player.count()
        dealerCount = self.dealer.count()
        if (playerCount > 21):
            self.dealer_wins()
            self.close(Result.playerBusted)
        elif (dealerCount > 21):
            self.player_wins()
            self.close(Result.dealerBusted)
        elif (dealerCount > playerCount):
            self.dealer_wins()
            self.close(Result.dealerMore)
        elif (playerCount > dealerCount):
            self.player_wins()
            self.close(Result.playerMore)
        else:
            self.close(Result.draw)

    def cover(self):
        while (self.dealer.count() < 16):
            self.deck.draw(1, self.dealer.hand)
        if (self.gameType == "human"):
            print(self.display_final())
        else:
            self.display_final()
        self.score()

    def close(self, result):
        if self.gameType == "human":
            print(result.value)
            print("You have " + str(self.player.cash) + " credits remaining.")
            print("This is equal to "+ str(self.player.cash/9999999999) + " dollars. You are now immensely rich.")
        self.result = result.value
        self.response.extend((self.player.cash, result.get_name()))
        self.dealer.hand.clear()
        self.player.hand.clear()

    def player_wins(self):
        self.player.cash += int(self.betAmount)

    def dealer_wins(self):
        self.player.cash -= int(self.betAmount)

    def get_response(self):
        return self.response