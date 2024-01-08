from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if the 'file' key is in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save the file to /var/www/uploads
        file.save('/var/www/uploads/' + file.filename)

        return jsonify({'message': 'File successfully uploaded'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/files')
def list_files():
    try:
        files = os.listdir('/var/www/uploads')
        return render_template('files.html', files=files)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('/var/www/uploads', filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete_file(filename):
    try:
        file_path = os.path.join('/var/www/uploads', filename)
        os.remove(file_path)
        return jsonify({'message': 'File successfully deleted'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
