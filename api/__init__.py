"""
API Package - define the REST API using Flask-Restful package.py

    /process_data - start a summy long operation on a Celery worker and return the ID of a new task.

    /tasks/<tasks_id> - Return the status of a task by task ID.
"""

import time
from flask import jsonify
from flask_restful import Api, Resource
from tasks import celery
import config

api = Api(prefix=config.API_PREFIX)

class TaskStatusAPI(Resource):
    def get(self, task_id):
        task = celery.AsyncResult(task_id)
        return jsonify(task.result)

class DataProcessingAPI(Resource):
    def post(self):
        task = process_data.delay()
        return {'task_id': task.id}, 200
        
@celery.task()
def preprocess_data():
    time.sleep(60)

#data processing endpoint
api.add_resource(dataProcessingAPI, '/process_data')

#task status endpoint
api.add_resource(TaskStatusAPI, '/tasks/<string:task_id>')