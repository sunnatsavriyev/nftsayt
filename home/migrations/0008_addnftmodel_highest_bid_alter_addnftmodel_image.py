# Generated by Django 4.2.7 on 2023-11-15 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_addnftmodel_delete_usermodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='addnftmodel',
            name='Highest_Bid',
            field=models.CharField(default='0wETH', max_length=50),
        ),
        migrations.AlterField(
            model_name='addnftmodel',
            name='image',
            field=models.ImageField(blank=True, default='defult_img', null=True, upload_to='image/'),
        ),
    ]
