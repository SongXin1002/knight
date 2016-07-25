运行项目
python manage.py runserver 0.0.0.0:80

前言
1、关联包安装
# yum install python-pip
# yum install mysql*
# yum install python-devel
# pip install MySQLdb
# pip install pexpect

2、Django安装APP
创建APP
# python manage.py startapp ${AppName}
安装APP（编辑settings.py）
# vim mysite/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '${AppName}',
]

3、Django连接数据库
# vim mysite/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'knight',        # 数据库名
        'USER': 'knight',        # 用户名
        'PASSWORD': 'knight',    # 密码
        'HOST': '192.168.1.12',  # MySQL主机IP
        'PORT': '3306',          # MySQL端口
    }
}

4、创建和修改数据库
生成并安装一个新的Django APP(AppName:MySQL)
编写项目models
# vim MySQL/models.py
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class songxin(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=10)

执行项目，使刚定义的表写入数据库
# python manage.py makemigrations
# python manage.py migrate

一、用户登录
1、生成并安装一个新的Django APP(AppName:login)
2、修改models.py
# vim login/models.py
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

admin.site.register(User)

4、初始化
# python manage.py migrate
5、创建super用户
# python manage.py createsuperuser
