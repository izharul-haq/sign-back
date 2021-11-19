from io import BytesIO
from json import loads
from logging import exception

from flask import Blueprint, jsonify, request, Response
from werkzeug.wsgi import FileWrapper

from services import rsa, dsa
from type_aliases import dsign, key
from utils import sha

Signature = Blueprint('signature', __name__, url_prefix='/sign')


@Signature.route('/key/<string:key_type>', methods=['POST'])
def generate_key(key_type: str):
    try:
        algo: str = request.args.get('algo', type=str)
        req_body = loads(request.data)

        pub_key: key = None
        pri_key: key = None

        # Create public and private keys
        if algo == 'rsa':
            p: int = int(req_body['p'])
            q: int = int(req_body['q'])
            e: int = int(req_body['e'])

            pub_key, pri_key = rsa.generate_key(p, q, e)

        elif algo == 'dsa':
            p: int = int(req_body['p'])
            q: int = int(req_body['q'])
            x: int = int(req_body['x'])

            pub_key, pri_key = dsa.generate_key(p, q, x)

        else:
            raise ValueError(f'Algorithm {algo} is not supported.')

        # Return public key or/and private key
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
        algo = request.args.get('algo', type=str)
        attach = request.args.get('attach', type=int)   # either 0 or 1
        req_file = request.files['message']

        content: bytes = req_file.read()
        digest: int = sha(content)

        # Create digital signature
        signature: dsign = None
        if algo == 'rsa':
            d, n = list(map(int, request.form.get('key').split(', ')))

            signature = rsa.sign(digest, d, n)
            signature: str = hex(signature)[2:].upper()

        elif algo == 'dsa':
            p, q, g, x = list(map(int, request.form.get('key').split(', ')))

            signature = dsa.sign(digest, p, q, g, x)
            signature = ' '.join(hex(s)[2:].upper() for s in signature)

        else:
            raise ValueError(f'Algorithm {algo} is not supported.')

        # Return result
        if attach:
            buffer: bytes = content + b'\n\n\nSIGNATURE:' + signature.encode(
                'utf-8')
            wrapped = FileWrapper(BytesIO(buffer))

            return Response(wrapped, mimetype=req_file.mimetype,
                            direct_passthrough=True), 200

        else:
            return signature, 200

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400


@Signature.route('/verify', methods=['POST'])
def verify():
    try:
        algo = request.args.get('algo', type=str)
        content: bytes = request.files['message'].read()
        sign: str = request.form.get('sign')

        signature: dsign = None
        if sign == '' or sign is None:
            content, sign = content.split(b'\n\n\nSIGNATURE:')
            sign = sign.decode('utf-8')

        digest: int = sha(content)

        is_valid: bool = None

        if algo == 'rsa':
            signature = int(sign, base=16)
            e, n = list(map(int, request.form.get('key').split(', ')))

            is_valid = rsa.verify(digest, signature, e, n)

        elif algo == 'dsa':
            signature = tuple([int(h, base=16) for h in sign.split(' ')])
            p, q, g, y = list(map(int, request.form.get('key').split(', ')))

            is_valid = dsa.verify(digest, signature, p, q, g, y)

        else:
            raise ValueError(f'Algorithm {algo} is not supported.')

        return jsonify(is_valid), 200

    except Exception as e:
        err_message: str = str(e)
        exception(err_message)

        return jsonify({'code': 400, 'message': err_message}), 400
