# Generated by Django 3.0.6 on 2020-06-12 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0, editable=False)),
                ('slug', models.SlugField(max_length=75)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('published', 'Published'), ('sold', 'Sold'), ('archived', 'Archived')], default='pending', max_length=15)),
                ('extra_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title second part')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('logo', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Car brand',
                'verbose_name_plural': 'Car brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Car model',
                'verbose_name_plural': 'Car models',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.AddIndex(
            model_name='color',
            index=models.Index(fields=['name'], name='cars_color_name_95ff05_idx'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.CarBrand'),
        ),
        migrations.AddIndex(
            model_name='carbrand',
            index=models.Index(fields=['name'], name='cars_carbra_name_e5d8f6_idx'),
        ),
    ]
