from json import loads
from logging import exception

from flask import Blueprint, request, jsonify

from services import create_key, create_sign, verify_sign
from utils import generate_hash

Signature = Blueprint('signature', __name__, url_prefix='/sign')


@Signature.route('/key/<string:key_type>', methods=['POST'])
def generate_key(key_type: str):
    try:
        algorithm: str = request.args.get('algo', type=str)
        req_body = loads(request.data)

        pub_key: dict = None
        pri_key: dict = None

        if algorithm == 'rsa':
            p: int = int(req_body['p'])
            q: int = int(req_body['q'])
            e: int = int(req_body['e'])

            pub_key, pri_key = create_key(algorithm, p=p, q=q, e=e)

        elif algorithm == 'elg':
            p: int = int(req_body['p'])
            q: int = int(req_body['q'])
            x: int = int(req_body['x'])

            pub_key, pri_key = create_key(algorithm, p=p, q=q, x=x)

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
    try:
        algorithm: str = request.args.get('algo', type=str)
        content: str = request.files['message'].read()
        hash_value: int = generate_hash(content)

        signature: str = None
        if algorithm == 'rsa':
            d, n = list(map(int, request.form.get('key').split(', ')))

            signature = create_sign(algorithm, hash_value, d=d, n=n)

        elif algorithm == 'elg':
            x, p, q = list(map(int, request.form.get('key').split(', ')))

        else:
            raise ValueError(f'algorithm {algorithm} is not supported.')

        return signature, 200

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400


@Signature.route('/verify', methods=['POST'])
def verify():
    try:
        algorithm: str = request.args.get('algo', type=str)
        content: str = request.files['message'].read()
        signature: str = request.form.get('sign')

        hash_value: int = generate_hash(content)
        hash_sign: int = int('0x' + signature, base=0)

        is_valid: bool = None

        if algorithm == 'rsa':
            e, n = list(map(int, request.form.get('key').split(', ')))

            is_valid = verify_sign(algorithm, hash_value, hash_sign, e=e, n=n)

        elif algorithm == 'elg':
            p, q, g, y = list(map(int, request.form.get('key').split(', ')))

        else:
            raise ValueError(f'algorithm {algorithm} is not supported.')

        return jsonify(is_valid), 200

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400
