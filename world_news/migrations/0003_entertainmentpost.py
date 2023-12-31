# Generated by Django 4.2.4 on 2023-08-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_news', '0002_newstitle_created_at_newstitle_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntertainmentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='Entertainment/images')),
                ('inline_category', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.TextField(verbose_name='Yangilik matni')),
            ],
        ),
    ]
