import  pprint

def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = dir(obj)

    # Получаем методы объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = obj.__mod__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


# Пример использования функции
number_info = introspection_info(42)
pprint.pprint(number_info)

