from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImagePostSerializer
from .models import ImagePost, User
from .forms import ImageForm

from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class ImagePostViewSet(viewsets.ModelViewSet):
    queryset = ImagePost.objects.all().order_by('image')
    serializer_class = ImagePostSerializer


class PhotoListView(ListView):

    model = ImagePost

    template_name = 'mysite/list.html'

    context_object_name = 'posts'


class PhotoDetailView(DetailView):

    model = ImagePost

    template_name = 'mysite/detail.html'

    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):

    model = ImagePost

    fields = ['caption', 'author', 'image']

    template_name = 'mysite/create.html'

    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):

        form.instance.submitter = self.request.user

        return super().form_valid(form)


class UserIsSubmitter(UserPassesTestMixin):

    # Custom method
    def get_photo(self):
        return get_object_or_404(ImagePost, pk=self.kwargs.get('pk'))

    def test_func(self):

        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')


class PhotoUpdateView(UserIsSubmitter, UpdateView):

    template_name = 'mysite/update.html'

    model = ImagePost

    fields = ['caption', 'author', 'image']

    success_url = reverse_lazy('photo:list')


class PhotoDeleteView(UserIsSubmitter, DeleteView):

    template_name = 'mysite/delete.html'

    model = ImagePost

    success_url = reverse_lazy('photo:list')


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
