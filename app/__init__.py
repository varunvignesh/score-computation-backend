import sqlite3
import os
import logging
from flask import Flask, jsonify
from dotenv import load_dotenv

from app.helpers import localization as message

# Get the .env variables
load_dotenv()

# Create flask app instance
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Instantiate database, same thread is disable as trying to fetch the data from the file created from consumer-rabbitMQ app
connection = sqlite3.connect(os.getenv("DATABASE_NAME"), check_same_thread=False)
cursor = connection.cursor()

# health check api
@app.route('/')
def hello_world():
    """
    Add health check route
    """
    return jsonify({
        'status': message.SUCCESS_STATUS,
        "message": message.HEALTH_CHECK_SUCCESS
    })

# Mount the api
from app.api.account import route

# Teardown database connection on app context teardown
# @app.teardown_appcontext
# def close_database_connection(exception=None):
#     if connection is not None:
#         connection.close()