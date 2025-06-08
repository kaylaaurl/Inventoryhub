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

@query.field("getNotificationById")
def resolve_get_notification_by_id(_, info, id):
    db = SessionLocal()
    notif = db.query(Notification).filter(Notification.id == id).first()
    db.close()
    return notif

@mutation.field("updateNotification")
def resolve_update_notification(_, info, id, message=None, status=None):
    db = SessionLocal()
    notif = db.query(Notification).filter(Notification.id == id).first()
    if not notif:
        db.close()
        return None
    if message:
        notif.message = message
    if status:
        notif.status = status
    db.commit()
    db.refresh(notif)
    db.close()
    return notif

@mutation.field("deleteNotification")
def resolve_delete_notification(_, info, id):
    db = SessionLocal()
    notif = db.query(Notification).filter(Notification.id == id).first()
    if not notif:
        db.close()
        return False
    db.delete(notif)
    db.commit()
    db.close()
    return True

    
    
