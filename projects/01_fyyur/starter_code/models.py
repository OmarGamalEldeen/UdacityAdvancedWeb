import json
import dateutil.parser
import babel
from flask import Flask,render_template,request,redirect,url_for,jsonify,abort,flash
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
import sys


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,unique=True, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,unique=True, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500),unique=True, nullable=False)
    facebook_link = db.Column(db.String(120))
    def __repr__(self):
        return f'<Artist ID: {self.id}, name: {self.name} , city : {self.city}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer,db.ForeignKey('Venue.id'))
    venue_name = db.Column(db.String(120),db.ForeignKey('Venue.name'))
    artist_id = db.Column(db.Integer,db.ForeignKey('Artist.id'))
    artist_name =  db.Column(db.String(120),db.ForeignKey('Artist.name'))
    artist_image_link = db.Column(db.String(500),db.ForeignKey('Artist.image_link'))
    start_time = db.Column(db.DateTime)

#db.drop_all() 
db.create_all()
db.session.commit()