# Generated by Django 2.2.6 on 2019-11-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lg_app', '0027_auto_20191119_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='presetpack',
            name='pack_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
            preserve_default=False,
        ),
    ]
