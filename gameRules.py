#Justin Holsclaw 9/30/2020 This is the beginnings of the Cribbage Program
from functools import reduce
class gameRules():
   def isFifteen(self, hand): # Needs to be changed so that it adds more than two numbers together
      points = 0
      x=0
      y=1
      while x < 5:
         if y < 5:
            z = lambda a,b: hand[a] + hand[b]
            if  z(x,y) == 15:
               points = points + 2
               y= y+1
            else:
               y= y+1

         else:
            x = x+1
            y = x+1
      print(points)  
      return points

   def isPair(self, hand):
      points = 0
      x = 0
      y = 1
      while x < 5:
         if y < 5:
            if hand[x] == hand[y]:
               points = points + 2
               y= y+1
            else:
               y= y+1

         else:
            x = x+1
            y = x+1 
      return points
      
   def isRun(self, hand): # This Function still needs some work it is not returning the right value
      points = 0
      hand.sort()
      x = 0
      while x < 4:
         if hand[x]+1 == hand[x+1]:
            points = points+1
            x = x+1
         else: 
            x= x+1
      return points+1

     
   def totalPoints(self, hand): #This returns the total of all of the point making functions.
      pointTotal = [gameRules().isRun(hand), gameRules().isPair(hand), gameRules().isFifteen(hand)]
      points = reduce((lambda x, y: x+y), pointTotal)
      return points
      
