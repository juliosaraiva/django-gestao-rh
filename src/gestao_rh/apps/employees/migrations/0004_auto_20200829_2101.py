# Generated by Django 3.1 on 2020-08-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20200829_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Enabled'), (0, 'Disabled')], default=1),
        ),
    ]
