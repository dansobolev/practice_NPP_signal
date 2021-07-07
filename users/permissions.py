from django.contrib.auth.models import User

from .exceptions import UserDoesntHaveEnoughPermissions
from .enums import UserTypeEnum


class ProjectPermissions:
    PERM_PROJECT_READ = 'PERM_PROJECT_READ'
    PERM_PROJECT_UPDATE = 'PERM_PROJECT_UPDATE'


def project_permissions_required(permissions: list):
    """
    Декоратор, который проверяет, есть ли у пользователя какие-либо из указанных разрешений.
    """
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            current_user = kwargs['request'].user
            current_user_permissions = get_current_user_permissions(current_user)
            if any(require_perm.startswith(user_perm) for user_perm in
                   current_user_permissions for require_perm in permissions):
                result = function(*args, **kwargs)
            else:
                raise UserDoesntHaveEnoughPermissions("You don't have enough permissions.")
            return result
        return wrapper
    return real_decorator


def get_current_user_permissions(user: User):
    permissions = []

    if user.user_type in [UserTypeEnum.LEAD_DESIGNER.value,
                          UserTypeEnum.LEAD_TECHNOLOGIST.value,
                          UserTypeEnum.SOFTWARE_ENGINEER.value]:
        permissions.extend([ProjectPermissions.PERM_PROJECT_READ,
                            ProjectPermissions.PERM_PROJECT_UPDATE])

    else:
        permissions.extend([ProjectPermissions.PERM_PROJECT_READ])

    return permissions
