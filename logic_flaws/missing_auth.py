from flask import Flask, request
app = Flask(__name__)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.json.get('user_id')
    database.delete(user_id)