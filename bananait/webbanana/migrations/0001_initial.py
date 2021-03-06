# Generated by Django 3.1.7 on 2021-03-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter a email of company (e.g. a@a.com)', max_length=254)),
                ('mobile', models.CharField(help_text='Enter a mobile of company (e.g. +919898257016)', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title of slider (e.g. Best Company)', max_length=100)),
                ('description', models.TextField(help_text='Enter a description of Slider (e.g. any)', max_length=500)),
                ('sliderimage', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='TblTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name (e.g. Ronak Panchal)', max_length=100)),
                ('designation', models.CharField(help_text='Enter a designation (e.g. Web Designer)', max_length=100)),
                ('qualification', models.TextField(help_text='Enter a qualification (e.g. MCA, BTech)', max_length=100)),
                ('social_fb', models.TextField(help_text='Enter a facebook link (e.g. fb/ronak)', max_length=500)),
                ('social_ln', models.TextField(help_text='Enter a linkedin link (e.g. Best Company)', max_length=500)),
                ('social_insta', models.TextField(help_text='Enter a instagram link (e.g. Best Company)', max_length=500)),
                ('social_twitter', models.TextField(help_text='Enter a twitter link (e.g. Best Company)', max_length=500)),
                ('sliderimage', models.FileField(upload_to='photo/')),
            ],
        ),
        migrations.CreateModel(
            name='TblTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a name (e.g. Ronak Panchal)', max_length=100)),
                ('designation', models.CharField(help_text='Enter a designation (e.g. Web Designer)', max_length=100)),
                ('description', models.TextField(help_text='Enter a description (e.g. Brief)', max_length=500)),
                ('photoimage', models.FileField(upload_to='testimonialphoto/')),
            ],
        ),
    ]
