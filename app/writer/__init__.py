from flask import Blueprint
writer_user = Blueprint('writer_user', __name__)
from . import views