# from nba.models import Player, Stat
import pandas as pd
from nba.models import Player, Stat
from django.core.management.base import BaseCommand

players = pd.read_csv("./data/players.csv")
player_stats = pd.read_csv("./data/player_stats.csv")

def seed_player():
  for index in players.index:
    player = Player(
    player_number  = players.loc[index, "player_id"],
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
  player = Player.objects.filter(player_number = player_stats.loc[index, "player_id"]).first(),
  Seas_id = player_stats.loc[index, "seas_id"],
  Season = player_stats.loc[index, "season"],
  Position = player_stats.loc[index, "pos"],
  Age = player_stats.loc[index, "age"],
  Experience = player_stats.loc[index, "experience"],
  League = player_stats.loc[index, "lg"],
  Team =  player_stats.loc[index, "tm"],
  Games = player_stats.loc[index, "g"],
  Games_started = player_stats.loc[index, "gs"],
  Minutes_Played_per_game = player_stats.loc[index, "mp_per_game"],
  Field_Goals_per_game = player_stats.loc[index, "fg_per_game"],
  Field_Goal_Attempts_per_game =player_stats.loc[index, "fga_per_game"],
  Field_Goal_percent = player_stats.loc[index, "fg_percent"],
  x3_Point_Field_Goals_per_game = player_stats.loc[index, "x3p_per_game"],
  x3_Point_Field_Goal_Attempts_per_game =player_stats.loc[index, "x3pa_per_game"],
  x3_Point_Field_Goal_percent =player_stats.loc[index, "x3p_percent"],
  x2_Point_Field_Goals_per_game =player_stats.loc[index, "x2p_per_game"],
  x2_Point_Field_Goal_Attempts_per_game =player_stats.loc[index, "x2pa_per_game"],
  x2_Point_Field_Goal_percent =player_stats.loc[index, "x2p_percent"],
  Effective_Field_Goal_percent =player_stats.loc[index, "e_fg_percent"],
  Free_Throws_per_game =player_stats.loc[index, "ft_per_game"],
  Free_Throw_Attempts_per_game =player_stats.loc[index, "fta_per_game"],
  Free_Throw_percent =player_stats.loc[index, "ft_percent"],
  Offensive_Rebounds_per_game = player_stats.loc[index, "orb_per_game"],
  Defensive_Rebounds_per_game =  player_stats.loc[index, "drb_per_game"],
  Total_Rebounds_per_game = player_stats.loc[index, "trb_per_game"],
  Assists_per_game =player_stats.loc[index, "ast_per_game"],
  Steals_per_game = player_stats.loc[index, "stl_per_game"],
  Blocks_per_game =player_stats.loc[index, "blk_per_game"],
  Turnovers_per_game =player_stats.loc[index, "tov_per_game"],
  Personal_Fouls_per_game = player_stats.loc[index, "pf_per_game"],
  Points_per_game =player_stats.loc[index, "pts_per_game"],
  Player_Efficiency_Rating = player_stats.loc[index, "per"],
  True_Shooting_percent = player_stats.loc[index, "ts_percent"],
  x3_Point_Attempt_Rate = player_stats.loc[index, "x3p_ar"],
  Free_Throw_Attempt_Rate = player_stats.loc[index, "f_tr"],
  Offensive_Rebounds_percent = player_stats.loc[index, "orb_percent"],
  Defensive_Rebounds_percent =player_stats.loc[index, "drb_percent"],
  Total_Rebounds_percent = player_stats.loc[index, "trb_percent"],
  Assists_percent = player_stats.loc[index, "ast_percent"],
  Steals_percent = player_stats.loc[index, "stl_percent"],
  Blocks_percent = player_stats.loc[index, "blk_percent"],
  Turnovers_percent =player_stats.loc[index, "tov_percent"],
  Usage_percent = player_stats.loc[index, "usg_percent"],
  Offensive_Win_Shares =player_stats.loc[index, "ows"],
  Defensive_Win_Shares = player_stats.loc[index, "dws"],
  Win_Shares = player_stats.loc[index, "ws"],
  Win_Shares_Per_48_Minutes = player_stats.loc[index, "ws_48"],
  Offensive_Box_Plus_Minus = player_stats.loc[index, "obpm"],
  Defensive_Box_Plus_Minus = player_stats.loc[index, "dbpm"],
  Box_Plus_Minus = player_stats.loc[index, "bpm"],
  VORP =player_stats.loc[index, "vorp"],
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
    