from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
      connection = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD")
      )

      return connection

@app.route("/")
def hello_world():
      return "<p>Hello World</p>"

@app.route("/db-test")
def db_test():
      connection = get_db_connection()
      connection.close()

      return "<p>Database connection successful!</p>"

if __name__ == "__main__":
    app.run(debug=True)