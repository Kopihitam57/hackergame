# Generated by Django 2.1.12 on 2019-10-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0005_auto_20191012_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='challenge',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='group',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.IntegerField(db_index=True),
        ),
    ]