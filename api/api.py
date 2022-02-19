from flask import Flask, Response
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
import datetime
from models import Message
from domain import Message
import status
from pytz import utc
import crud


class Message(Resource):
    def abort_if_message_doesnt_exist(self, id):
        if not crud.get_message(id):
            abort(status.HTTP_404_NOT_FOUND, message=f"Message {0} doesn't exist")

    @marshal_with(Message.__dict__)
    def get(self, id):
        self.abort_if_message_doesnt_exist(id)
        return crud.get_message(id)

    def delete(self, id):
        self.abort_if_message_doesnt_exist(id)
        crud.delete_message(id)
        return Response("", status.HTTP_204_NO_CONTENT)

    @marshal_with(Message.__dict__)
    def patch(self, id):
        pass
