from abc import abstractmethod

from .basenode import BaseNode
from ..util.categories import categories

category = categories["logic"]


class LogicNode(BaseNode):

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "A": ("BOOLEAN",),
            "B": ("BOOLEAN",)
        }}

    CATEGORY = category
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "operation"

    @abstractmethod
    def operation(self, A: bool, B: bool):
        pass


class AndNode(LogicNode):
    name = "Boolean And"
    display_name = "🆎 Boolean And"

    def operation(self, A: bool, B: bool):
        return A and B


class OrNode(LogicNode):
    name = "Boolean Or"
    display_name = "🆎 Boolean Or"

    def operation(self, A: bool, B: bool):
        return A or B


class EqNode(LogicNode):
    name = "Boolean Equals"
    display_name = "🆎 Boolean Equals"

    def operation(self, A: bool, B: bool):
        return A == B


class NeqNode(LogicNode):
    name = "Boolean Not Equals"
    display_name = "🆎 Boolean Not Equals"

    def operation(self, A: bool, B: bool):
        return A != B


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
        return not In
