from django.contrib import admin
from nba.models import Player, Stat, Chart, User, Comment, Like

admin.site.register(Player)
admin.site.register(Stat)
admin.site.register(Chart)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)

# Register your models here.
