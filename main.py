from flask import Flask
from flask_cors import CORS
import blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(blueprint.auth, url_prefix='/api/auth')
app.register_blueprint(blueprint.info, url_prefix='/api/info')

app.run(host="0.0.0.0", port=8081, debug=True)
