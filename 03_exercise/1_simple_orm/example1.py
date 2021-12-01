import peewee
from peewee import *

db = MySQLDatabase("university", user="root", passwd="nomoresecret")


class Lecturer(peewee.Model):
    name = peewee.CharField()
    title = peewee.TextField()
    dep = peewee.TextField()

    class Meta:
        database = db


Lecturer.create_table()
lecturer = Lecturer(name="Natalia", title="Dr", dep="computer science")
lecturer.save()

for l in Lecturer.filter(dep="computer science"):
    print(l.name, l.title, l.dep)

# Lecturer.drop_table()
