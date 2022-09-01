from nba.models import Player, Stat
import csv

def run():
  with open("./data/players.csv") as file:
    reader = csv.reader(file)
    next(reader)
    
    Player.objects.all().delete
    Stat.objects.all().delete
    
    for n in reader:
      player = Player(
        player_id  = n["player_id"],
    player  = n["player"],
    birth_year = n["birth_year"],
    hof = n["hof"],
    num_seasons = n["num_seasons"],
    first_seas = n["first_seas"],
    last_seas = n["last_seas"],
    img_url = n["img_url"],
      )
      player.save()
    
      
      
      
