# Generated by Django 2.2.1 on 2019-05-20 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_master', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='user',
        ),
        migrations.DeleteModel(
            name='Consumer',
        ),
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]
