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

@mutation.field("updateCategory")
def resolve_update_category(_, info, id, name=None, description=None):
    db = SessionLocal()
    category = db.query(Category).filter_by(id=id).first()
    if not category:
        db.close()
        return None
    if name is not None:
        category.name = name
    if description is not None:
        category.description = description
    try:
        db.commit()
        db.refresh(category)
        return category
    except IntegrityError:
        db.rollback()
        return None
    finally:
        db.close()

@mutation.field("deleteCategory")
def resolve_delete_category(_, info, id):
    db = SessionLocal()
    category = db.query(Category).filter_by(id=id).first()
    if not category:
        db.close()
        return False
    db.delete(category)
    db.commit()
    db.close()
    return True