# First REST API Project

This project demonstrates building REST APIs using Python, Flask, Docker, Flask-Smorest, and Flask-SQLAlchemy.

## Features

- RESTful API endpoints with Flask
- Data modeling and persistence using SQLAlchemy
- API documentation and validation with Flask-Smorest
- Containerization with Docker

## Getting Started

1. **Clone the repository**
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application**
    ```bash
    flask run
    ```
4. **(Optional) Run with Docker**
    ```bash
    docker build -t flask-rest-api .
    docker run -p 5000:5000 flask-rest-api
    ```

## Folder Structure

- `app/` - Source code
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration

## Technologies Used

- Python
- Flask
- Flask-Smorest
- Flask-SQLAlchemy
- Docker

## License

This project is licensed under the MIT License.