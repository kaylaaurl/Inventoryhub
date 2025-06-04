from ariadne import QueryType, MutationType
from models import Item, SessionLocal

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
