from database import SessionLocal
from model import User

db = SessionLocal()
user = db.query(User).filter(User.id == 14).first()
print("User:", user.name)
for post in user.posts:
    print("Post:", post.title)
    
    
