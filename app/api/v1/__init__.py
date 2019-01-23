from flask import Blueprint
from flask_restful import Api, Resource
from .views.views import *

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)            

api.add_resource(HomePage, '/')
api.add_resource(PostParcel,'/parcel',strict_slashes=False)
api.add_resource(GetSpecificOrder,'/parcels/<int:parcel_id>', strict_slashes=False)
api.add_resource(GetAll,'/parcels', strict_slashes=False)
api.add_resource(CancelSpecific,'/parcels/<int:parcel_id>', strict_slashes=False)
api.add_resource(GetUserOrders, '/parcels/<string:sender_email>', strict_slashes=False)

