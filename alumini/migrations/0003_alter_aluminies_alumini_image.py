# Generated by Django 3.2.2 on 2021-05-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumini', '0002_rename_aluminious_aluminies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluminies',
            name='alumini_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
