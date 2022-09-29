from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from main.models import Image

# Create your views here.

def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all().order_by('date')
 return render(request, 'index.html', {'img':img, 'form':form})


def search(request):
  search = request.GET['search']
  images = Image.objects.filter(tags__icontains=search)
  
  return render(request, 'search.html',{'images':images})




#  if form.is_valid():
#    form.save()
#    context = {'form': form, 'Upload':Image.objects.order_by('-pk')[0]}
#    return render(request, 'index.html',context)