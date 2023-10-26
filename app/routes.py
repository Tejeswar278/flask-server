from app import app

@app.route('/')
def home():
    print("welcome to home")
    return "welcome to home page"

@app.route('/login')
def login():
    return "welcom to login"

@app.route('/signup')
def signup():
    return "welcome to signup"