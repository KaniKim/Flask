from flask import Flask
from api.models import db

app = Flask(__name__)

app.config["SECRET_KEY"] = "this is secret"
app.config["SQLALCEHMY_DATABASE_URI"] = "postgresql://kanikim:rlarhksgml!4113@127.0.0.1:5432/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWM"] = True