from .anytype import any
from .basenode import BaseNode
from ..util.categories import categories

category = categories["conv"]

original_bool = bool


def bool(val):
    match val:
        case False, 0, "0", "false", "False", "FALSE":
            return False
        case True, 1, "1", "true", "True", "TRUE":
            return True
    if val is float or val is int:
        return val != 0
    return original_bool(val)


types = {type.__name__: type for type in [int, float, str, bool]}


class ConvertToType(BaseNode):
    name = "Convert to type"
    display_name = "Convert"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Type": (list(types.keys()),),
            "Input": (any,)
        }}

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Result",)
    FUNCTION = "convert"

    def convert(self, Type, Input):
        return (types[Type](Input),)


types_create = {"list": lambda: [], "dict": lambda: {}}


class CreateEmpty(BaseNode):
    name = "Create empty object"
    display_name = "➕ Create empty object"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Type": (list(types_create.keys()),)
        }}

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Object",)
    FUNCTION = "create"

    def create(self, Type, **kwargs):
        return (types_create[Type](),)
