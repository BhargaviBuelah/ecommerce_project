# Generated by Django 4.1.1 on 2022-11-02 04:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_product_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('obj1', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
