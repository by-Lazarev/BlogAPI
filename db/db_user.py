from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db import hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, user_id: int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()


def update_user(db: Session, user_id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == user_id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: hash.bcrypt(request.password)
    })
    db.commit()
    return "OK"


def delete_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    db.delete(user)
    db.commit()
    return "OK"