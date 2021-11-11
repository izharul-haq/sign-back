from io import BytesIO
from json import loads
from logging import exception

from flask import Blueprint, Response, request, jsonify
from werkzeug.wsgi import FileWrapper

from services import create_key

Signature = Blueprint('signature', __name__, url_prefix='/sign')


# TODO : implement generate key using elgamal algorithm
@Signature.route('/key/<string:key_type>', methods=['POST'])
def generate_key(key_type: str):
    algorithm: str = request.args.get('algo', type=str)

    try:
        req_body = loads(request.data)

        pub_key: dict = None
        pri_key: dict = None

        if algorithm == 'rsa':
            p: int = req_body['p']
            q: int = req_body['q']
            e: int = req_body['e']

            pub_key, pri_key = create_key(algorithm, p=p, q=q, e=e)

        elif algorithm == 'elg':
            pass

        else:
            raise ValueError(f'Algorithm {algorithm} is not supported.')

        if key_type == 'public':
            return jsonify({'pub_key': pub_key}), 200

        elif key_type == 'private':
            return jsonify({'pri_key': pri_key}), 200

        elif key_type == 'all':
            return jsonify({'pub_key': pub_key, 'pri_key': pri_key}), 200

        else:
            raise ValueError(f'Key type {key_type} is not supported.')

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
            raise ValueError(f'algorithm {algorithm} is not supported.')

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
            raise ValueError(f'algorithm {algorithm} is not supported.')

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400
