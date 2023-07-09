from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    print(f"New user registered - Username: {username}, Password: {password}")
    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
