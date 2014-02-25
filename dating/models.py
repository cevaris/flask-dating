import datetime
from flask import url_for
from dating import db
from slugify import slugify
import random

class Pets(db.Document):

    name = db.StringField(max_length=255, required=True, unique=True)
    slug = db.StringField(max_length=255, required=False)
    pet_type = db.StringField(max_length=255, required=True)
    birthdate = db.DateTimeField(required=False)
    weight = db.StringField(max_length=255, required=True)
    color = db.StringField(max_length=255, required=True)

    def __unicode__(self):
        return self.name

    def clean(self):
        self.slug = slugify(self.name)

        year = random.choice(range(2000, 2014))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 28))
        self.birthdate = datetime.date(year, month, day)




