# Generated by Django 5.1.2 on 2024-10-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_dishes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
