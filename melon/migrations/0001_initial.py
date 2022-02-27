# Generated by Django 3.2.12 on 2022-02-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Melon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('song', models.FileField(upload_to='melon')),
                ('thumbnail', models.FileField(upload_to='melon')),
            ],
        ),
    ]