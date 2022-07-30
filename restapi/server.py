from flask import Flask,request,make_response,jsonify
from user import User_registration
from werkzeug.security import generate_password_hash
import uuid

app = Flask(__name__)
Users = []
Userinfo = []
@app.route('/register',methods=['POST'])
def register():
    user_data = request.get_json()
    user_name = user_data['name']
    user_email = user_data['email']
    user_birthday = user_data['birthday']
    user_password = user_data['password']

    for user in Users:
        if user.email == user_email:
           return "User is already registered",400
    user_id = uuid.uuid4().hex[:16]
    print(type(uuid.uuid4().hex[:16]))
    user_hashpassword = generate_password_hash(user_password)
    user = User_registration(user_id,user_name,user_email,user_birthday,user_hashpassword)
    Users.append(user)
    print(Users)

    return "Registration Successful",201

@app.route('/current_users',methods=['GET'])
def get_user():
    for user in Users:
        public_user_info = {"id":user.id,"name":user.name,"email":user.email,"birthday":user.birthday}
        Userinfo.append(public_user_info)
    return make_response(jsonify({"Users":Userinfo}))

@app.route('/update_user',methods=['PUT'])
def update_user():
    user_data=request.get_json()
    user_id = user_data['id']
    user_name = user_data['name']
    user_email = user_data['email']
    user_birthday = user_data['birthday']
    for user in Users:
        if user.id == user_id:
           user.update(user_name,user_email,user_birthday)
           Userinfo.clear()
           return "User updated successfully",204
    return "User Not Found",404

@app.route('/delete_user/<id>',methods=['DELETE'])
def delete_user(id):
    for user in Users:
        if user.id == id:
           Users.remove(user)
           Userinfo.clear()
           return "User Deleted",204
    return "User Not Found",404

@app.route('/user',methods=['GET','PUT'])
def user():
    id = request.args.get('id')
    if request.method=='GET':
       for user in Users:
           if user.id == id:
             public_user_info = {"id":user.id,"name":user.name,"email":user.email,"birthday":user.birthday}
        
           return make_response(jsonify(public_user_info))
    if request.method== 'PUT':
        user_data=request.get_json()
        user_name = user_data['name']
        user_email = user_data['email']
        user_birthday = user_data['birthday']
        for user in Users:
           if user.id == id:
              user.update(user_name,user_email,user_birthday)
              Userinfo.clear()
              return "User updated successfully",204
    return "User Not Found",404
          

       




if __name__ == '__main__':
    app.run()


