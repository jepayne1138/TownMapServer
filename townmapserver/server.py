import flask
import flask.ext.restful as restful

import resources

flaskApp = flask.Flask(__name__)


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
