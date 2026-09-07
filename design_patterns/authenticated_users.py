class IAuthenticator:
  def authenticate(self, username: str, password: str) -> bool:
    pass

class Authenticator(IAuthenticator):
  def authenticate(self, username: str, password: str) -> bool:
    pass

class GoogleAuthenticator(IAuthenticator):
  def authenticate(self, username: str, password: str) -> bool:
    pass

class IUserRepository:
  def saveAuthenticatedUser(self, username: str) -> None:
    pass

class UserRepository(IUserRepository):
  def saveAuthenticatedUser(self, username: str) -> None:
    pass

class AuthController:
  def __init__(self, authenticator: IAuthenticator, userRepository: IUserRepository):
    self.authenticator = authenticator
    self.userRepository = userRepository

  def login(self, username: str, password: str) -> bool:
    if self.authenticator.authenticate(username, password):
      self.userRepository.saveAuthenticatedUser(username);
      return True
    else:
      return False

authenticator = Authenticator()
userRepository = UserRepository()
authController = AuthController(authenticator, userRepository)