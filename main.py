import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person
p = Person(
  first_name = 'Taro', last_name = 'Sato',
  birthday = '2000-01-01', email = 'test@test.com',
  salary = 10000, memo = 'memo taro', web_site = 'http://www.google'
)
p.save()