# Generated by Django 3.2.3 on 2022-02-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(help_text='Upload your document', null='True', upload_to='upload_to', verbose_name='file'),
        ),
    ]
