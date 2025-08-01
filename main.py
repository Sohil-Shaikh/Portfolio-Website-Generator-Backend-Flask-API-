from flask import Flask
from flask_cors import CORS
from app.routes.resume import resume_api
from app.routes.translate import translate_api
from app.routes.currency import currency_api
from app.routes.facebook_agent import fb_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(resume_api)
app.register_blueprint(translate_api)
app.register_blueprint(currency_api)
app.register_blueprint(fb_api)

@app.route('/')
def home():
    return "✅ Flask backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
