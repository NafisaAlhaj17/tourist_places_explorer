from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Place, Category, Feedback
from .forms import PlaceSearchForm, FeedbackForm


# ✅ Publicly visible homepage (place list)
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
    return render(request, 'places/place_list.html', {
        'places': qs,
        'form': form,
        'categories': categories
    })


# ✅ Only logged-in users can view place details and give feedback
@login_required(login_url='/users/signup/')
def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)
    feedbacks = place.feedbacks.filter(approved=True)
    average_rating = place.get_average_rating()
    rating_count = place.get_rating_count()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.place = place
            feedback.user = request.user
            feedback.approved = True
            feedback.save()
            messages.success(request, '✅ Thank you for your feedback!')
            return redirect('places:place_detail', slug=place.slug)
    else:
        form = FeedbackForm()

    context = {
        'place': place,
        'feedback_form': form,
        'feedbacks': feedbacks,
        'average_rating': round(average_rating, 1) if average_rating > 0 else 0,
        'rating_count': rating_count,
    }
    return render(request, 'places/place_detail.html', context)
