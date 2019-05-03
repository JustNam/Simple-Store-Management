from flask import request, jsonify


def message(text, code):
    return jsonify({"message": text}), code


def convert_request_to_dict():
    # print(request.form)
    print(request)
    if request.content_type != 'application/json':
        return {'error': message("The request format have to be JSON", 400)}
    try:
        data = request.json
    except:
        return {'error': message("The request did not meet JSON syntax", 400)}
    return data
