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
        many = "true",
        read_only=True
    )
  comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many = "true",
        read_only=True
    )
  class Meta: 
    model = User
    fields = ('id','name', 'email', 'charts', 'likes', 'comments' )

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  stats = serializers.HyperlinkedRelatedField(
        view_name='stat_detail',
        read_only=True
    )
  class Meta: 
    model = Player
    fields = ('id', 'charts', 'player_id', 'player', 'birth_year', "hof", "num_seasons", "first_seas",
              "last_seas", "img_url", "stats" )



class StatSerializer(serializers.HyperlinkedModelSerializer):
  player = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        read_only=True
    )
  class Meta: 
    model = Stat
    fields = ('id','player', 'season', 'player_id', 'pos', 'age', 'experience', 'lg', 'tm', 'g', 'gs',
              'mp_per_game', 'fg_per_game', 'fga_per_game', 'fg_percent', 'x3p_per_game',
              'x3pa_per_game', 'x3p_percent', 'x2p_per_game', 'x2pa_per_game','x2p_percent', 
              'e_fg_percent', 'ft_per_game', 'fta_per_game', 'ft_percent', 'orb_per_game', 
              'drb_per_game', 'trb_per_game', 'ast_per_game', 'stl_per_game', 'blk_per_game', 
              'tov_per_game', 'pf_per_game', 'pts_per_game', 'per', 'ts_percent', 'x3p_ar', 
              'f_tr', 'orb_percent', 'drb_percent', 'trb_percent', 'ast_percent', 'stl_percent',
              'blk_percent', 'tov_percent', 'usg_percent', 'ows', 'dws', 'ws', 'ws_48', 'obpm', 'dbpm', 'bpm', 'vorp')

class ChartSerializer(serializers.HyperlinkedModelSerializer):
  author = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
  player = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many = "true",
        read_only=True
    )
  likes = serializers.HyperlinkedRelatedField(
        view_name='like_detail',
        many = "true",
        read_only=True
    )
  comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many = "true",
        read_only=True
    )
  class Meta: 
    model = Chart
    fields = ('id','title', 'author', 'player', 'y_year', 'x', "likes", "comments" )

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