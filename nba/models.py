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
  Seas_id = models.CharField(max_length=100, blank=True, null=True)
  Season = models.CharField(max_length=100, blank=True, null=True)
  Position = models.CharField(max_length=100)
  Age = models.CharField(max_length=100, blank=True, null=True)
  Experience = models.CharField(max_length=100, blank=True, null=True)
  League = models.CharField(max_length=100, blank=True, null=True)
  Team =  models.CharField(max_length=100, blank=True, null=True)
  Games = models.CharField(max_length=100, blank=True, null=True)
  Games_Started = models.CharField(max_length=100, blank=True, null=True)
  Minutes_Played_Per_Game = models.CharField(max_length=100, blank=True, null=True)
  Field_Goals_per_game = models.CharField(max_length=100, blank=True, null=True)
  Field_Goal_Attempts_per_game =models.CharField(max_length=100, blank=True, null=True)
  Field_Goal_percent = models.CharField(max_length=100, blank=True, null=True)
  x3_Point_Field_Goals_per_game = models.CharField(max_length=100, blank=True, null=True)
  x3_Point_Field_Goal_Attempts_per_game =models.CharField(max_length=100, blank=True, null=True)
  x3_Point_Field_Goal_percent =models.CharField(max_length=100, blank=True, null=True)
  x2_Point_Field_Goals_per_game =models.CharField(max_length=100, blank=True, null=True)
  x2_Point_Field_Goal_Attempts_per_game =models.CharField(max_length=100, blank=True, null=True)
  x2_Point_Field_Goal_percent =models.CharField(max_length=100, blank=True, null=True)
  Effective_Field_Goal_percent =models.CharField(max_length=100, blank=True, null=True)
  Free_Throws_per_game =models.CharField(max_length=100, blank=True, null=True)
  Free_Throw_Attempts_per_game =models.CharField(max_length=100, blank=True, null=True)
  Free_Throw_percent =models.CharField(max_length=100, blank=True, null=True)
  Offensive_Rebounds_per_game = models.CharField(max_length=100, blank=True, null=True)
  Defensive_Rebounds_per_game =  models.CharField(max_length=100, blank=True, null=True)
  Total_Rebounds_per_game = models.CharField(max_length=100, blank=True, null=True)
  Assists_per_game =models.CharField(max_length=100, blank=True, null=True)
  Steals_per_game = models.CharField(max_length=100, blank=True, null=True)
  Blocks_per_game =models.CharField(max_length=100, blank=True, null=True)
  Turnovers_per_game =models.CharField(max_length=100, blank=True, null=True)
  Personal_Fouls_per_game = models.CharField(max_length=100, blank=True, null=True)
  Points_per_game =models.CharField(max_length=100, blank=True, null=True)
  Player_Efficiency_Rating = models.CharField(max_length=100, blank=True, null=True)
  True_Shooting_percent = models.CharField(max_length=100, blank=True, null=True)
  x3_Point_Attempt_Rate = models.CharField(max_length=100, blank=True, null=True)
  Free_Throw_Attempt_Rate = models.CharField(max_length=100, blank=True, null=True)
  Offensive_Rebounds_percent = models.CharField(max_length=100, blank=True, null=True)
  Defensive_Rebounds_percent =models.CharField(max_length=100, blank=True, null=True)
  Total_Rebounds_percent = models.CharField(max_length=100, blank=True, null=True)
  Assists_percent = models.CharField(max_length=100, blank=True, null=True)
  Steals_percent = models.CharField(max_length=100, blank=True, null=True)
  Blocks_percent = models.CharField(max_length=100, blank=True, null=True)
  Turnovers_percent =models.CharField(max_length=100, blank=True, null=True)
  Usage_percent = models.CharField(max_length=100, blank=True, null=True)
  Offensive_Win_Shares =models.CharField(max_length=100, blank=True, null=True)
  Defensive_Win_Shares = models.CharField(max_length=100, blank=True, null=True)
  Win_Shares = models.CharField(max_length=100, blank=True, null=True)
  Win_Shares_Per_48_Minutes = models.CharField(max_length=100, blank=True, null=True)
  Offensive_Box_Plus_Minus = models.CharField(max_length=100, blank=True, null=True)
  Defensive_Box_Plus_Minus = models.CharField(max_length=100, blank=True, null=True)
  Box_Plus_Minus = models.CharField(max_length=100, blank=True, null=True)
  VORP =models.CharField(max_length=150, blank=True, null=True)

  def __str__(self):
    return self.player
class Chart(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="charts")
    # player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="charts")
    player = models.ManyToManyField(Player, related_name="charts")
    y_year = models.BooleanField(default=True)
    x = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=255, default=" ")

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
  
  
