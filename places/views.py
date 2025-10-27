from django.shortcuts import render, get_object_or_404
from .models import Place, Category
from .forms import PlaceSearchForm
from django.db.models import Q

def place_list(request):
    form = PlaceSearchForm(request.GET or None)
    qs = Place.objects.all().select_related('category')

    if form.is_valid():
        q = form.cleaned_data.get('q')
        city = form.cleaned_data.get('city')
        category = form.cleaned_data.get('category')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if city:
            qs = qs.filter(city__icontains=city)
        if category:
            qs = qs.filter(category__name__icontains=category)

    categories = Category.objects.all()
    return render(request, 'places/place_list.html', {'places': qs, 'form': form, 'categories': categories})

def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)
    return render(request, 'places/place_detail.html', {'place': place})
