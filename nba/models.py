from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email =  models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Player(models.Model):
    player_id  = models.CharField(max_length=100)
    player  = models.CharField(max_length=100)
    birth_year = models.FloatField(blank=True, null=True)
    hof = models.BooleanField(default=False)
    num_seasons = models.IntegerField()
    first_seas = models.IntegerField()
    last_seas = models.IntegerField()
    img_url = models.TextField(default="https://cdn.nba.com/manage/2021/07/NBA_75-690x588.jpg")

    def __str__(self):
        return self.player

class Stat(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")
  seas_id = models.FloatField()
  season = models.FloatField()
  pos = models.CharField(max_length=100)
  age = models.IntegerField()
  experience = models.FloatField()
  lg = models.FloatField()
  tm =  models.FloatField()
  g = models.FloatField()
  gs = models.FloatField()
  mp_per_game = models.FloatField()
  fg_per_game = models.FloatField()
  fga_per_game =models.FloatField()
  fg_percent = models.FloatField()
  x3p_per_game = models.FloatField()
  x3pa_per_game =models.FloatField()
  x3p_percent =models.FloatField()
  x2p_per_game =models.FloatField()
  x2pa_per_game =models.FloatField()
  x2p_percent =models.FloatField()
  e_fg_percent =models.FloatField()
  ft_per_game =models.FloatField()
  fta_per_game =models.FloatField()
  ft_percent =models.FloatField()
  orb_per_game = models.FloatField()
  drb_per_game =  models.FloatField()
  trb_per_game = models.FloatField()
  ast_per_game =models.FloatField()
  stl_per_game = models.FloatField()
  blk_per_game =models.FloatField()
  tov_per_game =models.FloatField()
  pf_per_game = models.FloatField()
  pts_per_game =models.FloatField()
  per = models.FloatField()
  ts_percent = models.FloatField()
  x3p_ar = models.FloatField()
  f_tr = models.FloatField()
  orb_percent = models.FloatField()
  drb_percent =models.FloatField()
  trb_percent = models.FloatField()
  ast_percent = models.FloatField()
  stl_percent = models.FloatField()
  blk_percent = models.FloatField()
  tov_percent =models.FloatField()
  usg_percent = models.FloatField()
  ows =models.FloatField()
  dws = models.FloatField()
  ws = models.FloatField()
  ws_48 = models.FloatField()
  obpm = models.FloatField()
  dbpm = models.FloatField()
  bpm = models.FloatField()
  vorp =models.FloatField()

  def __str__(self):
    return self.pos

class Chart(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="charts")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="charts")
    y_year = models.BooleanField
    x = models.CharField(max_length=100)

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
  count = models.IntegerField()
  
  def __int__ (self):
    return self.count
  
  
