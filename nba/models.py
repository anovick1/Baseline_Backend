from datetime import datetime
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email =  models.CharField(max_length=300)
    pfp_url =  models.TextField(default='https://st4.depositphotos.com/1000507/24489/v/600/depositphotos_244890858-stock-illustration-user-profile-picture-isolate-background.jpg')


    def __str__(self):
        return self.name

class Player(models.Model):
    player_number  = models.IntegerField(primary_key=True)
    player  = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100, blank=True, null=True)
    hof = models.BooleanField(default=False)
    num_seasons = models.IntegerField()
    first_seas = models.IntegerField()
    last_seas = models.IntegerField()
    img_url = models.TextField(default="https://cdn.nba.com/manage/2021/07/NBA_75-690x588.jpg")

    def __str__(self):
        return self.player

class Stat(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")
  seas_id = models.CharField(max_length=100, blank=True, null=True)
  season = models.CharField(max_length=100, blank=True, null=True)
  pos = models.CharField(max_length=100)
  age = models.CharField(max_length=100, blank=True, null=True)
  experience = models.CharField(max_length=100, blank=True, null=True)
  lg = models.CharField(max_length=100, blank=True, null=True)
  tm =  models.CharField(max_length=100, blank=True, null=True)
  g = models.CharField(max_length=100, blank=True, null=True)
  gs = models.CharField(max_length=100, blank=True, null=True)
  mp_per_game = models.CharField(max_length=100, blank=True, null=True)
  fg_per_game = models.CharField(max_length=100, blank=True, null=True)
  fga_per_game =models.CharField(max_length=100, blank=True, null=True)
  fg_percent = models.CharField(max_length=100, blank=True, null=True)
  x3p_per_game = models.CharField(max_length=100, blank=True, null=True)
  x3pa_per_game =models.CharField(max_length=100, blank=True, null=True)
  x3p_percent =models.CharField(max_length=100, blank=True, null=True)
  x2p_per_game =models.CharField(max_length=100, blank=True, null=True)
  x2pa_per_game =models.CharField(max_length=100, blank=True, null=True)
  x2p_percent =models.CharField(max_length=100, blank=True, null=True)
  e_fg_percent =models.CharField(max_length=100, blank=True, null=True)
  ft_per_game =models.CharField(max_length=100, blank=True, null=True)
  fta_per_game =models.CharField(max_length=100, blank=True, null=True)
  ft_percent =models.CharField(max_length=100, blank=True, null=True)
  orb_per_game = models.CharField(max_length=100, blank=True, null=True)
  drb_per_game =  models.CharField(max_length=100, blank=True, null=True)
  trb_per_game = models.CharField(max_length=100, blank=True, null=True)
  ast_per_game =models.CharField(max_length=100, blank=True, null=True)
  stl_per_game = models.CharField(max_length=100, blank=True, null=True)
  blk_per_game =models.CharField(max_length=100, blank=True, null=True)
  tov_per_game =models.CharField(max_length=100, blank=True, null=True)
  pf_per_game = models.CharField(max_length=100, blank=True, null=True)
  pts_per_game =models.CharField(max_length=100, blank=True, null=True)
  per = models.CharField(max_length=100, blank=True, null=True)
  ts_percent = models.CharField(max_length=100, blank=True, null=True)
  x3p_ar = models.CharField(max_length=100, blank=True, null=True)
  f_tr = models.CharField(max_length=100, blank=True, null=True)
  orb_percent = models.CharField(max_length=100, blank=True, null=True)
  drb_percent =models.CharField(max_length=100, blank=True, null=True)
  trb_percent = models.CharField(max_length=100, blank=True, null=True)
  ast_percent = models.CharField(max_length=100, blank=True, null=True)
  stl_percent = models.CharField(max_length=100, blank=True, null=True)
  blk_percent = models.CharField(max_length=100, blank=True, null=True)
  tov_percent =models.CharField(max_length=100, blank=True, null=True)
  usg_percent = models.CharField(max_length=100, blank=True, null=True)
  ows =models.CharField(max_length=100, blank=True, null=True)
  dws = models.CharField(max_length=100, blank=True, null=True)
  ws = models.CharField(max_length=100, blank=True, null=True)
  ws_48 = models.CharField(max_length=100, blank=True, null=True)
  obpm = models.CharField(max_length=100, blank=True, null=True)
  dbpm = models.CharField(max_length=100, blank=True, null=True)
  bpm = models.CharField(max_length=100, blank=True, null=True)
  vorp =models.CharField(max_length=150, blank=True, null=True)

  def __str__(self):
    return self.player
class Chart(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="charts")
    # player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="charts")
    player = models.ManyToManyField(Player, related_name="charts")
    y_year = models.BooleanField(default=True)
    x = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)

    def __str__(self):
      return self.title


class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
  chart = models.ForeignKey(Chart, on_delete=models.CASCADE, related_name="comments")
  text = models.TextField(default=" ")
  
  def __str__(self):
    return self.text
  
class Like(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
  chart = models.ForeignKey(Chart, on_delete=models.CASCADE, related_name="likes")
  count = models.IntegerField(default=0)
  
  def __int__ (self):
    return self.count
  
  
