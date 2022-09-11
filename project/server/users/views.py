from flask import Blueprint, make_response, jsonify
from flask.views import MethodView

from project.server.models import User

users_blueprint = Blueprint('user', __name__)

class UsersAPI(MethodView):

  def get(self):
    users = User.query.all()
    response = {
      "users": []
    }
    for user in users:
      response["users"].append({
        "admin": user.admin,
        "email": user.email,
        "id": user.id,
        "registered_on": user.registered_on
      })
    return make_response(jsonify(response), 201)

# define the API resources
users_view = UsersAPI.as_view('user_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)