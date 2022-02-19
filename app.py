from flask import Flask
from flask_restful import Api
from api.api import Message

app = Flask(__name__)
api = Api(app)
api.add_resource(Message, "/api/message/<int:id>", endpoint="message_endpoint")

if __name__ == "__main__":
    app.run(debug=True)
