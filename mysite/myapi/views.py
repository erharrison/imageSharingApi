from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImagePostSerializer
from .models import ImagePost
from .forms import ImageForm


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
