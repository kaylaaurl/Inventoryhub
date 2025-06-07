from models import User, SessionLocal
from ariadne import QueryType, MutationType
from sqlalchemy.exc import IntegrityError

query = QueryType()
mutation = MutationType()

@query.field("getUsers")
def resolve_get_users(_, info):
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

@mutation.field("register")
def resolve_register(_, info, username, password, role):
    db = SessionLocal()
    new_user = User(username=username, password=password, role=role)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        return None
    finally:
        db.close()

@mutation.field("login")
def resolve_login(_, info, username, password):
    db = SessionLocal()
    user = db.query(User).filter_by(username=username, password=password).first()
    db.close()
    if user:
        return f"Login success! Role: {user.role}"
    return "Invalid credentials"

@mutation.field("updateUser")
def resolve_update_user(_, info, id, username=None, password=None, role=None):
    db = SessionLocal()
    user = db.query(User).filter_by(id=id).first()
    if not user:
        db.close()
        return None

    if username:
        user.username = username
    if password:
        user.password = password
    if role:
        user.role = role

    db.commit()
    db.refresh(user)
    db.close()
    return user

@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    db = SessionLocal()
    user = db.query(User).filter_by(id=id).first()
    if not user:
        db.close()
        return False

    db.delete(user)
    db.commit()
    db.close()
    return True
