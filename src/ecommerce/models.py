from django.db import models


# Create your models here.
class Products(models.Model):

    CATEGORY_CHOICES = [
        ('headphones', 'Headphones'),
        ('speakers', 'Speakers'),
        ('earphones', 'Earphones'),
    ]

    slug = models.SlugField()
    name = models.CharField(max_length=100)
    image = models.TextField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, editable=False)

