from flask import Flask, request, jsonify, render_template, send_file, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from utils import process_file
import os
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

# Enable CORS only for /api/* endpoints, from localhost:5173
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# Directories
UPLOAD_FOLDER = os.path.join(app.static_folder, 'images')
OUTPUT_FOLDER = os.path.join(app.static_folder, 'output')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ✅ API route to upload and convert file
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

    try:
        docx_path = process_file(filepath, lang, OUTPUT_FOLDER)
        relative_url = os.path.relpath(docx_path, app.static_folder)
        docx_url = f"/static/{relative_url.replace(os.path.sep, '/')}"
        return jsonify({"docx_url": docx_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Separate upload-only API endpoint (optional/flexible)
@app.route('/api/upload', methods=['POST'])
def api_upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(uploaded_file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(filepath)

    # 🛠️ You can call your conversion logic here
    # Let's assume the output docx is saved as 'output.docx'
    output_filename = "image.docx"  # or use logic to generate filename
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    # 🔁 If using your process_file() function, do something like:
    # output_path = process_file(filepath, lang, OUTPUT_FOLDER)

    # ✅ Return the complete URL to frontend
    backend_url = request.host_url.rstrip('/')  # e.g., https://dockerback-xxxx.onrender.com
    doc_url = f"{backend_url}/output/{output_filename}"

    return jsonify({
        "message": "Uploaded and processed successfully",
        "docUrl": doc_url
    })

# 🔓 Serve the output files
@app.route('/output/<path:filename>')
def download_file(filename):

# ✅ Optional HTML form route for testing via browser
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

# ✅ Serve output files for download
@app.route('/static/output/<path:filename>')
def serve_output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

# ✅ Homepage
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Run server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)