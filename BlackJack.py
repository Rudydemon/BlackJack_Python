import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                    'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
                    'King': 10, 'Ace': 11}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        # The initiaization of the Deck class
        # should be all 52 Card Objects
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                create_card = Card(suit, rank)

                self.all_cards.append(create_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    # print the contents of the deck
    def __str__(self):
        # start with an empty string
        deck_comp = ''
        for card in self.all_cards:
            # add each Card object's print string
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp


class Hand():
    def __init__(self):
        # start with an empty list, same as deck
        self.cards = []
        # start with zero value
        self.value = 0
        # added attribute to keep track of aces
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    # when a hands value goes above 21 but contains an ace,
    # the ace reduces in value from 11 to 1
    def adjust_for_ace(self):
        pass


class Chips():
    def __init__(self):
        # This can be set to a default value or supplied by user input
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet


game_on = True
chips = Chips()

while game_on:
    print('Welcome to BlackJack. We are playing "Dealer stands on all 17s".')
    # first ask the Player to make a bet
    print(f'You have {chips.total} amount to bet.')
    while True:
        try:
            chips.bet = int(input("Please enter how many chips you would like to bet : "))
        except:
            print("I'm sorry. That is not a number. Please try again.")
            continue
        else:
            break
    # Setup Deck
    play_deck = Deck()
    play_deck.shuffle()
    # Setup Player and Dealer Hands
    player = Hand()
    dealer = Hand()
    i = 0
    while i < 2:
        player.add_card(play_deck.deal_one())
        dealer.add_card(play_deck.deal_one())
        i += 1

    print(f'Dealers first card is {dealer.cards[0]}')
    print(f'Players cards are {player.cards[0]} and {player.cards[1]}')
    print(f'Players hand value is {player.value}')

    hit_stay = True
    while hit_stay:
        choice = int(input("Enter 1 to hit, Enter 2 to stay :"))
        if choice == 1:
            # Player hits and gets another card
            player.add_card(play_deck.deal_one())
            print(f'Players cards are {player.cards[0]}, {player.cards[1]}, {player.cards[2]}')
            print(f'Players hand value is {player.value}')
            hit_stay = False
        elif choice == 2:
            hit_stay = False
        else:
            print("That was not a choice. Please try again.")
            continue

    # dealer hit or stay
    if dealer.value < 17:
        dealer.add_card(play_deck.deal_one())
        print("Dealer Hits!")
        print(f'Dealers 2 viewable cards are {dealer.cards[0]} and {dealer.cards[2]}')
    else:
        print("Dealer Stays")

    # comparison
    print("Dealer flips his last card")
    if len(dealer.cards) == 2:
        print(f'Dealers cards are {dealer.cards[0]} and {dealer.cards[1]}')
    else:
        print(f'Dealers cards are {dealer.cards[0]}, {dealer.cards[1]}, and {dealer.cards[2]}')
    print(f'Dealers value is : {dealer.value}')
    print(f'Players value is : {player.value}')
    if (player.value < 22) & ((player.value > dealer.value) or dealer.value > 21):
        print("Player Wins!")
        chips.win_bet
    elif player.value > 21:
        print("Player Busts!")
        chips.lose_bet
    elif player.value <= dealer.value & dealer.value < 22:
        print("House Wins")
        chips.lose_bet

    play_on = int(input("Press 1 to play again. Press anything else to exit : "))
    if play_on == 1:
        continue
    else:
        game_on = False
