user_permissions = ["user"]


def check_permission(permission):
    def wrapper_permission(func):
        def wrapped_check():
            if permission not in user_permissions:
                raise ValueError("Недостаточно прав")
            return func()

        return wrapped_check

    return wrapper_permission


@check_permission("user")
def check_value():
    return "значение"


@check_permission("admin")
def do_something():
    return "только админ"


print("старт программы")
check_value()
do_something()
print('конец программы')
