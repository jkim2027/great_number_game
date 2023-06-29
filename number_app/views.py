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
    users_guess = int(request.POST['users_guess'])
    random_num = int(request.session['random'])
    context = {
        "guess_template": users_guess,
        "random_template": random_num
    }
    if users_guess < random_num or users_guess > random_num:
        return render(request, "index.html", context)
    if users_guess == random_num:
        del request.session['random']
        return render(request, "again.html", context)