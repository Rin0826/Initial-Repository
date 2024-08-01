from django.db import models

# Create your models here.
CATEGORY = (('お店について', 'お店について'),('メニューについて', 'メニューについて'),('その他','その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title