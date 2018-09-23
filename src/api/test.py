from src.validator import validate, field
from flask import Blueprint, request
from src.services.user import UserService

bp = Blueprint('test', __name__)


@bp.route('/register', methods=['POST'])
def register():
    body = validate({
        'email': field('email'),
        'password': field('password'),
        'repeat_password': field('password'),
        'tos': field('tos')
    }, request.get_json(force=True, silent=True))

    UserService.add_user(body)

    return 'Hi'
