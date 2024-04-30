from .basenode import BaseNode
from ..util.categories import categories

category = categories["logic"]

actions = ["and", "or", "equal", "not equal"]


def operation(a, b, action):
    match action:
        case "and":
            return a and b
        case "or":
            return a or b
        case "equal":
            return a == b
        case "not equal":
            return a != b
    return False


class LogicNode(BaseNode):
    name = "2 boolean operation"
    display_name = "🆎 2 Boolean operation"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Operation": (actions,),
            "A": ("BOOLEAN",),
            "B": ("BOOLEAN",)
        }}

    CATEGORY = category
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "operation"

    def operation(self, Operation, A: bool, B: bool):
        return (operation(A, B, Operation),)


class NotNode(BaseNode):
    name = "Boolean Not"
    display_name = "❗ Boolean Not"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "In": ("BOOLEAN",)
        }}

    CATEGORY = category
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "operation"

    def operation(self, In):
        return (not In,)
