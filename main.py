from flask import Flask, send_from_directory, render_template_string
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Text Display App</title>
        <style>
            body {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }
            #text-container {
                text-align: center;
                font-size: 24px;
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                width: 100%;
            }
            #control-panel {
                width: 100%;
                padding: 10px;
                position: absolute;
                bottom: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: #f0f0f0;
                box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
            }
            #button-container, #settings-container {
                display: flex;
                gap: 10px;
                margin-bottom: 10px;
            }
            button {
                font-size: 18px; /* ボタンのフォントサイズを変更 */
                padding: 10px 20px; /* ボタンのサイズを調整 */
            }
            input {
                font-size: 18px;
                padding: 5px;
                width: 60px;
            }
            #load-file-button {
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div id="text-container"></div>
        <div id="control-panel">
            <div id="button-container">
                <button id="start-button">Start</button>
                <button id="stop-button">Stop</button>
            </div>
            <div id="settings-container">
                <label for="interval-input">Display duration: </label>
                <input type="number" id="interval-input" value="3">
                <label for="lines-input">Maximum number of display lines: </label>
                <input type="number" id="lines-input" value="5">
                <label for="font-size-input">Font size: </label>
                <input type="number" id="font-size-input" value="24">
            </div>
            <div>
                <input type="file" id="load-file-button">
            </div>
        </div>
        <script>
            let intervalId = null;
            let index = 0;
            let splitText = [];
            let maxDisplayLines = 5;
            let interval = 3000;
            let fontSize = 24;

            document.addEventListener("DOMContentLoaded", () => {
                document.getElementById('load-file-button').addEventListener('change', loadFile);
                document.getElementById('start-button').addEventListener('click', startDisplay);
                document.getElementById('stop-button').addEventListener('click', stopDisplay);
                document.getElementById('interval-input').addEventListener('change', (e) => {
                    interval = parseInt(e.target.value) * 1000;
                });
                document.getElementById('lines-input').addEventListener('change', (e) => {
                    maxDisplayLines = parseInt(e.target.value);
                });
                document.getElementById('font-size-input').addEventListener('change', (e) => {
                    fontSize = parseInt(e.target.value);
                    document.getElementById('text-container').style.fontSize = fontSize + 'px';
                });
            });

            function loadFile(event) {
                const file = event.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        splitText = e.target.result.split('\\\\');
                        index = 0;
                        document.getElementById('text-container').innerHTML = ''; // テキストコンテナをクリア
                    };
                    reader.readAsText(file);
                }
            }

            function displayNextPart() {
                if (index < splitText.length) {
                    const textContainer = document.getElementById('text-container');
                    const newLine = document.createElement('div');
                    newLine.textContent = splitText[index].trim();
                    newLine.style.fontSize = fontSize + 'px';
                    textContainer.appendChild(newLine);

                    if (textContainer.children.length > maxDisplayLines) {
                        for (let i = 0; i < textContainer.children.length - maxDisplayLines; i++) {
                            textContainer.removeChild(textContainer.firstChild);
                        }
                    }

                    index++;
                } else {
                    stopDisplay();
                }
            }

            function startDisplay() {
                if (intervalId === null) {
                    displayNextPart();
                    intervalId = setInterval(displayNextPart, interval);
                }
            }

            function stopDisplay() {
                if (intervalId !== null) {
                    clearInterval(intervalId);
                    intervalId = null;
                }
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/text.txt')
def text_file():
    return send_from_directory('.', 'text.txt')

def open_browser():
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=False)
