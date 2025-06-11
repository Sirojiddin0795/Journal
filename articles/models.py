from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from categories.models import Category
from publications.models import Publication

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent_to_review', 'Sent to Moderator'),
        ('under_review', 'Under Review'),
        ('revision_required', 'Revision Required'),
        ('published', 'Published'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)

    def avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum([r.score for r in reviews]) / reviews.count(), 2)
        return None

    def __str__(self):
        return self.title

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='reviews', on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reviewer', 'article')

    def __str__(self):
        return f'{self.reviewer.username} → {self.article.title}'
