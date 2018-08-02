from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    pass
    return render(request, 'todolist/home.html', locals())


def add(request):
    pass
    return redirect('/home/')


def delete(request, pk):
    pass
    return redirect('/home/')


def edit(request, pk):
    pass
    return render(request, "todolist/edit.html", locals())