# Generated by Django 4.2.11 on 2024-04-09 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0002_gallery_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='option',
            field=models.CharField(choices=[('JPG', 'jpg'), ('PNG', 'png'), ('JPEG', 'jpeg')], default='JPG', max_length=6),
        ),
    ]
