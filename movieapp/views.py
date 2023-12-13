from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.form import cinemaform
from movieapp.models import cinema_table


# Create your views here.
def index(request):
    movie= cinema_table.objects.all()
    contex = { 'movie_list':movie }
    return render(request,"index.html",contex)

def detail(request, movie_id):
    shoot = cinema_table.objects.get(id=movie_id)
    return render(request,"detail.html",{'script':shoot})

def add_data(request):
    if request.method =="POST":
        name = request.POST.get('name',)
        year = request.POST.get('year',)
        desc = request.POST.get('desc',)
        img = request.FILES['img']
        movie=cinema_table(name=name,year=year,desc=desc,img=img)
        movie.save();
    return render(request,"add.html")

def update(request,id):
    story = cinema_table.objects.get(id=id)
    form = cinemaform(request.POST or None,request.FILES,instance=story)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'movie':story,'form':form})

def delete(request,id):
    if request.method == "POST":
        cancel = cinema_table.objects.get(id=id)
        cancel.delete();
        return redirect('/')
    return render(request,"delete.html")