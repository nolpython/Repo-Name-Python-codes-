from MovieApp.models import MyMovieModel
from django import forms


class MyMovieModelForm(forms.ModelForm):
    class Meta:
        model = MyMovieModel
        fields = "__all__"
        #fields = ("rdate","hero","heroine",)
        #exclude = ["rating"]