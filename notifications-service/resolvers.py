from ariadne import QueryType, MutationType
from models import Notification, SessionLocal

query = QueryType()
mutation = MutationType()

@query.field("getNotifications")
def resolve_get_notifications(_, info):
    db = SessionLocal()
    notifications = db.query(Notification).all()
    db.close()
    return notifications

@mutation.field("addNotification")
def resolve_add_notification(_, info, user_id, item_id, message, status="pending"):
    db = SessionLocal()
    notif = Notification(
        user_id=user_id,
        item_id=item_id,
        message=message,
        status=status
    )
    db.add(notif)
    db.commit()
    db.refresh(notif)
    db.close()
    return notif
