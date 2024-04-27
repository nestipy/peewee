import typing

from peewee import TextField, IntegerField, Model as BaseModel

from nestipy_peewee import Model


@Model()
class User:
    name = TextField()
    city = TextField()
    age = IntegerField()


