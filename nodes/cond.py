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
        }, "optional": {
            "Flow": ("FLOW",),
        }}

    CATEGORY = category
    RETURN_TYPES = (any, any)
    RETURN_NAMES = ("True", "False")
    FUNCTION = "node"

    def node(self, Bool: bool, Value, **kwargs):
        return (Value, None) if Bool else (None, Value)


class BoolSwitchExpr(BaseNode):
    name = "Boolean Switch expression"
    display_name = "🔀 Boolean Switch expression"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": ("BOOLEAN",)
        }, "optional": {
            "Flow": ("FLOW",),
            "True": (any,),
            "False": (any,),
        }}

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Result",)
    FUNCTION = "node"

    def node(self, Value, **kwargs):
        return (kwargs["True"] if Value else kwargs["False"],)


class SwitchExpr(BaseNode):
    name = "Int Switch expression"
    display_name = "🔀 Int Switch expression"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": ("INT", {"default": 0, "min": 0, "max": 19, "step": 1})
        }, "optional":
            {"Case " + str(v): (any, {"dynamicAvailable": "Case"}) for v in range(20)} | {"Flow": ("FLOW",)}
        }

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Result",)
    FUNCTION = "node"

    def node(self, Value, **kwargs):
        key = "Case " + str(Value)
        return (kwargs[key] if key in kwargs else None,)


class FlowStartNode(BaseNode):
    name = "Flow start"
    display_name = "🌊 Activate flow from any"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {},
                "optional": {
                    "Trigger": (any,)
                }}

    CATEGORY = category
    RETURN_TYPES = ("FLOW",)
    RETURN_NAMES = ("Flow",)
    FUNCTION = "node"

    def node(self, **kwargs):
        return (None,)  # Flow is just a hack to get the executions in the wanted order.


class FlowMergeNode(BaseNode):
    name = "Flow merge"
    display_name = "🌊 Merge flow (bottleneck)"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Input": (any,)
        }, "optional": {
            "Flow": ("FLOW",)
        }}

    CATEGORY = category
    RETURN_TYPES = (any, "FLOW")
    RETURN_NAMES = ("Output", "Flow")
    FUNCTION = "node"

    def node(self, Input, Flow, **kwargs):
        return Input, Flow
