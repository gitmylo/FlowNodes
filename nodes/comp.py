from .basenode import BaseNode
from ..util.categories import categories

category = categories["comp"]

actions = ["==", "!=", "<", ">", "<=", ">="]


def operation(a, b, action):
    match action:
        case "==":
            return a == b
        case "!=":
            return a != b
        case "<":
            return a < b
        case ">":
            return a > b
        case "<=":
            return a <= b
        case ">=":
            return a >= b
    return False


class IntCompare(BaseNode):
    name = "Int Compare"
    display_name = "❓ Compare (Int)"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Action": (actions,),
                "A": ("INT", {}),
                "B": ("INT", {})
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "compare"
    CATEGORY = category

    def compare(self, Action, A, B, **kwargs):
        return (operation(A, B, Action),)


class FloatCompare(BaseNode):
    name = "Float Compare"
    display_name = "❓ Compare (Float)"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Action": (actions,),
                "A": ("FLOAT", {}),
                "B": ("FLOAT", {})
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "compare"
    CATEGORY = category

    def compare(self, Action, A, B, **kwargs):
        return (operation(A, B, Action),)
