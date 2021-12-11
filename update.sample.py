import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person
from django.utils import timezone
import pytz

person = Person.objects.get(id=1)
print(person)
person.birthday = '2001-01-01'
person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
person.save()

persons = Person.objects.filter(first_name='Taro')
for person in persons:
  person.first_name = person.first_name.lower()
  person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
  # person.save()
# 上記は一つずつ更新するため処理が遅い、下記は一気に処理するため更新が早い
Person.objects.filter(first_name='Saburo').update(
  web_site='http://sample.jp',
  update_at=timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
)