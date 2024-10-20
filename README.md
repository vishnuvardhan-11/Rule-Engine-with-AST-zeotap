

---

# Rule Engine with AST

This project implements a rule engine using **Abstract Syntax Trees (AST)** to dynamically create, evaluate, and combine rules based on user attributes (age, department, salary, etc.). The project uses a **Flask** backend, **SQLite** database, and a **frontend** with HTML, CSS, and JavaScript.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Frontend Functionality](#frontend-functionality)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

## Features

- Create rules using AST.
- Store rules and user attributes in an SQLite database.
- Evaluate rules dynamically based on user inputs.
- Frontend allows users to input data and evaluate eligibility based on stored rules.

## Project Structure

```
rule-engine-ast/
│
├── backend/
│   ├── app.py                  # Main Flask backend file
│   ├── ast_engine.py            # AST logic (create_rule, combine_rules, evaluate_rule)
│   ├── models.py                # Database models (Rule, UserAttributes)
│   ├── db.py                    # Database connection setup
│   └── test.py                  # Unit test cases for rules
│
├── frontend/
│   ├── index.html               # Simple HTML UI
│   ├── app.js                   # JavaScript code for making API requests
│   └── style.css                # Styles for the UI
│
├── venv/                        # Virtual environment for Python
└── README.md                    # This README file
```

## Technologies Used

- **Backend**: Flask, SQLite, Python
- **Frontend**: HTML, CSS, JavaScript (AJAX)
- **Database**: SQLite
- **Testing**: Unit tests with Python

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- **Python 3.x**
- **pip** (Python package manager)
- **Virtual environment** setup (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/rule-engine-ast.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rule-engine-ast
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Initialize the database:

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   ```

7. Run the application:

   ```bash
   flask run
   ```

   The app will be accessible at `http://127.0.0.1:5000`.

### Frontend

Open the `frontend/index.html` file in your browser to interact with the UI.

## API Endpoints

### 1. `POST /api/rules`
- **Description**: Adds a new rule to the database.
- **Request Body**:
  ```json
  {
    "rule_name": "Example Rule",
    "rule_expression": "age > 30 and department == 'Engineering'"
  }
  ```

### 2. `POST /api/evaluate`
- **Description**: Evaluates a rule based on user input.
- **Request Body**:
  ```json
  {
    "age": 35,
    "department": "Engineering",
    "salary": 50000,
    "experience": 5
  }
  ```

### 3. `GET /api/rules`
- **Description**: Fetches all the rules from the database.

## Frontend Functionality

The frontend allows users to:
- Input personal details like age, department, salary, and experience.
- Select a rule to evaluate their eligibility.
- Submit data via an HTML form, which sends an AJAX request to the backend for evaluation.

## Database Schema

The SQLite database contains two main tables:

### 1. `rules`
- **Columns**:
  - `id`: Primary Key
  - `name`: Name of the rule
  - `expression`: The rule's condition in AST format

### 2. `user_attributes`
- **Columns**:
  - `id`: Primary Key
  - `age`: User's age
  - `department`: User's department
  - `salary`: User's salary
  - `experience`: User's experience

## Testing

Unit tests are provided in `backend/test.py`. To run the tests:

```bash
python -m unittest backend/test.py
```

## Future Enhancements

- Add more complex rule conditions.
- Support for multiple databases (MySQL, PostgreSQL).
- Implement user authentication.
- Create a dashboard to display rule evaluation statistics.

---
