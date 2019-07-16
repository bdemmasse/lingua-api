from mongoengine import *


connect('linguadb')


class Languages(Document):
    language = StringField(required=True)
    code = StringField(required=True, max_length=3)
    type = StringField(required=True)
    default = BooleanField()


class Sentences(Document):
    text = StringField(required=True)
    lang = ReferenceField(Languages)


class Users(Document):
    fullname = StringField()
    username = StringField(required=True)
    location = StringField()
    avatar = StringField()


class Translations(Document):
    author = ReferenceField(Users)
    targetlang = ReferenceField(Languages)
    sentence = ReferenceField(Sentences)
    file = StringField(required=True)
