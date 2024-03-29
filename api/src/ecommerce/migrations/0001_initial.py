# Generated by Django 3.1.6 on 2023-02-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True)),
                ('category', models.CharField(choices=[('headphones', 'Headphones'), ('speakers', 'Speakers'), ('earphones', 'Earphones')], editable=False, max_length=20)),
            ],
        ),
    ]
