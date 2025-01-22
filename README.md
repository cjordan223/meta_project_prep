
# Meta Interview Prep Dashboard

## Overview

This project is a simple web application built using Flask (Python) for the backend and Vue.js for the frontend. It allows users to submit SQL queries, practice Meta interview questions, and track their progress.

## Project Structure

```
meta-interview-prep/
│-- backend/
│   ├── app.py                # Flask app
│   ├── db_setup.py            # Database setup
│   ├── models.py              # SQLAlchemy models
│   ├── routes.py              # API routes
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables
│
│-- frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── QueryForm.vue   # SQL query form component
│   │   │   ├── Results.vue     # Results display component
│   │   ├── App.vue             # Main Vue component
│   │   ├── main.js             # Entry point
│   ├── package.json            # Frontend dependencies
│   ├── vite.config.js           # Vite config for fast development
│
│-- docker-compose.yml          # Container setup
│-- README.md                   # Documentation

```

## Setup Instructions

### Prerequisites

-   Install Python (>=3.8)
-   Install Node.js (>=16.x)
-   Install MySQL and MySQL Workbench

### Backend Setup

1.  Navigate to the backend folder:
    
    ```bash
    cd backend
    
    ```
    
2.  Create a virtual environment and activate it:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    
    ```
    
3.  Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4.  Create a `.env` file and add the database connection string:
    
    ```plaintext
    DATABASE_URL=mysql+pymysql://root:password@localhost/meta_prep
    
    ```
    
5.  Run the Flask app:
    
    ```bash
    python app.py
    
    ```
    

### Frontend Setup

1.  Navigate to the frontend folder:
    
    ```bash
    cd frontend
    
    ```
    
2.  Install dependencies:
    
    ```bash
    npm install
    
    ```
    
3.  Start the development server:
    
    ```bash
    npm run dev
    
    ```
    
4.  Open the application in your browser:
    
    ```
    http://localhost:5173
    
    ```
    

## MySQL Database Setup

1.  Open **MySQL Workbench** and connect to your MySQL server.
2.  Create a new database:
    
    ```sql
    CREATE DATABASE meta_prep;
    
    ```
    
3.  Use the new database:
    
    ```sql
    USE meta_prep;
    
    ```
    
4.  Create a sample table for storing SQL questions:
    
    ```sql
    CREATE TABLE sql_questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        correct_query TEXT NOT NULL
    );
    
    ```
    
5.  Insert sample data:
    
    ```sql
    INSERT INTO sql_questions (question, correct_query) VALUES
    ('Find the number of posts per user in 2024', 'SELECT user_id, COUNT(*) FROM posts WHERE YEAR(post_date) = 2024 GROUP BY user_id;');
    
    ```
    
6.  Verify the data:
    
    ```sql
    SELECT * FROM sql_questions;
    
    ```
    

## API Endpoints

Method

Endpoint

Description

POST

/execute

Runs the submitted SQL query

Example request to `/execute`:

```json
{
  "query": "SELECT * FROM sql_questions;"
}

```

### Deployment (Optional)

1.  Build the frontend:
    
    ```bash
    npm run build
    
    ```
    
2.  Deploy the Flask backend with Gunicorn:
    
    ```bash
    gunicorn -w 4 app:app
    
    ```
    

## Future Enhancements

-   User authentication
-   Progress tracking
-   Visual analytics with charting
-   Deployment to AWS/GCP

----------

 
