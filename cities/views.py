from django.shortcuts import render, get_object_or_404

from cities.models import Ciry

__all__ = (
    'home',
)

def home(request, pk=None):
    if pk:
        #city = Ciry.objects.filter(id=pk).first()
        #city = Ciry.objects.get(id=pk)
        city = get_object_or_404(Ciry, id=pk)

        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    qs = Ciry.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)




# Create your views here.
