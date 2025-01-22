from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_cors import CORS



load_dotenv()


app = Flask(__name__)
CORS(app) #enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#model definition
class SQLQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    correct_query = db.Column(db.Text, nullable=False)
    
# route to fetch all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    questions = SQLQuestion.query.all()
    return jsonify([
        {"id": q.id, "question": q.question, "correct_query": q.correct_query} for q in questions
    ])
    
# route to execute SQL queries
@app.route('/execute', methods=['POST'])
def execute_query():
    try:
        data = request.json
        user_query = data.get('query')
        result = db.session.execute(user_query).fetchall()
        result_list = [dict(row._asdict()) for row in result]
        return jsonify({"success": True, "result": result_list})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True)