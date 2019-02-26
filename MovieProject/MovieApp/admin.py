from django.contrib import admin
from MovieApp.models import MyMovieModel
class MovieAdmin(admin.ModelAdmin):
    list_display = ["rdate","movieName","hero","heroine","rating"]

admin.site.register(MyMovieModel,MovieAdmin)

