# Generated by Django 2.1.2 on 2018-11-26 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20181118_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Resource')),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.resource',),
        ),
    ]