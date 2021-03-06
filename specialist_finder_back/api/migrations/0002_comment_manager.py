# Generated by Django 3.0.4 on 2020-04-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default title', max_length=100)),
                ('text', models.CharField(default='default text', max_length=1000)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialists', to='api.Specialist')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
