users = []  # list for storing our users


class UserModel(object):
  """Class user models."""

  def __init__(self):
    self.db = users

  def add_user(self, username, email, password, confirmPassword):
    """ Method for saving user to the dictionary """
    payload = {
        "userId": len(self.db) + 1,  # generates user id by starting 1
        "username": username,
        "email": email,
        "password": password,
        "confirmPassword": confirmPassword

    }
    self.db.append(payload)
