# Credits: https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/3f2c021e50be2fed3c9d1552ee8dcaae06ad1fe5/py/repeater.py
# Hack: string type that is always equal in not equal comparisons
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any = AnyType("*")