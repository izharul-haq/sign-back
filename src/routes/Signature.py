from io import BytesIO
from json import loads
from logging import exception

from flask import Blueprint, Response, request, jsonify
from werkzeug.wsgi import FileWrapper

Signature = Blueprint('signature', __name__, url_prefix='sign')


@Signature.route('/key/<string:key_type>', methods=['POST'])
def generate_key(key_type: str):
    try:
        if key_type == 'public':
            pass

        elif key_type == 'private':
            pass

        elif key_type == 'all':
            pass

        else:
            raise ValueError('Key type ${key_type} is not supported.')

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400


@Signature.route('/file', methods=['POST'])
def sign():
    attach_in_file: bool = request.args.get('attach', type=bool)
    algorithm: str = request.args.get('algo', type=str)

    try:
        if algorithm == 'rsa':
            pass

        elif algorithm == 'elg':
            pass

        else:
            raise ValueError(f'algorithm ${algorithm} is not supported.')

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400


@Signature.route('/verify', methods=['POST'])
def verify():
    algorithm: str = request.args.get('algo', type=str)

    try:
        if algorithm == 'rsa':
            pass

        elif algorithm == 'elg':
            pass

        else:
            raise ValueError(f'algorithm ${algorithm} is not supported.')

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400
