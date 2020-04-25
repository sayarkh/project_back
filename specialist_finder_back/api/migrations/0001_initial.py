# Generated by Django 3.0.4 on 2020-04-25 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('age', models.IntegerField(default='')),
                ('gender', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('likes', models.IntegerField(default='')),
                ('comments', models.CharField(max_length=250)),
                ('front_image', models.CharField(max_length=1000)),
                ('first_image', models.CharField(default='', max_length=1000)),
                ('second_image', models.CharField(default='', max_length=1000)),
                ('third_image', models.CharField(default='', max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialists', to='api.Category')),
            ],
            options={
                'verbose_name': 'Specialist',
                'verbose_name_plural': 'Specialists',
            },
        ),
    ]
