# Generated by Django 2.2.6 on 2019-10-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='auto_increment_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
