# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangoperm.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('name', djangoperm.db.fields.TextField(help_text='特定地址的名称', perms={'read': False, 'write': False}, verbose_name='地址名称')),
            ],
            options={
                'verbose_name_plural': '地址',
                'verbose_name': '地址',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('name', djangoperm.db.fields.CharField(help_text='城市的名称', max_length=90, perms={'read': False, 'write': False}, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '城市',
                'verbose_name': '城市',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('name', djangoperm.db.fields.CharField(help_text='公司的名称', max_length=90, perms={'read': False, 'write': False}, verbose_name='名称')),
                ('tel', djangoperm.db.fields.CharField(default='', help_text='公司电话', max_length=32, perms={'read': False, 'write': False}, verbose_name='电话')),
                ('address', models.OneToOneField(help_text='公司的所在地址,必须为公司对应合作伙伴的常用送货地址', on_delete=django.db.models.deletion.CASCADE, to='account.Address')),
            ],
            options={
                'verbose_name_plural': '公司',
                'verbose_name': '公司',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('name', djangoperm.db.fields.CharField(help_text='顾客的名称', max_length=90, perms={'read': False, 'write': False}, unique=True, verbose_name='名称')),
                ('can_sale', djangoperm.db.fields.BooleanField(default=True, help_text='合作伙伴是否可被销售货物', perms={'read': False, 'write': False}, verbose_name='可销售状态')),
                ('can_purchase', djangoperm.db.fields.BooleanField(default=False, help_text='是否可向合作伙伴采购', perms={'read': False, 'write': False}, verbose_name='可采购状态')),
                ('default_send_address', models.ForeignKey(blank=True, help_text='顾客设置的默认送货地址', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_customers', to='account.Address', verbose_name='默认地址')),
                ('usual_send_addresses', models.ManyToManyField(help_text='顾客的常用送货地址', related_name='usual_customers', to='account.Address', verbose_name='常用地址')),
            ],
            options={
                'verbose_name_plural': '合作伙伴',
                'verbose_name': '合作伙伴',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('user', models.OneToOneField(help_text='一对一绑定的相关django内置用户', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='绑定用户')),
                ('sex', djangoperm.db.fields.CharField(choices=[('unknown', '未知'), ('male', '男'), ('female', '女')], default='unknown', help_text='用户的性别', max_length=10, perms={'read': False, 'write': False}, verbose_name='性别')),
                ('phone', djangoperm.db.fields.CharField(default=None, help_text='用户唯一的移动电话', max_length=11, null=True, perms={'read': False, 'write': False}, unique=True, verbose_name='移动电话')),
                ('mail_notice', djangoperm.db.fields.BooleanField(default=True, help_text='站内邮件提醒状态,为True时,实时提醒用户有未读的新邮件', perms={'read': False, 'write': False}, verbose_name='邮件提醒')),
                ('language', djangoperm.db.fields.CharField(help_text='用户设置的默认语言', max_length=20, null=True, perms={'read': False, 'write': False}, verbose_name='语言')),
                ('online_notice', djangoperm.db.fields.BooleanField(default=False, help_text='在线提醒状态,为True时,其他用户可以接收该用户的在线状态,并告知其下线', perms={'read': False, 'write': False}, verbose_name='在线提醒')),
            ],
            options={
                'verbose_name_plural': '用户其他资料',
                'verbose_name': '用户其他资料',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('country', djangoperm.db.fields.CharField(choices=[('China', '中国')], help_text='省份的所属国家', max_length=90, perms={'read': False, 'write': False}, verbose_name='国家')),
                ('name', djangoperm.db.fields.CharField(help_text='省份的名称', max_length=90, perms={'read': False, 'write': False}, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '省份',
                'verbose_name': '省份',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('name', djangoperm.db.fields.CharField(help_text='地区的名称', max_length=90, perms={'read': False, 'write': False}, verbose_name='名称')),
                ('city', models.ForeignKey(help_text='地区的所属城市', on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='account.City', verbose_name='城市')),
            ],
            options={
                'verbose_name_plural': '地区',
                'verbose_name': '地区',
            },
        ),
        migrations.AlterUniqueTogether(
            name='province',
            unique_together=set([('country', 'name')]),
        ),
        migrations.AddField(
            model_name='company',
            name='belong_customers',
            field=models.ManyToManyField(help_text='管理公司的人员', related_name='belong_companies', to='account.Partner', verbose_name='公司管理员'),
        ),
        migrations.AddField(
            model_name='company',
            name='customer',
            field=models.OneToOneField(blank=True, help_text='代表该公司本身的顾客', on_delete=django.db.models.deletion.CASCADE, related_name='company', to='account.Partner', verbose_name='绑定顾客'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(help_text='城市的所属省份', on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='account.Province', verbose_name='省份'),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.ForeignKey(help_text='地址的所属地区', on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='account.Region', verbose_name='地区'),
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('city', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('province', 'name')]),
        ),
    ]
