from database import SessionLocal
from model import Post

db = SessionLocal()

posts = [
    Post(title="Advanced SQL", content="Learning SQL", user_id=1),
    Post(title="simple gen", content="Building APIs", user_id=2),
    Post(title="pyython code", content="doing simple logics", user_id=3),
    Post(title="pyython code", content="doing simple logics", user_id=4),
    Post(title="pyython code", content="doing simple logics", user_id=5)
]

for post in posts:
    existing_post = db.query(Post).filter(
        Post.title == post.title,
        Post.user_id == post.user_id
    ).first()

    if existing_post:
        print(f"Post '{post.title}' already exists for User {post.user_id}")
    else:
        db.add(post)
        print(f"Post '{post.title}' added for User {post.user_id}")

db.commit()
print("Process Completed!")