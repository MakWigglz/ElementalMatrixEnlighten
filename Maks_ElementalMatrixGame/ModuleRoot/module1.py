from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_choice', methods=['POST'])
def set_choice():
    data = request.get_json()
    choice = data.get('choice')
    # Process the choice as needed
    print(f"User choice received: {choice}")
    return jsonify({'status': 'success', 'choice': choice})

if __name__ == '__main__':
    app.run(debug=True)