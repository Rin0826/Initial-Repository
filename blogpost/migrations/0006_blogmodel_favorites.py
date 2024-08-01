# Generated by Django 5.0.4 on 2024-07-03 03:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0005_blogmodel_dislikes_blogmodel_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]