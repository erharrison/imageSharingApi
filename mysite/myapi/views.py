from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImagePostSerializer
from .models import ImagePost, User
from .forms import ImageForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class ImagePostViewSet(viewsets.ModelViewSet):
    queryset = ImagePost.objects.all().order_by('image')
    serializer_class = ImagePostSerializer


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def profile(request, username):
    user_profile = User.objects.get(username=username)

    data = {
        "author": user_profile,
    }
    return render(request, "author/profile.html", data)


def follow_toggle(request, author):
    author_obj = User.objects.get(username=author)
    current_user_obj = User.objects.get(username=request.user.username)
    following = author_obj.following.all()

    if author != current_user_obj.username:
        if current_user_obj in following:
            author_obj.following.remove(current_user_obj.id)
        else:
            author_obj.following.add(current_user_obj.id)

    return HttpResponseRedirect(reverse(profile, args=[author_obj.username]))
