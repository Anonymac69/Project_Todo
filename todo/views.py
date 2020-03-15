from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Profile

# Create your views here.
@login_required(login_url='/')
def user_profile(request):
    uid = request.user.id
    if request.method == 'GET':
        profile = Profile.objects.filter(author_id=uid)
        context = {'profile': profile}
        return render(request, 'todo/profile.html', context)

    if request.method == 'POST':
        create_post = Profile()
        create_post.title = request.POST['title'][0:100]
        create_post.description = request.POST['description'][0:255]
        create_post.author = User(pk=uid)
        create_post.achieve = int(request.POST['publish'])
        create_post.save()

        messages.success(request, 'Profile post created succesfully.')
        return redirect('profile')


@login_required(login_url='/')
def delete_profile(request, post_id):
    if request.method == 'POST':
        delete_post = Profile.objects.get(pk=post_id)
        delete_post.delete()
        return redirect('profile')
    else:
        return redirect('profile')


def update_profile(request, post_id):
    if request.method == 'GET':
        profile = Profile.object.get(pk=post_id)
        context = {'profile': profile}
        return render(request, 'accounts/update_profile.html', context)

    if request.method == 'POST':
        update_post = Profile.objects.get(pk=post_id)
        update_post.description = request.POST['description'][0:255]
        if 'image' in request.FILES:
            update_post.image = request.FILES['image']
        update_post.publish = int(request.POST['publish'])
        update_post.save()

        messages.success(request, 'Profile post created succesfully.')
        return redirect('profile')
