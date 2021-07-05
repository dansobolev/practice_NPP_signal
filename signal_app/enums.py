import enum


class TypeEnum(enum.Enum):
    ASSEMBLY = 0
    DETAIL = 1
    STANDARD_PRODUCTS = 2
    OTHER_PRODUCTS = 3

    __mapping__ = {
        'ASSEMBLY': 'Cборка',
        'DETAIL': 'Деталь',
        'STANDARD_PRODUCTS': 'Стандартные изделия',
        'OTHER_PRODUCTS': 'Прочие изделия',
    }

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
