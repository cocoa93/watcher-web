
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

from ownerPage.forms import PostForm
from ownerPage.models import Owners


def index(request):
    return render(request, "ownerPage/main.html", {})


def main(request):
    return render(request, "index.html", {})


def profile(request):
    if request.method == 'POST':
        owner = Owners.objects.get(user=request.user)
        form = PostForm(request.POST, request.FILES, instance=owner)  # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid():
            form.save()
            return redirect(profile)
    else:
        owner = Owners.objects.get(user=request.user)
        form = PostForm(instance=owner)
    return render(request, "ownerPage/profile.html", {
        'form': form,
    })


def logout(request):
    django_logout(request)
    return redirect('login')
