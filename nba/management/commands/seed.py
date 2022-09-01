# from nba.models import Player, Stat
import pandas as pd
from django.core.management.base import BaseCommand
from nba.models import Player



players = pd.read_csv("./data/players.csv")
player_stats = pd.read_csv("./data/player_stats.csv")


def seed_player():
    
  for index in players.index:
    player = Player(
    player_id  = players.loc[index, "player_id"],
    player  = players.loc[index, "player"],
    birth_year = players.loc[index, "birth_year"],
    hof = players.loc[index, "hof"],
    num_seasons = int(players.loc[index, "num_seasons"]),
    first_seas = int(players.loc[index, "first_seas"]),
    last_seas = int(players.loc[index, "last_seas"]),
    img_url = players.loc[index, "img_url"],
      )
    player.save()
 





class Command(BaseCommand):
  def handle(self, *args, **options):
    seed_player()
    # clear_data()
    print("completed")