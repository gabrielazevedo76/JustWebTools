# Generated by Django 4.0.3 on 2022-04-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watermarkmodel',
            name='watermarked',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='watermarkmodel',
            name='height',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='watermarkmodel',
            name='width',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]