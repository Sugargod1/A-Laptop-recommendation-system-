# Generated by Django 5.0.3 on 2024-03-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_images1_alter_product_images2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mobileness',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='office',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='operating_system',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
