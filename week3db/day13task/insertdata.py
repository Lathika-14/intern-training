from database import SessionLocal
from model import User

db = SessionLocal()

users = [
    {"id":1,"name": "lathi", "email": "lathi_new@gmail.com"},
    {"id":2,"name": "srii", "email": "srii_new@gmail.com"},
    {"id":3,"name": "joyy", "email": "joyy_new@gmail.com"},
    {"id":4,"name": "sundarr", "email": "sundarr_new@gmail.com"},
    {"id":5,"name": "siva", "email": "siva_new@gmail.com"}
]

new_users = []

for user_data in users:
    existing_user = db.query(User).filter(
        User.email == user_data["email"]
    ).first()

    if existing_user:
        print(f"User with email {user_data['email']} already exists")
    else:
        new_users.append(
            User(
                name=user_data["name"],
                email=user_data["email"]
            )
        )

if new_users:
    db.add_all(new_users)
    db.commit()
    print("New users added successfully!")
else:
    print("user already exists.")