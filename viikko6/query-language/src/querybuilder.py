from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self.matchers = []

    def plays_in(self, team):
        self.matchers.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return self

    def one_of(self, *matchers):
        for i in matchers:
            print(i)
            self.matchers.append(i)
        return self

    def build(self):
        if not self.matchers:
            return All()
        return And(*self.matchers)
