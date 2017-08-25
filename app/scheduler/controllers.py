from uuid import uuid4
from flask import Blueprint, jsonify
from tasks.tasks import tasks

scheduler = Blueprint("scheduler", __name__, url_prefix="/test")


@scheduler.route("", methods=["GET"])
def test():
    id_request = uuid4()

    # salvaria no banco
    result = tasks.delay(2, 3)

    return jsonify({"task_id": result.task_id})

@scheduler.route('/<task_id>', methods=["GET"])
def check_request(task_id):
    # verifica como esta o registro no banco
    res = tasks.AsyncResult(task_id)
    return jsonify({"ready": res.ready()})
