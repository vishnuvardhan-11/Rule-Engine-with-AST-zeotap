from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    rule_name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Rule {self.rule_name}>'
