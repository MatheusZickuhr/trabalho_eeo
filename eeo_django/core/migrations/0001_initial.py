# Generated by Django 2.1.3 on 2018-11-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
