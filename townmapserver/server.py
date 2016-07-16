import sys

import flask
import flask.ext.restful as restful

import console
# import townmapserver.console as console

flaskApp = flask.Flask(__name__)
# TODO: This is wonky, and is a code smell to me that I need to refactor how
# I have broken up my modules. Need to look into if there is a better way of
# organizing this package. Perhaps include methods to only instantiate when
# launching the server?
#
# The problem is that I need the db variable at the top level of some module
# so that I can define the SqlAlchemy models, but I need to first create a
# Flask app instance to get the db object. So if I split the Model
# definition into a seperate module, I have to import it after I create
# the Flask application at the very least. Only way I see around it right
# now is to use the (uglier) syntax for defining SqlAlchemy Models.
import database   # Trigger the creation of the database definitions
import resources  # We can't import this until after the database module


def add_resources(api, resource_list):
    """Add all resources to the api in the resource list.

    All objects in the resource_list must implement the ResourceBase abc.
    """
    for resource in resource_list:
        api.add_resource(
            resource, *resource.urls(), endpoint=resource.endpoint()
        )


def launch_server(address, port):
    api = restful.Api(flaskApp)
    add_resources(api, resources.ResourceBase.__subclasses__())


def main():
    args = console.parse_arguments(sys.argv[1:])
    launch_server(args.address, args.port)
