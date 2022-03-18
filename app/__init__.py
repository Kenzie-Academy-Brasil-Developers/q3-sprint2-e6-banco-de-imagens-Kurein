from flask import Flask, jsonify
from app.kenzie import retrieve_all_files, create_files

app = Flask(__name__)

create_files()

@app.post("/upload")
def upload():
    return ""

@app.get("/files")
def list_files():
    return jsonify(retrieve_all_files())

@app.get("/files/<extension>")
def list_files_by_extension(extension):
    return ""

@app.get("/download/<file_name>")
def download(file_name):
    return ""