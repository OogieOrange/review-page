# Generated by Django 3.2.19 on 2023-05-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsapp', '0006_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
