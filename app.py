from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from utils import process_file
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Setup CORS: allow frontend on Vite dev server
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# 🔧 Set up folders
UPLOAD_FOLDER = os.path.join(app.static_folder, 'images')
OUTPUT_FOLDER = os.path.join(app.static_folder, 'output')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 🌐 For public Render URL
BASE_URL = "https://dockerback-77dc.onrender.com"  # Update for production

@app.route('/api/upload', methods=['POST'])
def upload_and_process():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    lang_code = request.form.get('lang', 'eng')
    lang_name = request.form.get('language_name', 'English')  # optional, default: English

    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(upload_path)

    try:
        # 🔁 Process the image/PDF to DOCX
        docx_path = process_file(upload_path, lang_code, OUTPUT_FOLDER, lang_name)
        docx_filename = os.path.basename(docx_path)
        docx_url = f"{BASE_URL}/output/{docx_filename}"

        return jsonify({
            "message": "Uploaded and converted successfully",
            "docx_url": docx_url
        })
    except Exception as e:
        return jsonify({"error": f"Failed to process file: {str(e)}"}), 500

# ✅ Serve .docx file for download
@app.route('/output/<path:filename>')
def serve_docx(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

# ✅ Root page (if needed)
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)