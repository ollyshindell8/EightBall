# Generated by Django 3.0 on 2019-12-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eightball', '0002_auto_20191213_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]