from django.http import JsonResponse

from .exceptions import UserDoesntHaveEnoughPermissions
from .enums import UserTypeEnum
from .models import UserProfile


class ProjectPermissions:
    PERM_PROJECT_READ = 'PERM_PROJECT_READ'
    PERM_PROJECT_UPDATE = 'PERM_PROJECT_UPDATE'


def project_permissions_required(permissions: list):
    """
    Декоратор, который проверяет, есть ли у пользователя какие-либо из указанных разрешений.
    """
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            current_user = args[0].user
            get_user_profile = UserProfile.objects.get(id=current_user.id)
            current_user_permissions = get_current_user_permissions(get_user_profile)
            if any(require_perm.startswith(user_perm) for user_perm in
                   current_user_permissions for require_perm in permissions):
                result = function(*args, **kwargs)
            else:
                return JsonResponse({"message": "У вас недостаточно прав для этого действия."})
            return result
        return wrapper
    return real_decorator


def get_current_user_permissions(user: UserProfile):
    permissions = []

    if user.user_type in [UserTypeEnum.LEAD_DESIGNER.value,
                          UserTypeEnum.LEAD_TECHNOLOGIST.value,
                          UserTypeEnum.SOFTWARE_ENGINEER.value]:
        permissions.extend([ProjectPermissions.PERM_PROJECT_READ,
                            ProjectPermissions.PERM_PROJECT_UPDATE])

    else:
        permissions.extend([ProjectPermissions.PERM_PROJECT_READ])

    return permissions
