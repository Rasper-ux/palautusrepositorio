from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table
from rich.prompt import Prompt


def main():
    print("NHL statistics by nationality")
    print()
    season = Prompt.ask("Enter season", choices=["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25"])
    nationality = Prompt.ask("Enter nationality", choices=["AUT","CZE","AUS","SWE","GER","DEN","SUI","SVK","NOR","RUS","CAN","LAT","BLR","SLO","USA","FIN","GBR"])

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Top scorers of {nationality} season {season}")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold yellow")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    print(table)

if __name__ == "__main__":
    main()
