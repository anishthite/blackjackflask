from .deck import Deck
from .game import Game, PlayType
from .bot import Bot

class Human(Bot):

    def __init__(self, cash):
        super().__init__(1000)
        self.blackjack = None

    def get_cash(self):
        return self.player.cash

    def create_game(self, betAmount):
        self.blackjack = Game(self.id, self.player, self.dealer, Deck(), "human", betAmount)

    def response(self):
        self.blackjack.response_init()
        self.dealerhand, self.playerhand = self.blackjack.display()

    def display_dealer(self):
        return self.dealerhand

    def display_player(self):
        return self.playerhand

    def display_result(self):
        return self.blackjack.result

    def action(self, inputAction):
        return self.blackjack.action(inputAction)

    def convert(self, action):
        if action == 'hit':
            return PlayType.hit
        if action == 'stand':
            return PlayType.stand

    def write_to_file(self, outputfile):

        with open(outputfile, "a") as output:
            print(self.blackjack.response)
            output.write("test")
            output.write(str(self.blackjack.response).strip('[]'))
            output.write("\n")
            output.flush()
            output.close()
#     @classmethod
#     def play(cls, output):
#         human = Human(1000)
#         while(True):
#             blackjack = game.Game(human.id, human.player, human.dealer, Deck(), "human", Human.human_input_betAmount())
#             roundContinue = True
#             while(roundContinue):
#                 blackjack.response_init()
#                 print(blackjack.display())
#                 roundContinue = blackjack.action(Human.human_input_action())
#             Human.write_to_file(output, blackjack.response)

#     def human_input_betAmount(self, betamount):
#         return betamount

#     @classmethod
#     def human_input_action(cls):
#         action = input("Hit or Stand: ")
#         if action.lower() == "hit" or action.lower() == "h":
#             return game.PlayType.hit
#         if action.lower() == "stand" or action.lower() == "s":
#             return game.PlayType.stand
#         return Human.human_input_action()


# if __name__ == "__main__":
#     Human.play("human.csv")