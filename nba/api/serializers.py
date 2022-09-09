from rest_framework import serializers
from nba.models import User, Player, Stat, Chart, Comment, Like

class UserSerializer(serializers.HyperlinkedModelSerializer):
  charts = serializers.HyperlinkedRelatedField(
        view_name='chart_detail',
        many=True,
        read_only=True
    )
  likes = serializers.HyperlinkedRelatedField(
        view_name='like_detail',
        many = True,
        read_only=True
    )
  comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many = True,
        read_only=True
    )
  class Meta: 
    model = User
    fields = ('id','name', 'email', 'charts', 'likes', 'comments' )




class StatSerializer(serializers.HyperlinkedModelSerializer):
  player = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        read_only=True
    )
  class Meta: 
    model = Stat
    fields = ('id','player', 'Season', 'Position', 'Age', 'Experience', 'League', 'Team', 'Games', 'Games_Started',
              'Minutes_Played_Per_Game', 'Field_Goals_per_game', 'Field_Goal_Attempts_per_game', 'Field_Goal_percent', 
              'x3_Point_Field_Goals_per_game', 'x3_Point_Field_Goal_Attempts_per_game', 'x3_Point_Field_Goals_percent', 
              'x2_Point_Field_Goals_per_game', 'x2_Point_Field_Goal_Attempts_per_game','x2_Point_Field_Goals_percent', 
              'Effective_Field_Goal_percent', 'Free_Throws_per_game', 'Free_Throw_Attempts_per_game', 'Free_Throw_percent', 
              'Offensive_Rebounds_game', 'Defensive_Rebounds_game', 'Total_Rebounds_per_game', 'Assists_per_game', 'Steals_per_game', 
              'Blocks_per_game', 'Turnovers_per_game', 'Personal_Fouls_per_game', 'Points_per_game', 'Player_Efficiency_Rating', 
              'True_Shooting_percent', 'x3_Point_Attempt_Rate', 'Free_Throw_Attempt_Rate', 'Offensive_Rebounds_percent', 
              'Defensive_Rebounds_percent', 'Total_Rebounds_percent', 'Assists_percent', 'Steals_percent',
              'Blocks_percent', 'Turnovers_percent', 'Usage_percent', 'Offensive_Win_Shares', 'Defensive_Win_Shares', 
              'Win_Shares', 'Win_Shares_Per_48_Minutes','Offensive_Box_Plus_Minus', 'Defensive_Box_Plus_Minus', 'Box_Plus_Minus', 'VORP')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  stats = StatSerializer(many = True, read_only=True )
  # stats = serializers.HyperlinkedRelatedField(
  #       view_name='stat_detail',
  #       many = True,
  #       read_only=True
  #   )
  charts = serializers.HyperlinkedRelatedField(
        view_name='chart_detail',
        many = True,
        read_only=True
        
    )
  class Meta: 
    model = Player
    fields = ('player_number', 'player', 'birth_year', "hof", "num_seasons", "first_seas",
              "last_seas", "img_url", "stats", 'charts'  )

class ChartSerializer(serializers.HyperlinkedModelSerializer):
  author = UserSerializer(read_only=True)
  # author = serializers.HyperlinkedRelatedField(
  #       view_name='user_detail',
  #       read_only=True
  #   )
  player = PlayerSerializer(
        many = True,
        read_only=True
    )
  # player = serializers.HyperlinkedRelatedField(
  #       view_name='player_detail',
  #       many = True,
  #       read_only=True
  #   )
  likes = serializers.HyperlinkedRelatedField(
        view_name='like_detail',
        many = True,
        read_only=True
    )
  comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many = True,
        read_only=True
    )
  class Meta: 
    model = Chart
    fields = ('id','title', 'author', 'player', 'y_year', 'x', "likes", "comments", "date", "description" )
    depth = 1
  # def create(self, data):
  #   chart = Chart(
  #     title = data["tile"],
  #     author = data["author"],
  #     player = data["player"],
  #     y_year = data["y_year"],
  #     x = data["x"]
  #   )
  #   chart.save()
  #   return chart

class CreateChartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chart
    fields = ('title', 'author', 'player', 'y_year', 'x')

class LikeSerializer(serializers.HyperlinkedModelSerializer):
  chart = serializers.HyperlinkedRelatedField(
        view_name='chart_detail',
        read_only=True
    )
  user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
  class Meta: 
    model = Like
    fields = ('id','count', 'user', 'chart' )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  chart = serializers.HyperlinkedRelatedField(
        view_name='chart_detail',
        read_only=True
    )
  user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
  class Meta: 
    model = Comment
    fields = ('id','text', 'user', 'chart' )