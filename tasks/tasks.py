from celery import Celery
import time

app = Celery()
app.config_from_object("tasks.celery_settings")

@app.task
def tasks(x, y):

    time.sleep(50)

    return "hello world = %s" % str(x + y)



# Application - > Broker -> WOKER