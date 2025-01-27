# Generated by Django 5.0.4 on 2024-06-12 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.blogmodel')),
            ],
        ),
    ]
