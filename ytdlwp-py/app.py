from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/runcmd', methods=['POST'])
def run_command():
    link = request.form['command']
    showName = request.form['showName']
    print(link)
    command =  f'"C:\\Program Files(x86)\\ytdl\\youtube-dl.exe" -url {link} -o "C:\\ToRename\\TVTorename\\{showName}\\%(title)s.%(ext)s"'
    # for Testing
    # command =  f'echo "-url {link} -o C:\\ToRename\\TVTorename\\{showName}\\%(title)s.%(ext)s"'


    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        return f"Success: <pre>{output}</pre>"
    except Exception as e:
        return f"Failed to execute command: {e}"

if __name__ == '__main__':
    app.run(debug=True)
