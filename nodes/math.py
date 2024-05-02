from .basenode import BaseNode
from ..util.categories import categories

category = categories["math"]

actions = ["+", "-", "*", "/", "^ (**)", "%"]


def operation(a, b, action, c_type=float):
    match action:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "^ (**)":
            return a ** b
        case "%":
            return a % b
    return c_type(0)


class IntExpression(BaseNode):
    name = "Int Expression"
    display_name = "❓ Math expression (Int)"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Action": (actions,),
                "A": ("INT", {}),
                "B": ("INT", {})
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "expr"
    CATEGORY = category

    def expr(self, Action, A, B, **kwargs):
        return (operation(A, B, Action, int),)


class FloatExpression(BaseNode):
    name = "Float Expression"
    display_name = "❓ Math expression (Float)"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Action": (actions,),
                "A": ("FLOAT", {}),
                "B": ("FLOAT", {})
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "expr"
    CATEGORY = category

    def expr(self, Action, A, B, **kwargs):
        return (operation(A, B, Action, float),)
