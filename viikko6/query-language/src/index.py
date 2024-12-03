from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder
from matchers import HasAtLeast, Or

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    for player in stats.matches(matcher):
        print(player)
    print()

    query2 = QueryBuilder()

    matcher2 = query2.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()

    for player in stats.matches(matcher2):
        print(player)
if __name__ == "__main__":
    main()
