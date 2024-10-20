from flask import Flask, request, jsonify
from models import db, Rule
from flask_cors import CORS # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/save-rule', methods=['POST'])
def save_rule():
    data = request.get_json()

    new_rule = Rule(
        department=data['department'],
        age=data['age'],
        rule_name=data['rule_name'],
        salary=data['salary'],
        experience=data['experience']
    )

    db.session.add(new_rule)
    db.session.commit()

    return jsonify({"message": "Rule saved successfully!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
CORS(app)