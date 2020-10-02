#Justin Holsclaw 9/30/2020 This is the beginnings of the Cribbage Program

class gameRules():
   def IsFifteen(self, Value, Value1):
      fifteen = Value + Value1
      return fifteen

   def IsPair(self, card, card2):
       PairStatus = False
       if card == card2:
        PairStatus = True
        return PairStatus
      
   def isRun(self, hand):
      sortedHand = hand.sort()
      x = 0
      pairs = 0
      def isEqual(self):
         if sortedHand[x].value+1 == sortedHand[x+1]:
            x=x+1
            pairs= pairs +1
            isEqual(self)
         else:
            if x == 2:
               re