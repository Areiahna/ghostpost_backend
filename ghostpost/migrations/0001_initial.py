# Generated by Django 3.1.2 on 2020-10-04 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(choices=[('Roast', 'Roast'), ('Boast', 'Boast')], max_length=20)),
                ('upvotes', models.PositiveIntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=150)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
