from app import login_manager
from app.models import User

@login_manager.user_loader
def user_loader(user_id):
    users = User.query.get(int(user_id))
    return users
