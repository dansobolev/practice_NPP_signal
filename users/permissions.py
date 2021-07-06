from .exceptions import UserDoesntHaveEnoughPermissions


def project_permissions_required(permissions: list):
    """
    Декоратор, который проверяет, есть ли у пользователя какие-либо из указанных разрешений.
    """
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            current_user = kwargs['request'].user
            for perm in permissions:
                if current_user.has_perm(perm):
                    result = function(*args, **kwargs)
                    return result
                else:
                    raise UserDoesntHaveEnoughPermissions("You don't have enough permissions.")
        return wrapper
    return real_decorator
