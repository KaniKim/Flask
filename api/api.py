from flask import Response
from flask_restful import abort, marshal_with, reqparse, Resource
from .domain import Message
from .status import Status
from .crud import CRUD_API


class Message(Resource):
    def abort_if_message_doesnt_exist(self, id):
        if not CRUD_API.get_message(id):
            abort(Status.HTTP_404_NOT_FOUND, message=f"Message {0} doesn't exist")

    @marshal_with(Message.__dict__)
    def get(self, id):
        self.abort_if_message_doesnt_exist(id)
        return CRUD_API.get_message(id)

    def delete(self, id):
        self.abort_if_message_doesnt_exist(id)
        CRUD_API.delete_message(id)
        return Response("", Status.HTTP_204_NO_CONTENT)

    @marshal_with(Message.__dict__)
    def patch(self, id):
        self.abort_if_message_doesnt_exist(id)
        parser = reqparse.RequestParser()
        parser.add_argument("message", type=str)
        parser.add_argument("duration", type=int)
        parser.add_argument("printed_times", type=int)
        parser.add_argument("printed_once", type=bool)

        args = parser.parse_args()
        message = CRUD_API.get_message(id)

        if "message" in args:
            message.message = args["message"]
        if "duration" in args:
            message.duration = args["duration"]
        if "printed_times" in args:
            message.printed_times = args["printed_times"]
        if "printed_once" in args:
            message.printed_once = args["printed_once"]

        return CRUD_API.patch_message(Message, message)
