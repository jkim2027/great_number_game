from django.shortcuts import render, redirect
import random

# Create your views here.


def index(request):
    if 'random' not in request.session:
        random_num = random.randint(1, 100)
        request.session['random'] = random_num
        print(random_num)
    return render(request, "index.html")


def validate_guess(request):
    if int(request.POST['users_guess']) < int(request.session['random']):
        return redirect("/")
    if int(request.POST['users_guess']) > int(request.session['random']):
        return redirect("/")
    if int(request.POST['users_guess']) == int(request.session['random']):
        del request.session['random']
        return render(request, "again.html")