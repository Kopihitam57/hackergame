# Generated by Django 3.1 on 2020-09-08 13:42

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20200829_1930'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='application',
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='apply_hint',
            field=models.TextField(blank=True, help_text='给申请者的提示'),
        ),
        migrations.AlterField(
            model_name='group',
            name='rule_email_suffix',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='verified',
            field=models.BooleanField(default=False, help_text='是否为认证过的组'),
        ),
    ]