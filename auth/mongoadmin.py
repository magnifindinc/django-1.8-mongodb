from mongo_admin.sites import MongoAdmin

from .models import User

User.mongoadmin = MongoAdmin()