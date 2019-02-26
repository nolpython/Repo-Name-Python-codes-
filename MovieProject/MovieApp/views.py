from django.shortcuts import render
from MovieApp.forms import MyMovieModelForm
from MovieApp.models import MyMovieModel

def showAddMovieView(req):
    mmmf = MyMovieModelForm()
    if req.method == "POST":
        fmmmf = MyMovieModelForm(req.POST)
        print("Inside post..")
        if fmmmf.is_valid():
            fmmmf.save(commit=True)
            return render(req,"MovieApp/index.html")
    return render(req,"MovieApp/addmovie.html",{"mmmf":mmmf})


def showIndexView(request):
    return render(request,"MovieApp/index.html")


def showListMovieView(request):
    qs = MyMovieModel.objects.all()
    print(qs)
    return render(request,"MovieApp/listmovie.html",{"qs":qs})