from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_user
from auth import oauth2

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# ---[CRUD]---
# CREATE USER
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# READ ALL USERS
@router.get("/", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_current_user)):
    return db_user.get_all_user(db)


# READ ONE USER
@router.get("/{user_id}", response_model=UserDisplay)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_current_user)):
    return db_user.get_user(db, user_id)


# UPDATE USER
@router.post("/{user_id}/update")
def update_user(
        user_id: int, request: UserBase,
        db: Session = Depends(get_db),
        current_user: UserBase = Depends(oauth2.get_current_user)
):
    return db_user.update_user(db, user_id, request)


# DELETE USER
@router.delete("/{user_id}/delete")
def delete_user(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: UserBase = Depends(oauth2.get_current_user)
):
    return db_user.delete_user(db, user_id)
