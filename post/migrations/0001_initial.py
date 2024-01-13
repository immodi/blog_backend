# Generated by Django 5.0 on 2023-12-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('author', models.TextField()),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
