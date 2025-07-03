from app.database import SessionLocal
from app.models import User
from app.auth import get_password_hash

db = SessionLocal()
ops = User(email="ops@example.com", hashed_password=get_password_hash("password"), is_ops=True, is_verified=True)
db.add(ops)
db.commit()
