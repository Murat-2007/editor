# Generated by Django 3.2.3 on 2022-02-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='post', to='post.Category'),
        ),
    ]