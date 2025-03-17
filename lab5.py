#############################
# APS106 Winter 2025 - lab5 #
# Card Game                 #
#############################

import random

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - DO NOT EDIT
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    cards = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            cards.append([suit,number])

    return cards


def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck


######################
# Part 1 - Deal Card #
######################

def deal_card(hand, deck):
    """
    (list,list) -> None

    Deals a card from the first element in the deck list and add it to the list
    representing the player's hand. This function should remove the first card
    from the deck list and append it to hand list.

    Parameters
    ----------
    hand : list
        List representing the player's hand
    deck : list
        List representing the deck of cards
    """
    # To Do: Complete the function

    hand.append(deck.pop(0))



########################
# Part 2 - Score Cards #
########################

def score_cards(hand):
    """
    (list) -> int

    Calculate the score of the player's hand. The score is the sum of the values
    of the cards in the hand. Number cards are worth their number value, face cards (jack, queen, king)
    are worth 10, and aces are worth 11. If the hand contains an ace and the score
    is greater than 21, the ace should be worth 1 instead of 11.

    Parameters
    ----------
    hand : list
        List representing the player's hand

    Returns
    -------
    int
        The score of the collection of cards in the hand
    """
    # To Do: Complete the function

    score = 0
    ace_counter = 0
    number = []
    f_ace_counter = 0

    for i in range(len(hand)):
        number.append(hand[i][1])
    
    #print("number: ", number) # debugger 

    for i in range(len(number)):

        # Makes all face cards 10 
        if number[i] > 10: 
            number[i] = 10
        
        # Counts the number of aces in the hand 
        if number[i] == 1:
            ace_counter += 1

        # Sums gets the total of the hand 
        score += number[i]
        #print(score)
        # At this point we have all of the numbers in the list and all of the numbers summed up into score 

    #print(number)
    #print(ace_counter)
    #print("this is tot score:", score)

    # Adds 10 to the aces 
    # while the score is below 21 and the number of aces that become 11 is below the number of aces in the hand 
    #add 10 to the score 
    
    while (score <= 11) and (f_ace_counter < ace_counter): 
        score += 10 
        f_ace_counter += 1
            
    #print(score)
    return score

hand = [['clubs',8],['clubs',6],['spades',1]]
print(score_cards(hand))

######################
# Part 3 - Play Game #
######################

def play(shuffled_deck):
    """
    (list) -> [str,int,int]

    Play the card game of with the shuffled deck of cards.

    Parameters
    ----------
    shuffled_deck : list
        List representing the shuffled deck of cards

    Returns
    -------
    list
        A list containing the winner of the game, the dealer's score, and the player's score.
        The winner is a string representing the winner of the game ('player' or 'dealer').
        The dealer's score is an integer representing the score of the player's hand.
        The player's score is an integer representing the score of the dealer's hand.
    """

    # define the player and dealer hands
    player_hand = []
    dealer_hand = []

    # To Do: Complete the function

    #deal cards 
    deal_card(player_hand, shuffled_deck)
    deal_card(dealer_hand, shuffled_deck)
    deal_card(player_hand, shuffled_deck)
    deal_card(dealer_hand, shuffled_deck)

    # deal another card while the players hand is less than 14 
    if score_cards(player_hand) < 14: # CHANGE THE IF STATEMENT
        deal_card(player_hand, shuffled_deck)
        
    # if the players hand is more than 21 lose 
    if score_cards(player_hand) > 21:
        result = ["dealer", score_cards(dealer_hand), score_cards(player_hand)] 
        return result
    
    # while the dealers score is less than that players score deal another card 
    while score_cards(dealer_hand) < score_cards(player_hand):
        deal_card(dealer_hand, shuffled_deck)

    # if the dealer exceeds 21 win 
    if score_cards(dealer_hand) > 21:
        result = ["player", score_cards(dealer_hand), score_cards(player_hand)] 
        return result
    
    if score_cards(player_hand) > score_cards(dealer_hand):
        result = ["player", score_cards(dealer_hand), score_cards(player_hand)]
        return result 
    else: 
        result = ["dealer", score_cards(dealer_hand), score_cards(player_hand)]
        return result 
    

'''
deck = [['diamonds', 7], ['hearts', 6], ['clubs', 8], ['spades', 5],
['spades', 1], ['hearts', 1], ['spades', 6], ['diamonds', 3], ['spades', 10],
['hearts', 11]]
print("deck: ",deck[:10]) # just print the first cards in the deck
result = play(deck)
print("result: ",result)
'''
