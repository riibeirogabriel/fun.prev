# Generated by Django 3.0.6 on 2020-05-30 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('years_old', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=500)),
                ('answer_one', models.CharField(max_length=500)),
                ('answer_two', models.CharField(max_length=500)),
                ('answer_three', models.CharField(max_length=500)),
                ('answer_four', models.CharField(max_length=500)),
                ('true_answer', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
