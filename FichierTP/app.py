from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://mongo:27017/')
client = MongoClient(mongo_uri)
db = client['mydatabase'] 

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><p>Cette application Flask fonctionne dans un conteneur Docker </p>'

@app.route('/data')
def get_data():
    # Example route to fetch data from MongoDB
    data = db['mycollection'].find()  # Replace 'mycollection' with your collection name
    return '<br>'.join([str(item) for item in data])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)