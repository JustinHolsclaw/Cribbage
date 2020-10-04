import random
class Deal_Shuffle():
    
    def CreateDeck(self):
        def CreateSuitLength(self):
            suit = []
            suitLength = 0
            while len(suit) < 13:
                suitLength = len(suit)
                suit.append(suitLength) #suit is now populated with 12 cards
            return suit

        def DefineSuit(self): #Create a list of 52 dictionaries, each defining a singular card
            thisSuit = CreateSuitLength(self)
    
            def addSpades(n):
                dictItem = {
                "Suit": "Spades",
                "Value": n+1
                }
                return dictItem
            def addClubs(n):
                dictItem = {
                "Suit": "Clubs",
                "Value": n+1
                }
                return dictItem
            def addHearts(n):
                dictItem = {
                "Suit": "Hearts",
                "Value": n+1
                }
                return dictItem
            def addDiamonds(n):
                dictItem = {
                "Suit": "Diamonds",
                "Value": n+1
                }
                return dictItem
            orderedDeck = []
            Spades = []
            Clubs = []
            Hearts = []
            Diamonds = []
            Spades = list(map(addSpades, thisSuit)) #Using the map function
            Clubs = list(map(addClubs, thisSuit))
            Hearts = list(map(addHearts, thisSuit))
            Diamonds = list(map(addDiamonds, thisSuit))
            counter = 0
            while counter < len(Spades):
                orderedDeck.append(Spades[counter])
                orderedDeck.append(Hearts[counter])
                orderedDeck.append(Clubs[counter])
                orderedDeck.append(Diamonds[counter])
                counter = counter+1
            return orderedDeck

        Deck = DefineSuit(self)
        return Deck
        

    def DealAndShuffle(self):
        Deck = Deal_Shuffle().CreateDeck() #Creates the Deck
        random.shuffle(Deck)#this shuffles the deck
        dealCount = 0
        hand1 = []
        hand2 = []
        while dealCount < 12:
            if dealCount == 0 or dealCount == 2 or dealCount == 4 or dealCount == 6 or dealCount == 8 or dealCount == 10:
                hand1.append(Deck.pop())
                dealCount = dealCount+1
            else: 
                hand2.append(Deck.pop())
                dealCount = dealCount+1

        ShuffledHand = []
        count = 0
        while count < len(hand1):
            ShuffledHand.append(hand1[count])
            ShuffledHand.append(hand2[count])
            ShuffledHand.append(Deck.pop())
            count = count + 1

        return ShuffledHand
            

