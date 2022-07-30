from flask import Flask,request,make_response,jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import uuid
import datetime

app = Flask(__name__) 
bcrypt = Bcrypt(app)
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_DB']="user_db"
app.config['MYSQL_CURSORCLASS']="DictCursor"

mysql = MySQL(app)
@app.route('/register',methods=['POST'])
def register():
    user_data = request.get_json()
    user_name = user_data['name']
    user_email = user_data['email']
    user_birthday = user_data['birthday']
    user_birthday=datetime.datetime.strptime(user_birthday,'%d/%m/%Y').date()
    user_password = user_data['password']

    cur = mysql.connection.cursor()
    count = cur.execute("select * from user_table where email=%s",[user_email])
    if count ==1:
       return "User is already registered",400
    
    user_id = uuid.uuid4().hex[:16]
    user_hashpassword = bcrypt.generate_password_hash(user_password)
    cur.execute("INSERT INTO user_table(id,name,email,birth,pass) values(%s,%s,%s,%s,%s)",
    (user_id,user_name,user_email,user_birthday,user_hashpassword))
    mysql.connection.commit()
    cur.close()
    return "Registration Successful",201

@app.route('/current_users',methods=['GET'])
def get_user():
    cur = mysql.connection.cursor()
    count = cur.execute("select id,name,email,birth from user_table")
    if count == 0:
       return "No User Found",404
    Userinfo = cur.fetchall()
    cur.close()
    return make_response(jsonify({"Users":Userinfo}))

@app.route('/update_user',methods=['PUT'])
def update_user():
    user_data=request.get_json()
    user_id = user_data['id']
    user_name = user_data['name']
    user_email = user_data['email']
    user_birthday = user_data['birth']
    user_birthday=datetime.datetime.strptime(user_birthday,'%d/%m/%Y').date()
    cur = mysql.connection.cursor()
    count = cur.execute("select id from user_table where id=%s",[user_id])
    if count==1:
        cur.execute("UPDATE user_table set name=%s,email=%s,birth=%s where id=%s",(user_name,user_email,user_birthday,[user_id]))
        mysql.connection.commit()
        cur.close()
        return "User updated successfully",204
    return "User Not Found",404

@app.route('/delete_user/<id>',methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    count = cur.execute("select id from user_table where id=%s",[id])
    if count==1:
       cur.execute("DELETE from user_table where id=%s",[id])
       mysql.connection.commit()
       cur.close()
       return "User Deleted",204
    return "User Not Found",404

# @app.route('/user',methods=['GET','PUT'])
# def user():
#     id = request.args.get('id')
#     if request.method=='GET':
#        for user in Users:
#            if user.id == id:
#              public_user_info = {"id":user.id,"name":user.name,"email":user.email,"birthday":user.birthday}
        
#            return make_response(jsonify(public_user_info))
#     if request.method== 'PUT':
#         user_data=request.get_json()
#         user_name = user_data['name']
#         user_email = user_data['email']
#         user_birthday = user_data['birthday']
#         for user in Users:
#            if user.id == id:
#               user.update(user_name,user_email,user_birthday)
#               Userinfo.clear()
#               return "User updated successfully",204
#     return "User Not Found",404
          

       




if __name__ == '__main__':
    app.run()


