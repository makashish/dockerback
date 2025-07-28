from flask import Flask, request, jsonify, render_template, send_file, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from utils import process_file
import os
from datetime import datetime
from utils import process_file


app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Folders
UPLOAD_FOLDER = os.path.join(app.static_folder, 'images')
OUTPUT_FOLDER = os.path.join(app.static_folder, 'output')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ✅ API Endpoint for React app
@app.route('/api/convert', methods=['POST'])
def api_convert():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    uploaded_file = request.files['file']
    lang = request.form.get('lang', 'eng')

    if uploaded_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(uploaded_file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(filepath)

    docx_path = process_file(filepath, lang, OUTPUT_FOLDER)

    relative_url = os.path.relpath(docx_path, app.static_folder)
    docx_url = f"/static/{relative_url.replace(os.path.sep, '/')}"
    return jsonify({"docx_url": docx_url})

# 🌐 HTML Form page (optional)
@app.route('/convert', methods=['GET', 'POST'])
def form_convert():
    if request.method == 'POST':
        lang = request.form.get('lang', 'eng')
        uploaded_file = request.files.get('file')

        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(filepath)

            docx_path = process_file(filepath, lang, OUTPUT_FOLDER)
            return send_file(docx_path, as_attachment=True)

    return render_template('index.html')

# Serve uploaded/output files
@app.route('/static/output/<path:filename>')
def serve_static(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)