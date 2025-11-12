from fastapi import HTTPException, Request
import jwt
import uuid
from datetime import datetime, timedelta
from config import SECRET_KEY, ALGORITHM

users_db = {"admin": "admin", "user": "user"}

def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"sub": username, "exp": expire, "jti": str(uuid.uuid4())}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str):
    payload = verify_token(token)
    return payload.get("sub")
