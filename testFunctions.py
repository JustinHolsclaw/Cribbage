from gameRules import gameRules

def test_rules():
    rules = gameRules()
    assert rules.IsFifteen(10, 5) == 15, "should be 15"
    assert rules.IsPair(5,5)== True, "Not a pair"