# Generated by Django 4.2.4 on 2023-08-16 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('world_news', '0006_commentnewstitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstitle',
            name='powered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
