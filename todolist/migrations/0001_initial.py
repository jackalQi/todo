# Generated by Django 2.0.7 on 2018-08-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
