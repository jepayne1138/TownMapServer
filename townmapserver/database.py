import datetime

import flask_sqlalchemy

import townmapserver.server as server
import townmapserver.config_manager as cm


# To use, we need to create a settings.py modules in the same directory with
# the following variables (USER, PASSWORD, HOST, PORT, DATABASE)
DATABASE_URI = 'postgresql://{User}:{Password}@{Host}:{Port}/{Name}'.format(
    **cm.config['Database']
)


server.flaskApp.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# Disable Flask-SQLAlchemy tracking of modification to objects
# See: http://flask-sqlalchemy.pocoo.org/2.1/config/
server.flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(server.flaskApp)


class User(db.Model):

    userId = db.Column(db.Integer, primary_key=True)
    googleId = db.Column(db.String(32), unique=True)  # TODO: Check length
    trainerName = db.Column(db.String(32), unique=True)
    trainerLevel = db.Column(db.Integer)

    def __init__(self, googleId, trainerName, trainerLevel=0):
        self.googleId = googleId
        self.trainerName = trainerName
        self.trainerLevel = trainerLevel


# Database table definition
class Catch(db.Model):

    catchId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'))
    user = db.relationship('User', backref=db.backref('catches', lazy='joined'))
    usingLure = db.Column(db.Boolean)
    usingIncense = db.Column(db.Boolean)
    creatureId = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    catchTime = db.Column(db.Float)  # Store as Unix time

    def __init__(
            self, user, creatureId, latitude, longitude,
            usingLure=False, usingIncense=False, catchTime=None):
        self.user = user
        self.creatureId = creatureId
        self.usingLure = usingLure
        self.usingIncense = usingIncense
        self.latitude = latitude
        self.longitude = longitude
        if catchTime is None:
            catchTime = datetime.datetime.utcnow()
        self.catchTime = catchTime
