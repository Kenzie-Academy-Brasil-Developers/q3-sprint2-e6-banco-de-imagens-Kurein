from http import HTTPStatus
from flask import Flask, jsonify
from app.kenzie import create_files, retrieve_all_files, retrieve_extension_files, allowed_extensions_filter

app = Flask(__name__)

create_files()

@app.get("/files")
def list_files():
    return jsonify(retrieve_all_files()), HTTPStatus.OK

@app.get("/files/<extension>")
def list_files_by_extension(extension):

    if allowed_extensions_filter(extension):
        return {'msg': f'extension {extension} not allowed or incorrect format'}, HTTPStatus.BAD_REQUEST

    return jsonify(retrieve_extension_files(extension))

@app.post("/upload")
def upload():
    return ""

@app.get("/download/<file_name>")
def download(file_name):
    return ""