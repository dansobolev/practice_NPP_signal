class UserNotFoundException(Exception):
    pass


class UserAlreadyExistsException(Exception):
    pass


class UserWithThisEmailAlreadyExistsException(Exception):
    pass


class UserDoesntHaveEnoughPermissions(Exception):
    pass
