# Generated by Django 2.2.6 on 2019-11-15 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lg_app', '0013_auto_20191115_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedimage',
            name='preset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processed_images', to='lg_app.Preset'),
        ),
    ]
