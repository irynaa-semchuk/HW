# Generated by Django 3.2.6 on 2021-08-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'News Letter',
                'verbose_name_plural': 'News Letters',
            },
        ),
    ]
