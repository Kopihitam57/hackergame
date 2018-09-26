# Generated by Django 2.1.1 on 2018-09-26 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('flag', models.TextField(unique=True)),
                ('score', models.IntegerField(default=100)),
            ],
            bases=(utils.models.DictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ctf.Flag')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('is_open', models.BooleanField(default=False)),
                ('name', models.TextField()),
                ('detail', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
            ],
            bases=(utils.models.DictMixin, utils.models.NameMixin, models.Model),
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Solve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctf.Flag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctf.Problem'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flag',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.Problem'),
        ),
    ]