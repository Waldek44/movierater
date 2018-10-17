# Generated by Django 2.1.2 on 2018-10-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('description', models.TextField(default='')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('relaesed', models.DateField(blank=True, null=True)),
                ('imdb_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='filmowe')),
            ],
        ),
    ]
