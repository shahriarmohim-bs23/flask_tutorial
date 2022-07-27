class User_registration:
      def __init__(self,id,name,email,birthday,hashpassword) -> None:
          self.id = id
          self.name = name
          self.email = email
          self.birthday = birthday
          self.haspassword = hashpassword
      def update(self,name,email,birthday):
          self.name = name
          self.email = email
          self.birthday = birthday
          

      def __str__(self):
          return f":{self.id},{self.name},{self.email},{self.birthday},{self.haspassword}"
      def __repr__(self):
        return str(self)



            