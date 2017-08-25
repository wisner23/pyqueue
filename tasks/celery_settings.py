TASK_SERIALIZER = "json"
BROKER_URL = "amqp://localhost"
CELERY_IMPORTS = ("tasks",)
CELERY_RESULT_BACKEND = "amqp://localhost"