import enum


class UserTypeEnum(enum.Enum):
    LEAD_DESIGNER = 0
    LEAD_TECHNOLOGIST = 1
    SOFTWARE_ENGINEER = 2
    PRODUCTION_MANAGER = 3
    LABOR_RATING_ENGINEER = 4
    FOREMAN = 5
    TECHNICAL_DOCUMENTATION_OFFICER = 6

    __mapping__ = {
        'LEAD_DESIGNER': 'Ведущий конструктор',
        'LEAD_TECHNOLOGIST': 'Ведущий технолог',
        'SOFTWARE_ENGINEER': 'Инженер программист IT-отдела',
        'PRODUCTION_MANAGER': 'Диспетчер производства',
        'LABOR_RATING_ENGINEER': 'Инженер по нормированию трудоемкости',
        'FOREMAN': 'Мастер участка',
        'TECHNICAL_DOCUMENTATION_OFFICER': 'Сотрудник отдела технической документации',
    }

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
