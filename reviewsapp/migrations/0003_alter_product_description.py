# Generated by Django 3.2.19 on 2023-05-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsapp', '0002_auto_20230511_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
