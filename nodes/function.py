from .basenode import BaseNode
import re
from ..util.categories import categories
from .anytype import any

category = categories["func"]


class RegexMatch(BaseNode):
    name = "Regex match"
    display_name = "🔍 Regex match"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Pattern": ("STRING", {"default": "(.+)", "multiline": False}),
            "String": ("STRING", {"default": "", "multiline": True})
        }}

    RETURN_TYPES = ("REGEX_MATCHES", "INT")
    RETURN_NAMES = ("matches", "amount")
    FUNCTION = "regex_match"
    CATEGORY = category

    def regex_match(self, Pattern, String, **kwargs):
        matches = re.findall(Pattern, String, re.MULTILINE)
        return matches, len(matches)


custom_op_actions = ["f + s", "f - s", "f * s", "f / s", "f[s]", "getattr(f, s)"]
output_op_actions = ["f[s] = t", "setattr(f, s, t)", "f.append(s)"]


def custom_op_action(first, second, third, action):
    match action:
        case "f + s":
            return first + second
        case "f - s":
            return first - second
        case "f * s":
            return first * second
        case "f / s":
            return first / second
        case "f[s]":
            print(type(first))
            if isinstance(first, list):
                if len(first) < second and second >= 0:
                    return first[second]
            elif isinstance(first, dict):
                if second in first:
                    return first[second]
            return third
        case "getattr(f, s)":
            if hasattr(first, second):
                return getattr(first, second)
            return third

        case "f[s] = t":
            first[second] = third
            return first
        case "setattr(f, s, t)":
            setattr(first, second, third)
            return first
        case "f.append(s)":
            first.append(second)
            return first
    return None


class CustomOperation(BaseNode):
    name = "Generic operation"
    display_name = "📖 Generic operation"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Action": (custom_op_actions,),
            "First": (any,),
            "Second": (any,),

            "no_cache": ("NO_CACHE",)
        }, "optional": {
            "Default": (any,),
            "Flow": ("FLOW",)
        }}

    RETURN_TYPES = (any, "FLOW")
    RETURN_NAMES = ("Result", "Flow")
    FUNCTION = "custom_operation"
    CATEGORY = category

    def custom_operation(self, Action, First, Second, **kwargs):
        return custom_op_action(First, Second, kwargs["Default"] if "Default" in kwargs else None, Action), None


class CustomOutputOperation(CustomOperation):
    name = "Generic operation (write)"
    display_name = "📖 Generic operation (write)"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Action": (output_op_actions,),
            "First": (any,),
            "Second": (any,),

            "no_cache": ("NO_CACHE",)
        },
            "optional": {
                "Third": (any),
                "Flow": ("FLOW",)
            }}

    RETURN_TYPES = (any, "FLOW")
    RETURN_NAMES = ("First", "Flow",)

    def custom_operation(self, Action, First, Second, **kwargs):
        return (custom_op_action(First, Second, kwargs["Third"] if "Third" in kwargs else None, Action), None)


class ConsolePrint(BaseNode):
    name = "Console print"
    display_name = "💻 Print to console"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": (any,),
            "no_cache": ("NO_CACHE",)
        }}

    RETURN_TYPES = ("FLOW",)
    RETURN_NAMES = ("Flow",)
    FUNCTION = "console_print"
    CATEGORY = category
    OUTPUT_NODE = True

    def console_print(self, Value, **kwargs):
        print(Value)
        return (None,)


class ExecuteScript(BaseNode):
    name = "Execute Python"
    display_name = "🐍 Execute python (UNSAFE)"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": ("STRING", {"default": "out = input0", "multiline": True}),
            "no_cache": ("NO_CACHE",)
        }, "optional": {
            "Input": (any,),
            "Flow": ("FLOW",)
        }}

    RETURN_TYPES = (any, "FLOW")
    RETURN_NAMES = ("Output", "Flow")
    FUNCTION = "exec_script"
    CATEGORY = category

    def exec_script(self, Value, **kwargs):
        # inp = kwargs["Input"] if "Input" in kwargs.keys() else None
        glob = {}
        loc = {"out": None}
        if "Input" in kwargs:
            if isinstance(kwargs["Input"], dict):
                loc = loc | (kwargs["Input"])
            else:
                loc["input0"] = kwargs["Input"]

        exec(Value, glob, loc)  # defined function will be stored in locals
        return loc['out'], None


class StackParams(BaseNode):
    name = "Stack parameters"
    display_name = "🐍 Stack python exec parameters"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {}, "optional":
                {"input" + str(i): (any, {"dynamicAvailable": "input"}) for i in range(20)} | {"Flow": ("FLOW",)}
        }

    RETURN_TYPES = ("EXEC_PARAMS", "FLOW")
    RETURN_NAMES = ("Stacked params", "Flow")
    FUNCTION = "stack_params"
    CATEGORY = category

    def stack_params(self, **kwargs):
        return kwargs, None


persistent_object = {}


class GetGlobalObject(BaseNode):
    name = "Get persistent dict"
    display_name = "🔺 Get persistent dict"

    @classmethod
    def INPUT_TYPES(s):
        # return {"required": {}, "hidden": {"no_cache": ("_", {"NoCache": True})}}
        return {"required": {
            "no_cache": ("NO_CACHE",)
        }}

    RETURN_TYPES = (any,)
    RETURN_NAMES = ("Persistent dict",)
    FUNCTION = "get_persistent"
    CATEGORY = category

    def get_persistent(self, **kwargs):
        global persistent_object
        return (persistent_object,)
