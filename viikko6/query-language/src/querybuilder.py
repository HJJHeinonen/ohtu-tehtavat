from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All
class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matchers = matcher
    
    def build(self):
        return self._matchers

    def playsIn(self, team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matchers, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matchers, HasFewerThan(value, attr)))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))