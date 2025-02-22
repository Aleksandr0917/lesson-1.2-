import  pprint

def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]

    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__mod__


    # Создание словаря с информацией об объекте
    info = {'type': obj_type,
            'attributes': attributes,
            'methods': methods,
            'module': module},
            # 'other_properties': other_properties}

    return info

# Интроспекция числа
number_info = introspection_info(42)
pprint.pprint(number_info)

