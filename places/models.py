from django.db import models 
from django.urls import reverse 
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta: 
        verbose_name_plural = "Categories" 
        def __str__(self):
            return self.name
            class Place(models.Model): 
                title = models.CharField(max_length=200)
                slug = models.SlugField(max_length=220, unique=True) 
                category = models.ForeignKey(Category, 
                                             on_delete=models.SET_NULL, null=True, blank=True) 
                city = models.CharField(max_length=100) 
                state = models.CharField(max_length=100, blank=True) 
                description = models.TextField(blank=True) image = models.ImageField(upload_to='places/', blank=True, null=True)
                created_at = models.DateTimeField(auto_now_add=True)
                class Meta: 
                    ordering = ['-created_at'] 
                    def __str__(self): 
                        return self.title 
                        def get_absolute_url(self): 
                            return reverse('places:place_detail', kwargs={'slug': self.slug})
                            def get_average_rating(self): 
                                """Calculate average rating for this place""" 
                                feedbacks = self.feedbacks.filter(approved=True)
                                if feedbacks.exists(): 
                                    return sum(f.rating for f in feedbacks) / feedbacks.count() 
                                    return 0 
                                    def get_rating_count(self): 
                                        """Get total number of ratings""" 
                                        return self.feedbacks.filter(approved=True).count()
                                        class Feedback(models.Model):
                                            RATING_CHOICES = [ 
                                                (5, '⭐⭐⭐⭐⭐ Excellent'),
                                                (4, '⭐⭐⭐⭐ Very Good'), 
                                                (3, '⭐⭐⭐ Good'), 
                                                (2, '⭐⭐ Fair'), 
                                                (1, '⭐ Poor'),
                                            ]
                                            place = models.ForeignKey(Place, on_delete=models.CASCADE,
                                                                      related_name='feedbacks')
                                            user = models.ForeignKey(User, on_delete=models.CASCADE, 
                                                                     null=True, blank=True)
                                            name = models.CharField(max_length=100, help_text="Your name")
                                            email = models.EmailField(help_text="Your email") 
                                            rating = models.IntegerField(choices=RATING_CHOICES) 
                                            comment = models.TextField(help_text="Share your experience...") 
                                            created_at = models.DateTimeField(auto_now_add=True) 
                                            approved = models.BooleanField(default=True, help_text="Approved for display")
                                            class Meta: 
                                                ordering = ['-created_at'] 
                                                def __str__(self):
                                                    return f"{self.name} - {self.place.title} ({self.rating} stars)" 
                                                    def get_stars(self): 
                                                        """Return star display for rating"""
                                                        return '⭐' * self.rating
