# Generated by Django 3.2 on 2022-01-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=130)),
                ('last_name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('feedback', models.TextField(blank=True)),
            ],
        ),
    ]
