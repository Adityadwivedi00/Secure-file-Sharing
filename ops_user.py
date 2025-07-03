from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from .. import models, schemas, auth, database, utils
import shutil, os

router = APIRouter(prefix="/ops")

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.SessionLocal)):
    db_user = db.query(models.User).filter(models.User.email == user.email, models.User.is_ops == True).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    token = auth.create_access_token({"sub": str(db_user.id), "role": "ops"})
    return {"access_token": token}

@router.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(database.SessionLocal)):
    if not utils.allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File type not allowed")
    path = f"uploads/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    db_file = models.File(filename=file.filename, filepath=path, user_id=1)
    db.add(db_file)
    db.commit()
    return {"message": "File uploaded"}