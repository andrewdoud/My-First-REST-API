import random
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, world!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def generate_random_id():
    id_length = 6
    rand_id = ""

    for _ in range(id_length//2):
        rand_id = rand_id + chr(random.randint(97, 122))

    for _ in range(id_length//2):
        rand_id = rand_id + chr(random.randint(48, 57))

    return rand_id

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username :
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd["id"] = generate_random_id()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        #resp.status_code = 200 #optionally, you can always set a response code. 
        # 200 is the default code for a normal response
        resp.status_code = 201
        return resp
    elif request.method == 'DELETE':
        userToDelete = request.get_json()
        users['users_list'].remove(userToDelete)
        resp = jsonify(success=True)
        return resp

@app.route('/users/<id>')
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})
    return users
