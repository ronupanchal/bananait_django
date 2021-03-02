# Generated by Django 3.1.7 on 2021-03-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbanana', '0003_auto_20210301_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title of slider (e.g. Best Company)', max_length=100)),
                ('description', models.TextField(help_text='Enter a description of Slider (e.g. any)', max_length=500)),
                ('sliderimage', models.FileField(upload_to='media/images/')),
            ],
        ),
    ]