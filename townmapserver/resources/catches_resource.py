import flask_restful as restful
import flask_restful.reqparse as reqparse
import flask_restful.fields as fields

from townmapserver.resources import resource_base as rb
import townmapserver.database as db


CATCHES_MARSHALLER = {
    'trainerName': fields.String(attribute=lambda x: x.user.trainerName),
    'trainerLevel': fields.Integer(attribute=lambda x: x.user.trainerLevel),
    'usingLure': fields.Boolean,
    'uwingIncense': fields.Boolean,
    'creatureId': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'catchTime': fields.Float,
}


class Catches(rb.ResourceBase):

    @classmethod
    def urls(cls):
        return ['/catches']

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
        catch_query = db.Catch.query.order_by(db.Catch.catchTime.desc())
        if args.starttime is not None:
            catch_query = catch_query.filter(
                db.Catch.catchTime >= args.starttime
            )
        if args.endtime is not None:
            catch_query = catch_query.filter(
                db.Catch.catchTime <= args.endtime
            )
        if args.limit is not None:
            catch_query = catch_query.limit(args.limit)

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

        # Create the new catch and add it to the db
        user = db.User.query.filter(db.User.token == args.token).first()
        new_catch = db.Catch(
            user, args.creatureId, args.usingLure,
            args.usingIncense, args.latitude, args.longitude, args.catchTime
        )
        db.session.add(new_catch)
        db.session.commit()
        return new_catch
