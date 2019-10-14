from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


BOOK_GENRES = [
        ('Fantasy', 'Fantasy'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Criminal', 'Criminal'),
        ('Science', 'Science'),
        ('Unspecified', 'Unspecified')
]


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    picture = models.ImageField(default='default.jpg', upload_to='book_authors')
    biography = models.TextField(blank=True)
    
    class Meta:
        ordering = ('surname',)
    
    def __str__(self):
        return f'{self.name} {self.surname}'

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    publication = models.DateField(default=date.today)
    cover = models.ImageField(default='default.jpg', upload_to='book_covers')
    genre = models.CharField(max_length=100, choices=BOOK_GENRES, default='Unspecified')
    series = models.CharField(max_length=150, blank=True)
    translation = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Bookshelf(models.Model):
    bookworm = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return f'Bookshelf of {self.bookworm.first_name} {self.bookworm.last_name} ({self.bookworm})'