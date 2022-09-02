# from nba.models import Player, Stat
import pandas as pd
from django.core.management.base import BaseCommand
from nba.models import Player, Stat

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

def seed_stats():
  for index in player_stats.index:
    print(index)
    stats = Stat(
  player = Player.objects.filter(player_id=player_stats.loc[index, "player_id"]),
  seas_id = player_stats.loc[index, "seas_id"],
  season = player_stats.loc[index, "season"],
  pos = player_stats.loc[index, "pos"],
  age = player_stats.loc[index, "age"],
  experience = player_stats.loc[index, "experience"],
  lg = player_stats.loc[index, "lg"],
  tm =  player_stats.loc[index, "tm"],
  g = player_stats.loc[index, "g"],
  gs = player_stats.loc[index, "gs"],
  mp_per_game = player_stats.loc[index, "mp_per_game"],
  fg_per_game = player_stats.loc[index, "fg_per_game"],
  fga_per_game =player_stats.loc[index, "fga_per_game"],
  fg_percent = player_stats.loc[index, "fg_percent"],
  x3p_per_game = player_stats.loc[index, "x3p_per_game"],
  x3pa_per_game =player_stats.loc[index, "x3pa_per_game"],
  x3p_percent =player_stats.loc[index, "x3p_percent"],
  x2p_per_game =player_stats.loc[index, "x2p_per_game"],
  x2pa_per_game =player_stats.loc[index, "x2pa_per_game"],
  x2p_percent =player_stats.loc[index, "x2p_percent"],
  e_fg_percent =player_stats.loc[index, "e_fg_percent"],
  ft_per_game =player_stats.loc[index, "ft_per_game"],
  fta_per_game =player_stats.loc[index, "fta_per_game"],
  ft_percent =player_stats.loc[index, "ft_percent"],
  orb_per_game = player_stats.loc[index, "orb_per_game"],
  drb_per_game =  player_stats.loc[index, "drb_per_game"],
  trb_per_game = player_stats.loc[index, "trb_per_game"],
  ast_per_game =player_stats.loc[index, "ast_per_game"],
  stl_per_game = player_stats.loc[index, "stl_per_game"],
  blk_per_game =player_stats.loc[index, "blk_per_game"],
  tov_per_game =player_stats.loc[index, "tov_per_game"],
  pf_per_game = player_stats.loc[index, "pf_per_game"],
  pts_per_game =player_stats.loc[index, "pts_per_game"],
  per = player_stats.loc[index, "per"],
  ts_percent = player_stats.loc[index, "ts_percent"],
  x3p_ar = player_stats.loc[index, "x3p_ar"],
  f_tr = player_stats.loc[index, "f_tr"],
  orb_percent = player_stats.loc[index, "orb_percent"],
  drb_percent =player_stats.loc[index, "drb_percent"],
  trb_percent = player_stats.loc[index, "trb_percent"],
  ast_percent = player_stats.loc[index, "ast_percent"],
  stl_percent = player_stats.loc[index, "stl_percent"],
  blk_percent = player_stats.loc[index, "blk_percent"],
  tov_percent =player_stats.loc[index, "tov_percent"],
  usg_percent = player_stats.loc[index, "usg_percent"],
  ows =player_stats.loc[index, "ows"],
  dws = player_stats.loc[index, "dws"],
  ws = player_stats.loc[index, "ws"],
  ws_48 = player_stats.loc[index, "ws_48"],
  obpm = player_stats.loc[index, "obpm"],
  dbpm = player_stats.loc[index, "dbpm"],
  bpm = player_stats.loc[index, "bpm"],
  vorp =player_stats.loc[index, "vorp"],
  )
    stats.save()



def clear_data():
  Player.objects.all().delete()
  Stat.objects.all().delete()

class Command(BaseCommand):
  def handle(self, *args, **options):
    clear_data()
    seed_player()
    seed_stats()
    print("completed")