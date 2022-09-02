from django.urls import path
from nba.api import views



urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    
    path('players/', views.PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name='player_detail'),
    
    path('stats/', views.StatList.as_view(), name='stat_list'),
    path('stats/<int:pk>', views.StatDetail.as_view(), name='stat_detail'),
    
    path('charts/', views.ChartList.as_view(), name='chart_list'),
    path('charts/<int:pk>', views.ChartDetail.as_view(), name='chart_detail'),
    
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    
    path('likes/', views.LikeList.as_view(), name='like_list'),
    path('likes/<int:pk>', views.LikeDetail.as_view(), name='like_detail'),

]