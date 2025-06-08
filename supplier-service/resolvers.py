from ariadne import QueryType, MutationType
from models import Supplier, SessionLocal

query = QueryType()
mutation = MutationType()

@query.field("getSuppliers")
def resolve_get_suppliers(_, info):
    db = SessionLocal()
    data = db.query(Supplier).all()
    db.close()
    return data

@query.field("getSupplier")
def resolve_get_supplier(_, info, id):
    db = SessionLocal()
    supplier = db.query(Supplier).filter_by(id=id).first()
    db.close()
    return supplier

@mutation.field("addSupplier")
def resolve_add_supplier(_, info, name, contact_person, phone=None, email=None, address=None):
    db = SessionLocal()
    new = Supplier(name=name, contact_person=contact_person, phone=phone, email=email, address=address)
    db.add(new)
    db.commit()
    db.refresh(new)
    db.close()
    return new

@mutation.field("updateSupplier")
def resolve_update_supplier(_, info, id, name=None, contact_person=None, phone=None, email=None, address=None):
    db = SessionLocal()
    s = db.query(Supplier).filter_by(id=id).first()
    if not s:
        db.close()
        return None
    if name: s.name = name
    if contact_person: s.contact_person = contact_person
    if phone: s.phone = phone
    if email: s.email = email
    if address: s.address = address
    db.commit()
    db.refresh(s)
    db.close()
    return s

@mutation.field("deleteSupplier")
def resolve_delete_supplier(_, info, id):
    db = SessionLocal()
    s = db.query(Supplier).filter_by(id=id).first()
    if not s:
        db.close()
        return False
    db.delete(s)
    db.commit()
    db.close()
    return True
