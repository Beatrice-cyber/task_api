# Task API (FastAPI)

A simple RESTful backend service built with FastAPI for managing tasks.

## Features

* Create tasks (POST /tasks)
* Retrieve tasks (GET /tasks)
* Delete tasks (DELETE /tasks/{task_id})

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:
http://127.0.0.1:8000/docs

## Notes

* Uses SQLite for persistent storage
* API automatically documented with Swagger UI

I built a REST API using FastAPI where requests are validated using Pydantic models, and data is stored in a SQLite database using SQLAlchemy.
I defined a SQLAlchemy model representing the tasks table, which maps Python objects to database rows.
The Pydantic model is used for request validation and parsing, while the SQLAlchemy model defines how data is stored in the database. 
We convert between them because they serve different purposes.
