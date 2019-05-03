from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_user_by_username(username)
    if user and UserModel.verify_hash(password, user.password):
        return user


def identify(payload):
    user_id = payload['identity']
    return UserModel.find_user_by_id(user_id)
