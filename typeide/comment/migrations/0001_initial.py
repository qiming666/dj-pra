# Generated by Django 3.2.5 on 2021-07-21 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('status', models.PositiveBigIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='评论目标')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
