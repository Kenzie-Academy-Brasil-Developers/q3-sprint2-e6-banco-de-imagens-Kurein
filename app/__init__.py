from http import HTTPStatus
from flask import Flask, jsonify, request, send_file
from app.kenzie import create_files_dir, retrieve_all_files, retrieve_extension_files, allowed_extensions_filter, upload_file, download_filepath
import os

MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")
MAX_CONTENT_LENGTH = int(MAX_CONTENT_LENGTH[:-2])

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH * 1024 * 1024

create_files_dir()

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
            return {'msg': f"file's {file.filename} extension not allowed or incorrect format"}, HTTPStatus.BAD_REQUEST

        upload_file(file)

    return {"msg": "files uploaded"}, HTTPStatus.CREATED

@app.get("/download/<file_name>")
def download(file_name):
    return send_file(download_filepath(file_name), as_attachment=True)