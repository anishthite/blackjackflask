from .deck import Deck
from .player import Player, Dealer
import uuid
# import game


class Bot():

    def __init__(self, startingAmount):
        self.deck = Deck()
        self.player = Player(startingAmount)
        self.dealer = Dealer()
        self.id = uuid.uuid4()

    # @classmethod
    # def play(cls, output):
    #     bot = Bot(1000);
    #     while(True):
    #         # blackjack = game.Game(bot.id, bot.player,bot.dealer, Deck(), "bot", Bot.input_betAmount(100))
    #         roundContinue = True;
    #         while(roundContinue):
    #             blackjack.response_init()
    #             blackjack.display()
    #             # roundContinue = blackjack.action(Bot.input_action(game.PlayType.stand))
    #         # Bot.write_to_file(output, blackjack.response)

    # @classmethod
    # def input_betAmount(cls, betAmount):
    #     return betAmount

    # @classmethod
    # def input_action(cls, action):
    #     return action


    # @classmethod
    # def write_to_file(cls, output, response):
    #     output = open(output, "a")
    #     output.write( str(response).strip('[]'))
    #     output.write("\n")
    #     output.close()
    #added a comment

# if __name__ == "__main__":
#     Bot.play("bot.csv")