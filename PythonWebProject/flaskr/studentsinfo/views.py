import json
from . import student
from flask import request, abort, jsonify
from flaskr.PythonWebProjectBLL.StudentsInfoManager import StudentsInfoManager


@student.route("/index")
def index():
    return f"<a>this is a student</a>"


@student.route("/all")
def QueryAllStudents():
    sm = StudentsInfoManager()
    result = sm.QueryAll()
    jsonresult = json.dumps(result, default=lambda obj: obj.__dict__, sort_keys=True, ensure_ascii=False)
    return jsonresult, 200, {'Content-Type': 'application/json'}


@student.route("/", methods=['GET'])
def querystu():
    if not 'words' in request.args.keys():
        abort(400)
    else:
        sm = StudentsInfoManager()
        words = request.args.get('words')
        result = sm.querystu(words)
        jsonresult = json.dumps(result, default=lambda obj: obj.__dict__, sort_keys=True, ensure_ascii=False)
        return jsonresult, 200, {'Content-Type': 'application/json'}


@student.route("/", methods=['POST'])
def addstu():
    if not request.json:
        abort(400)
    else:
        sm = StudentsInfoManager()
        newinfo = request.json
        result = sm.addnewstu(newinfo)
        return jsonify(result), 200


@student.route("/<int:sid>", methods=['PUT'])
def updatestu(sid):
    if not isinstance(sid, int) or not request.json:
        abort(404)
    sm = StudentsInfoManager()
    newinfo = request.json
    result = sm.updatestu(sid, newinfo)
    return jsonify(result), 200


@student.route("/<int:sid>", methods=['DELETE'])
def delstu(sid):
    if not isinstance(sid, int):
        abort(404)
    sm = StudentsInfoManager()
    result = sm.delstu(sid)
    return jsonify(result), 200
