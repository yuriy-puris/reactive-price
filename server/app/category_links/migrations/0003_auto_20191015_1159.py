# Generated by Django 2.2.6 on 2019-10-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_links', '0002_auto_20191015_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorylinks',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='categorylinks',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='productcategorypages',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
