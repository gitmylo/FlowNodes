from .basenode import BaseNode
from ..util.categories import categories
from .anytype import any


category = categories["cond"]


class IfCond(BaseNode):
    name = "If condition"
    display_name = "🔀 If condition"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Bool": ("BOOLEAN",),
            "Value": (any,)
        }}

    CATEGORY = category
    RETURN_TYPES = (any, any)
    RETURN_NAMES = ("True", "False")
    FUNCTION = "node"

    def node(self, Bool: bool, Value, **kwargs):
        return (Value, None) if Bool else (None, Value)


class BoolSwitchExpr(BaseNode):
    name = "Int Switch expression"
    display_name = "🔀 Int Switch expression"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": ("BOOLEAN",)
        }, "optional": {
            "True": (any,),
            "False": (any,),
        }}

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Result",)
    FUNCTION = "node"

    def node(self, Value, **kwargs):
        return kwargs["True"] if Value else kwargs["False"]


class SwitchExpr(BaseNode):
    name = "Int Switch expression"
    display_name = "🔀 Int Switch expression"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": ("INTEGER", {"default": 0, "min": 0, "max": 9, "step": 1})
        }, "optional": {
            # "0": (any,),
            # "1": (any,),
            # "2": (any,),
            # "3": (any,),
            # "4": (any,),
            # "5": (any,),
            # "6": (any,),
            # "7": (any,),
            # "8": (any,),
            # "9": (any,),
            str(v): (any,) for v in range(10)
        }}

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Result",)
    FUNCTION = "node"

    def node(self, Value, **kwargs):
        return kwargs[str(Value)]
