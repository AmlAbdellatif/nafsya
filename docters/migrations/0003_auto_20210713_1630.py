# Generated by Django 2.0.7 on 2021-07-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docters', '0002_alter_docter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docter',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
