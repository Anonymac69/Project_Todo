# Generated by Django 3.0.3 on 2020-03-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='active',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='body',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=200, null='False'),
            preserve_default='False',
        ),
    ]
