import jwt
from datetime import datetime,timedelta
jwt_secret_key = "This is secret key"
jwt_algorithm = 'HS256'

def encode(payload):
    #issued time
    payload['iat'] = datetime.utcnow()
    #expired time
    payload['exp'] = datetime.utcnow()+timedelta(minutes=15)
    #token expired
    
    encoded_string = jwt.encode(payload=payload,key=jwt_secret_key,algorithm=jwt_algorithm)
    return encoded_string

def decode(encoded_string):
    decoded_payload = jwt.decode(jwt=encoded_string,key=jwt_secret_key,algorithms=jwt_algorithm)
    return decoded_payload

   

