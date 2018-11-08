#TODO
* create human wrapper function
* create bot wrapper function
* test what happens when it reaches end of deck
* make it so player can stop
* check betamount


#CSV Guide
what data to insert:
Action:
game id, round id, money before round, betAmount,
dealer shown cards, count, player shown cards,count,
action,
===
final dealer cards, count, player cards, count
how much money after round, (if last action) end result


#GAMEFLOW:

1. create session
2. execute rounds of games
    a. init
        - create the metadata to store in csv
        - draw the opening cards for the dealer and the player
    b. loop:
        response_init- generate csventry from metadata
        display- give the dealer hand and player hand (list of cards) to the agent, add the shown hands to response
        action- get response
        - if hit: add one more to player hand, check for bust score_hit (go to close)
        - if stand: cover dealer, score, go to close
    c. close: complete csventry with the play results
