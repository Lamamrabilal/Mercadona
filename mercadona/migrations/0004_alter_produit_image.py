# Generated by Django 4.2.6 on 2023-11-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadona', '0003_remove_promotion_nouveau_prix_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]