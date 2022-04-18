from django.shortcuts import render

from cities.models import Ciry

__all__ = (
    'home',
)

def home(request):
    qs = Ciry.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)



# Create your views here.
