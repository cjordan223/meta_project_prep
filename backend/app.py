from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///meta_prep.db')
db = SQLAlchemy(app)

class SQLQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    correct_query = db.Column(db.Text, nullable=False)
    
@app.route('/execute', methods=['POST'])
def execute_query():
    try:
        user_query = request.json.get('query')
        result = db.session.execute(user_query).fetchall()
        return jsonify({"success": True, "result": [dict(row) for row in result]})
    except Exception as e:
        return jsonify({"success": True, "error": str(e)}), 400
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)