# Generated by Django 3.2.6 on 2021-09-09 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('new', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact_no', models.CharField(max_length=14, unique=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
