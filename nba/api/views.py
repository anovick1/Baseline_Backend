from rest_framework import generics
from nba.api.serializers import UserSerializer, PlayerSerializer, StatSerializer, ChartSerializer, CommentSerializer, LikeSerializer
from nba.models import User, Player, Stat, Chart, Comment, Like
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
from django.utils.decorators import method_decorator




# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.

## users

@method_decorator(csrf_exempt, name='dispatch')
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@method_decorator(csrf_exempt, name='dispatch')
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
## players
@method_decorator(csrf_exempt, name='dispatch')
class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
@method_decorator(csrf_exempt, name='dispatch')
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

## stats
@method_decorator(csrf_exempt, name='dispatch')
class StatList(generics.ListCreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

@method_decorator(csrf_exempt, name='dispatch')
class StatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

## charts
@method_decorator(csrf_exempt, name='dispatch')
class ChartList(generics.ListCreateAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        newChart = Chart.objects.create(title=data["title"], author=User.objects.filter(id = data["author"]).first(), y_year=data["y_year"], x=data["x"])
        
        newChart.save()
        context={'request': request}
        for p in data["player"]:
            player_obj = Player.objects.get(player_number= p["player_number"])
            newChart.player.add(player_obj)
        serializer = ChartSerializer(newChart, context=context)

        return Response(serializer.data)
    
   
    
@method_decorator(csrf_exempt, name='dispatch')
class ChartDetail(CsrfExemptMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    
    def update(self, request, *args, **kwargs):
        chart_object = self.get_object()
        data = request.data 
        chart_object.player.set([])
        
        chart_object.title=data["title"]
        chart_object.author=User.objects.filter(id = data["author"]).first()
        chart_object.y_year=data["y_year"]
        chart_object.x=data["x"]
        chart_object.description=data["description"]
        chart_object.save()
        for p in data["player"]:
            player_obj = Player.objects.get(player_number= p["player_number"])
            chart_object.player.add (player_obj)
        
        context={'request': request}

        serializer = ChartSerializer(chart_object, context=context)
        return Response(serializer.data)
        

# @method_decorator(csrf_exempt, name='dispatch')
# class CreateChart(APIView):
#     serializer_class = CreateChartSerializer
#     # @csrf_exempt
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             newtitle = serializer.data["title"]
#             author_id = User.objects.filter(id = serializer.data["author"]).first()
#             player_id = Player.objects.filter(player_number = serializer.data["player"]).first()
#             newy_year = serializer.data["y_year"]
#             newx = serializer.data["x"]
#             newChart = Chart(title = newtitle,author = author_id, player = player_id, y_year = newy_year, x = newx)
#             newChart.save()
#             return Response(ChartSerializer(newChart).data, status= status.HTTP_200_OK)
#         else:
#             return Response(status= status.HTTP_200_OK)
## comments
@method_decorator(csrf_exempt, name='dispatch')
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
@method_decorator(csrf_exempt, name='dispatch')
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

## likes
@method_decorator(csrf_exempt, name='dispatch')
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
@method_decorator(csrf_exempt, name='dispatch')
class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer