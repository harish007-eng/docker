from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome To Python App !"
    print("bugfix fixed")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    print("Login feature implemented!")
    print("Login with SSO enabled")
    print("squash commit1")
    print("sqaush commit2")
    print("squash commit3")
    print("changes")
