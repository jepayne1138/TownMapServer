import flask_restful as restful
import flask_restful.reqparse as reqparse
import flask_restful.fields as fields

from townmapserver.resources import resource_base as rb
import townmapserver.database as database

db = database.db


CATCHES_MARSHALLER = {
    'trainerName': fields.String(attribute=lambda u: u.trainerName),
    'trainerLevel': fields.Integer(attribute=lambda u: u.trainerLevel),
    'usingLure': fields.Integer,
    'uwingIncense': fields.Boolean,
    'creatureId': fields.Boolean,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'catchTime': fields.Float,
}


class Catches(rb.ResourceBase):

    @classmethod
    def urls(cls):
        return '/catches'

    @classmethod
    def endpoint(cls):
        return 'catches'

    @restful.marshal_with(CATCHES_MARSHALLER)
    def get(self):
        """Query catches with possible filters"""
        parser = reqparse.RequestParser()

        # TODO: Set up this authentication after I get the API working
        # parser.add_argument('token', type=str, required=True, help='Invalid access token')

        parser.add_argument('starttime', type=float, default=None)
        parser.add_argument('endtime', type=float, default=None)
        parser.add_argument('limit', type=int, default=None)
        args = parser.parse_args()

        # Build the query based on the given arguments
        catch_query = database.Catch.query
        if args.starttime is not None:
            catch_query.filter_by(database.Catch.catchTime >= args.starttime)
        if args.starttime is not None:
            catch_query.filter_by(database.Catch.catchTime <= args.endtime)
        if args.limit is not None:
            catch_query.limit(args.limit)

        # Fetch, marshal, and return the catches
        return catch_query.all()

    @restful.marshal_with(CATCHES_MARSHALLER)
    def post(self):
        """Add a catch"""
        parser = reqparse.RequestParser()

        # TODO: Set up this authentication after I get the API working
        # parser.add_argument('token', type=str, required=True, help='Invalid access token')

        parser.add_argument('usingLure', type=bool, required=True)
        parser.add_argument('usingIncense', type=bool, required=True)
        parser.add_argument('latitude', type=float, required=True)
        parser.add_argument('longitude', type=float, required=True)
        parser.add_argument('catchTime', type=float, required=True)
        args = parser.parse_args()

        # Create the new catch and add it to the database
        user = database.User.query.filter_by(database.User.token == args.token).first()
        new_catch = database.Catch(
            user, args.creatureId, args.usingLure,
            args.usingIncense, args.latitude, args.longitude, args.catchTime
        )
        db.session.add(new_catch)
        db.session.commit()
        return new_catch
