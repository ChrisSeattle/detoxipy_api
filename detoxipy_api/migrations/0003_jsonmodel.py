# Generated by Django 2.1.2 on 2018-10-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detoxipy_api', '0002_delete_sessioncache'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSONModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('json_chat', models.TextField()),
            ],
        ),
    ]