import uuid, os, json
from Constants import *


def get_template(filename):
    f = open(filename)
    template_json = json.load(f)
    f.close()
    return template_json


def generate_sample(type=None):
    global TEMPLATES
    UUID = str(uuid.uuid1())
    doc_template = get_template(os.path.join(TEMPLATES, type+".JSON"))
    doc_template["_id"]["UUID"] = UUID

    return doc_template
