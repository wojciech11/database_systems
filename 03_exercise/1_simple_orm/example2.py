import peewee
from peewee import *

db = MySQLDatabase("university", user="root", passwd="nomoresecret")


class Departament(peewee.Model):
    name = peewee.TextField()

    class Meta:
        database = db


class Lecturer(peewee.Model):
    name = peewee.CharField()
    title = peewee.TextField()
    departament = ForeignKeyField(Departament, backref="departament")

    class Meta:
        database = db


Departament.create_table()
Lecturer.create_table()

dep = Departament(dep="computer science")
dep.save()

for d in [{"name": "Natalia", "title": "Dr"}, {"name": "John", "title": "MSc"}]:
    lecturer = Lecturer(name=d["name"], title=d["title"], departament=dep)
    lecturer.save()

for l in Lecturer.filter(departament=dep):
    print(l.name, l.title, l.departament)

# Lecturer.drop_table()
# Departament.drop_table()
