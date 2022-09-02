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
  seas_id = models.FloatField(blank=True, null=True)
  season = models.FloatField(blank=True, null=True)
  pos = models.CharField(max_length=100)
  age = models.IntegerField()
  experience = models.FloatField(blank=True, null=True)
  lg = models.CharField(max_length=100, blank=True, null=True)
  tm =  models.CharField(max_length=100, blank=True, null=True)
  g = models.FloatField(blank=True, null=True)
  gs = models.FloatField(blank=True, null=True)
  mp_per_game = models.FloatField(blank=True, null=True)
  fg_per_game = models.FloatField(blank=True, null=True)
  fga_per_game =models.FloatField(blank=True, null=True)
  fg_percent = models.FloatField(blank=True, null=True)
  x3p_per_game = models.FloatField(blank=True, null=True)
  x3pa_per_game =models.FloatField(blank=True, null=True)
  x3p_percent =models.FloatField(blank=True, null=True)
  x2p_per_game =models.FloatField(blank=True, null=True)
  x2pa_per_game =models.FloatField(blank=True, null=True)
  x2p_percent =models.FloatField(blank=True, null=True)
  e_fg_percent =models.FloatField(blank=True, null=True)
  ft_per_game =models.FloatField(blank=True, null=True)
  fta_per_game =models.FloatField(blank=True, null=True)
  ft_percent =models.FloatField(blank=True, null=True)
  orb_per_game = models.FloatField(blank=True, null=True)
  drb_per_game =  models.FloatField(blank=True, null=True)
  trb_per_game = models.FloatField(blank=True, null=True)
  ast_per_game =models.FloatField(blank=True, null=True)
  stl_per_game = models.FloatField(blank=True, null=True)
  blk_per_game =models.FloatField(blank=True, null=True)
  tov_per_game =models.FloatField(blank=True, null=True)
  pf_per_game = models.FloatField(blank=True, null=True)
  pts_per_game =models.FloatField(blank=True, null=True)
  per = models.FloatField(blank=True, null=True)
  ts_percent = models.FloatField(blank=True, null=True)
  x3p_ar = models.FloatField(blank=True, null=True)
  f_tr = models.FloatField(blank=True, null=True)
  orb_percent = models.FloatField(blank=True, null=True)
  drb_percent =models.FloatField(blank=True, null=True)
  trb_percent = models.FloatField(blank=True, null=True)
  ast_percent = models.FloatField(blank=True, null=True)
  stl_percent = models.FloatField(blank=True, null=True)
  blk_percent = models.FloatField(blank=True, null=True)
  tov_percent =models.FloatField(blank=True, null=True)
  usg_percent = models.FloatField(blank=True, null=True)
  ows =models.FloatField(blank=True, null=True)
  dws = models.FloatField(blank=True, null=True)
  ws = models.FloatField(blank=True, null=True)
  ws_48 = models.FloatField(blank=True, null=True)
  obpm = models.FloatField(blank=True, null=True)
  dbpm = models.FloatField(blank=True, null=True)
  bpm = models.FloatField(blank=True, null=True)
  vorp =models.FloatField(blank=True, null=True)

  def __str__(self):
    return str(self.player)

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
  
  
