# Generated by Django 4.1.7 on 2023-02-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Project',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='technology',
            new_name='price',
        ),
    ]
