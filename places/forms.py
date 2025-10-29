from django import forms
from .models import Place, Feedback


class PlaceSearchForm(forms.Form):
    q = forms.CharField(label='Search', required=False)
    city = forms.CharField(label='City', required=False)
    category = forms.CharField(label='Category', required=False)


class FeedbackForm(forms.ModelForm):
    RATING_CHOICES = [
        (5, '⭐⭐⭐⭐⭐ Excellent'),
        (4, '⭐⭐⭐⭐ Very Good'),
        (3, '⭐⭐⭐ Good'),
        (2, '⭐⭐ Fair'),
        (1, '⭐ Poor'),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'rating-radio'}),
        label='Rating'
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
        label='Your Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
        label='Your Email'
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Share your experience about this place...'}),
        label='Your Feedback'
    )

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comment']
