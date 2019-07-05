# Generated by Django 2.0.2 on 2019-07-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pubdate', models.DateTimeField()),
                ('body', models.TextField()),
                ('bimage', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
