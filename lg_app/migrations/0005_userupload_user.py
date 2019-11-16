# Generated by Django 2.2.6 on 2019-11-13 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lg_app', '0004_auto_20191113_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='userupload',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_img', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]