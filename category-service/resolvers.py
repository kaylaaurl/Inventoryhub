from ariadne import QueryType, MutationType
from models import Category, SessionLocal
from sqlalchemy.exc import IntegrityError

query = QueryType()
mutation = MutationType()

@query.field("getCategories")
def resolve_get_categories(_, info):
    db = SessionLocal()
    categories = db.query(Category).all()
    db.close()
    return categories

@mutation.field("addCategory")
def resolve_add_category(_, info, name, description=None):
    db = SessionLocal()
    new_category = Category(name=name, description=description)
    db.add(new_category)
    try:
        db.commit()
        db.refresh(new_category)
        return new_category
    except IntegrityError:
        db.rollback()
        return None
    finally:
        db.close()