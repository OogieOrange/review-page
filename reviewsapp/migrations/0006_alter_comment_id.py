# Generated by Django 3.2.19 on 2023-05-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsapp', '0005_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(default='46F39', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
