# Generated by Django 5.0.4 on 2024-04-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_travelplan_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='travelplan',
            name='categories',
        ),
        migrations.AddField(
            model_name='travelplan',
            name='categories',
            field=models.ManyToManyField(to='users.category'),
        ),
    ]
