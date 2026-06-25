from database import SessionLocal
from model import User

db = SessionLocal()
user = db.query(User).filter(User.id==14).first ()
user.name = "pragal"
db.commit()
print("updated successfull")