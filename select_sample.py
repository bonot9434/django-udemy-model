import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

#  全て取得
person = Person.objects.all()
for person in person:
    print(person.id, person, person.salary)

# person = Person.objects.get(first_name = 'Taro') getは複数いるとエラー
# person = Person.objects.get(first_name = 'taro') 大文字小文字判別するためエラー
person = Person.objects.get(pk=1)

print(person.id, person)

# filter(絞込、エラーにならない、複数取得)
print('*' * 100)
# persons = Person.objects.filter(first_name='Taro').all()
persons = Person.objects.filter(first_name='Taro', id=1)
print(persons)
print(persons[0].email)
for person in persons:
    print(person.id, person)