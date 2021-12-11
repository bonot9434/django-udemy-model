import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

Person.objects.filter(first_name='Saburo')

Person.objects.filter(first_name='taro', birthday='2001-01-01').delate()

# 全権削除
Person.objects.all().delete()
