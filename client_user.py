from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, auth, database
from fastapi.responses import FileResponse

router = APIRouter(prefix="/client")

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
    hashed_pw = auth.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_pw, is_ops=False)
    db.add(new_user)
    db.commit()
    token = auth.create_access_token({"sub": str(new_user.id), "role": "client"})
    return {"verification_url": f"/client/verify-email?token={token}"}

@router.get("/verify-email")
def verify_email(token: str, db: Session = Depends(database.SessionLocal)):
    payload = auth.decode_token(token)
    user = db.query(models.User).filter(models.User.id == int(payload["sub"])).first()
    if user:
        user.is_verified = True
        db.commit()
        return {"message": "Email verified"}
    raise HTTPException(status_code=400, detail="Invalid token")

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.SessionLocal)):
    db_user = db.query(models.User).filter(models.User.email == user.email, models.User.is_ops == False).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    token = auth.create_access_token({"sub": str(db_user.id), "role": "client"})
    return {"access_token": token}

@router.get("/files", response_model=List[schemas.FileOut])
def list_files(db: Session = Depends(database.SessionLocal)):
    return db.query(models.File).all()

@router.get("/download/{file_id}")
def download_file(file_id: int, token: str, db: Session = Depends(database.SessionLocal)):
    payload = auth.decode_token(token)
    if payload.get("role") != "client":
        raise HTTPException(status_code=403, detail="Forbidden")
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file.filepath, filename=file.filename)