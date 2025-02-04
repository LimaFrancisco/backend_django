# Generated by Django 4.2.16 on 2024-10-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.CharField(default='', max_length=250)),
                ('release_date', models.DateTimeField()),
                ('toy_category', models.CharField(default='', max_length=200)),
                ('was_included_in_home', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
