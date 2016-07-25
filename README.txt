运行项目
python manage.py runserver 0.0.0.0:80

初始化项目
python manage.py migrate

添加新的APP
python manage.py startapp login

初始化数据库
python manage.py migrate
python manage.py createsuperuser

一、用户登录
1、创建App login
# python manage.py startapp login

2、修改models.py
# cd login
# vim models.py
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

admin.site.register(User)

3、修改settings.py
# cd ../mysite
# vim settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',        # 新添加的内容，为之前添加的APP名称
]
# 注释掉MIDDLEWARE_CLASSES中的'django.middleware.csrf.CsrfViewMiddleware'
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

4、初始化
# cd ..
初始化项目
# python manage.py migrate
创建super用户
# python manage.py createsuperuser
