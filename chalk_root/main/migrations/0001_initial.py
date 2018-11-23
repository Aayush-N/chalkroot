# Generated by Django 2.0.9 on 2018-11-12 09:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField(blank=True, null=True)),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('address_line1', models.CharField(blank=True, max_length=30, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=30, null=True)),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('facilities', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.CharField(blank=True, max_length=30, null=True)),
                ('photos', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('admission_info', models.TextField(blank=True, null=True)),
                ('overall_rating', models.FloatField(blank=True, null=True)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Board')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Type of User')),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.School'),
        ),
    ]
