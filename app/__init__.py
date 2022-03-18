from http import HTTPStatus
from flask import Flask, jsonify, request
from app.kenzie import create_files, retrieve_all_files, retrieve_extension_files, allowed_extensions_filter, upload_file

app = Flask(__name__)

create_files()

@app.get("/files")
def list_files():
    return jsonify(retrieve_all_files()), HTTPStatus.OK

@app.get("/files/<extension>")
def list_files_by_extension(extension):

    if allowed_extensions_filter(extension):
        return {'msg': f'extension {extension} not allowed or incorrect format'}, HTTPStatus.BAD_REQUEST

    return jsonify(retrieve_extension_files(extension)), HTTPStatus.OK

@app.post("/upload")
def upload():

    for file in request.files.values():
        if allowed_extensions_filter(file.filename):
            return {'msg': f'extension {file.filename} not allowed or incorrect format'}, HTTPStatus.BAD_REQUEST

        upload_file(file)

    return {"msg": "files uploaded"}, HTTPStatus.CREATED

@app.get("/download/<file_name>")
def download(file_name):
    return ""