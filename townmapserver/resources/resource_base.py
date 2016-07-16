import flask.ext.restful as restful


class ResourceBase(restful.Resource):

    """Defines interface for an API flask-restful.Resource

    TODO: Perhaps refactor the class properties in some better way? I just
      need to require a static attribute, perhaps there's a better way.
    """

    @classmethod
    def urls(cls):
        raise NotImplementedError('ResourceBase.urls property not implemented.')

    @classmethod
    def endpoint(cls):
        return cls.__name__.lower()
