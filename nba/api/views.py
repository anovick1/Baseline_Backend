from rest_framework import generics
from nba.api.serializers import UserSerializer, PlayerSerializer, StatSerializer, ChartSerializer, CommentSerializer, LikeSerializer
from nba.models import User, Player, Stat, Chart, Comment, Like

# Create your views here.

## users
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
## players
class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

## stats
class StatList(generics.ListCreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class StatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

## charts
class ChartList(generics.ListCreateAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

class ChartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

## comments
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

## likes
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer