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

    def convert(self, Type, Input, **kwargs):
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


class MergeList(BaseNode):
    name = "Merge batch (any)"
    display_name = "📃 List to Batch"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "List": (any,)
        }}

    INPUT_IS_LIST = (True,)

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Batch",)
    FUNCTION = "merge_list"

    def merge_list(self, List, **kwargs):
        return (List,)


class UnMergeList(BaseNode):
    name = "Unmerge batch (any)"
    display_name = "📃 Batch to List"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Batch": (any,)
        }}

    OUTPUT_IS_LIST = (True,)

    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("List",)
    FUNCTION = "unmerge_list"

    def unmerge_list(self, Batch, **kwargs):
        return (Batch,)


class CreateList(BaseNode):
    name = "Create batch"
    display_name = "📃 Create batch"

    @classmethod
    def INPUT_TYPES(s):
        return {
                    "required": {"no_cache": ("NO_CACHE",)},
                    "optional": {"input" + str(i): (any, {"dynamicAvailable": "input"}) for i in range(20)}
                }


    CATEGORY = category
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Batch",)
    FUNCTION = "create_list"

    def create_list(self, **kwargs):
        return (list({k: kwargs[k] for k in kwargs if k != "no_cache"}.values()),)
