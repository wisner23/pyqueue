from flask import Flask
from app.scheduler.controllers import scheduler

app = Flask(__name__)
app.register_blueprint(scheduler)