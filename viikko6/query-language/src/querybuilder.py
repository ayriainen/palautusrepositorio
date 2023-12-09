from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self._rules = []
    
    def build(self):
        if len(self._rules) == 0:
            return All()
        elif len(self._rules) == 1:
            return_rules =  self._rules[0]
        else:
            return_rules = And(*self._rules)
        
        self._rules = []
        return return_rules

    def playsIn(self, team):
        self._rules.append(PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self._rules.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._rules.append(HasFewerThan(value, attr))
        return self
    
    def oneOf(self, *queries):
        self._rules.append(Or(*queries))
        return self
