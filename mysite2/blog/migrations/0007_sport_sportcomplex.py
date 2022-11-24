# Generated by Django 4.1.3 on 2022-11-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
            ],
            options={
                'db_table': '시설명',
            },
        ),
        migrations.CreateModel(
            name='SportComplex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=70)),
                ('detail', models.CharField(default='', max_length=70)),
                ('lon', models.CharField(default='', max_length=70)),
                ('lat', models.CharField(default='', max_length=70)),
                ('status', models.CharField(default='', max_length=70)),
                ('name', models.ManyToManyField(related_name='mysite2', to='blog.sport')),
            ],
            options={
                'db_table': '공공체육시설',
            },
        ),
    ]