# Generated by Django 4.2 on 2024-01-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productitem_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='additional_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
