# Generated by Django 3.2.5 on 2021-08-25 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_register'),
        ('Blogs', '0003_blogs_globalblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.register'),
        ),
    ]
