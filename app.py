from flask import Flask, render_template, request, jsonify # type: ignore
from voice_module import listen_to_user
from vision_module import detect_objects_from_camera # type: ignore
from response_module import respond_to_user # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice', methods=['POST'])
def voice():
    command = listen_to_user()
    response = process_command(command)
    return jsonify({'command': command, 'response': response})

@app.route('/camera', methods=['POST'])
def camera():
    result = detect_objects_from_camera()
    respond_to_user(result)
    return jsonify({'response': result})

def process_command(command):
    if "camera" in command or "see" in command:
        result = detect_objects_from_camera()
        respond_to_user(result)
        return result
    elif "hello" in command:
        response = "Hi there! How can I assist you today?"
    elif "exit" in command or "quit" in command:
        response = "Goodbye!"
    else:
        response = "I'm not sure how to respond to that yet."
    respond_to_user(response)
    return response

if __name__ == '__main__':
    app.run(debug=True)
