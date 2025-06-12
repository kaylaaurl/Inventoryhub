from ariadne import QueryType, MutationType
from models import Item
from config import SessionLocal

query = QueryType()
mutation = MutationType()

@query.field("getItems")
def resolve_get_items(_, info):
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

@mutation.field("addItem")
def resolve_add_item(_, info, name, category, quantity, location=None, status="available"):
    db = SessionLocal()
    new_item = Item(
        name=name,
        category=category,
        quantity=quantity,
        location=location,
        status=status
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item

@mutation.field("updateItem")
def resolve_update_item(_, info, id, name=None, category=None, quantity=None, location=None, status=None):
    db = SessionLocal()
    item = db.query(Item).filter_by(id=id).first()
    if not item:
        db.close()
        return None

    if name:
        item.name = name
    if category:
        item.category = category
    if quantity is not None:
        item.quantity = quantity
    if location:
        item.location = location
    if status:
        item.status = status

    db.commit()
    db.refresh(item)
    db.close()
    return item

@mutation.field("deleteItem")
def resolve_delete_item(_, info, id):
    db = SessionLocal()
    item = db.query(Item).filter_by(id=id).first()
    if not item:
        db.close()
        return False

    db.delete(item)
    db.commit()
    db.close()
    return True