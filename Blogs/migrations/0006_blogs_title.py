# Generated by Django 3.2.5 on 2021-08-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0005_alter_blogs_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='title',
            field=models.TextField(default='No title'),
        ),
    ]