# Generated by Django 5.0.6 on 2024-05-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyatidnevka', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]