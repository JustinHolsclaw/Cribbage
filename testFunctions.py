from gameRules import gameRules
from Deal_Shuffle import Deal_Shuffle

def test_rules():
    rules = gameRules()
    deal = Deal_Shuffle()
    assert rules.isFifteen(hand = [1,2,2,10,5] ) == 2, "should be 2"
    assert rules.isPair(hand = [1,2,2,10,5] )== 2, "Points should be 2"
    assert deal.CreateDeck() == 52, "not 52"

