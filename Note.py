import uuid
from datetime import datetime

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:4], name = "text", content = "text", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.name = name
        self.content = content
        self.date = date

    def get_id(note):
        return note.id

    def get_name(note):
        return note.name

    def get_content(note):
        return note.content

    def get_date(note):
        return note.date


    def set_id(note):
        note.id = str(uuid.uuid1())[0:4]

    def set_name(note, name):
        note.name = name

    def set_content(note, content):
        note.content = content

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


    def to_string(note):
        return note.id + ';' + note.name + ';' + note.content + ';' + note.date

    def info(note):
        return '\n Title: ' + note.name + '\n Id:' + note.id + '\n Content:' + note.content + '\n Creation date:' + note.date
