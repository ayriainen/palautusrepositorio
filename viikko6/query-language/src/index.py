from statistics import Statistics
from player_reader import PlayerReader
#Tämän voisi poistaa, mutta olkoot molemmat tehtävät nyt näkyvillä sellaisenaan kuin ohjeistettu.
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from querybuilder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()

    print("HasAtLeast, PlaysIn:")
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nNot:")
    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nHasFewerThan:")
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nAll:")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("\nOr 1:")
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nOr 2:")
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nQueryBuilder all:")
    matcher = query.build()
    filtered_with_all_querybuilder = stats.matches(matcher)
    print(len(filtered_with_all_querybuilder))

    print("\nQueryBuilder playsIn:")
    matcher = (
      query
          .playsIn("NYR")
          .build()
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nQueryBuilder hasAtLeast, hasFewerThan:")
    matcher = (
      query
          .playsIn("NYR")
          .hasAtLeast(10, "goals")
          .hasFewerThan(20, "goals")
          .build()
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nQueryBuilder oneOf:")
    m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
    )
    m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
    )
    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
