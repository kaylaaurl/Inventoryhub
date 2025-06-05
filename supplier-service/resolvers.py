from ariadne import QueryType, MutationType
from models import Supplier, SessionLocal

query = QueryType()
mutation = MutationType()

@query.field("getSuppliers")
def resolve_get_suppliers(_, info):
    db = SessionLocal()
    suppliers = db.query(Supplier).all()
    db.close()
    return suppliers

@mutation.field("addSupplier")
def resolve_add_supplier(_, info, name, contact_person=None, phone=None, email=None, address=None):
    db = SessionLocal()
    new_supplier = Supplier(
        name=name,
        contact_person=contact_person,
        phone=phone,
        email=email,
        address=address
    )
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    db.close()
    return new_supplier
