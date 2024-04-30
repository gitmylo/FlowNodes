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
