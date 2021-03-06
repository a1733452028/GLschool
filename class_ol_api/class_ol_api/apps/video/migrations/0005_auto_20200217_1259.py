# Generated by Django 2.2.7 on 2020-02-17 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_homevideo_shortvideo_video_videotype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homevideo',
            options={'verbose_name': '首页轮播', 'verbose_name_plural': '首页轮播'},
        ),
        migrations.AlterModelOptions(
            name='shortvideo',
            options={'verbose_name': '短视频展示', 'verbose_name_plural': '短视频展示'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '视频管理', 'verbose_name_plural': '视频管理'},
        ),
        migrations.AlterModelOptions(
            name='videotype',
            options={'verbose_name': '视频分类', 'verbose_name_plural': '视频分类'},
        ),
        migrations.AlterModelTable(
            name='homevideo',
            table='gl_HomeVideo',
        ),
        migrations.AlterModelTable(
            name='shortvideo',
            table='gl_ShortVideo',
        ),
        migrations.AlterModelTable(
            name='video',
            table='gl_Video',
        ),
        migrations.AlterModelTable(
            name='videotype',
            table='gl_VideoType',
        ),
    ]
