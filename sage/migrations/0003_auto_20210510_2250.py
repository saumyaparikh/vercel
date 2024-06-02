# Generated by Django 3.2 on 2021-05-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage', '0002_vmain'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmain',
            name='haddr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vmain',
            name='hclosed',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vmain',
            name='hcordinate',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vmain',
            name='hdis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vmain',
            name='himage',
            field=models.ImageField(default='', upload_to='byimgs'),
        ),
        migrations.AddField(
            model_name='vmain',
            name='hlink',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vmain',
            name='hmap',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vmain',
            name='hphone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vmain',
            name='htiming',
            field=models.CharField(default='', max_length=100),
        ),
    ]
