# Generated by Django 4.1.1 on 2022-10-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartitem_cart_alter_cartitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=None, editable=False, null=True),
        ),
    ]
