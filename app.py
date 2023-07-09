from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    if username and password and email:
        # Register logic goes here
        return 'User registration successful!'
    else:
        return 'Missing required fields', 400

if __name__ == '__main__':
    app.run()