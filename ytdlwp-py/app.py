from flask import Flask, request, render_template, jsonify as flask_jsonify
import subprocess
import os
# import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runcmd', methods=['POST'])
def run_command():
    link = request.form['command']
    showName = request.form['showName']
    # command =  f'"C:\\Program Files (x86)\\ytdl\\youtube-dl.exe" -url {link} -o "C:\\ToRename\\TVTorename\\{showName}\\%(title)s.%(ext)s"'
    # for Testing
    command =  f'timeout 3 && echo "-url {link} -o C:\\ToRename\\TVTorename\\{showName}\\%(title)s.%(ext)s"'

    successMessg = f"{showName}  was downloaded to ToRename\{showName}\."

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        result2 = os.popen(command)
        return flask_jsonify({'success': True, 'output': successMessg})
        # return f"Success: <br> {command}<pre>{output}</pre>"
    except Exception as e:
        return flask_jsonify({'success': False, 'error': str(e)})
        # return f"Failed to execute command: {e}"

if __name__ == '__main__':
    app.run(debug=True)
