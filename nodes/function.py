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
output_op_actions = ["f[s] = t", "setattr(f, s, t)"]


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
            return first[second]
        case "getattr(f, s)":
            return getattr(first, second)

        case "f[s] = t":
            first[second] = third
            return None
        case "setattr(f, s, t)":
            setattr(first, second, third)
            return None
    return None


class CustomOperation(BaseNode):
    name = "Generic operation"
    display_name = "📖 Generic operation"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Action": (custom_op_actions,),
            "First": (any,),
            "Second": (any,)
        }, "optional": {
            "Flow": ("FLOW",)
        }}

    RETURN_TYPES = (any, "FLOW")
    RETURN_NAMES = ("Result", "Flow")
    FUNCTION = "custom_operation"
    CATEGORY = category

    def custom_operation(self, Action, First, Second, **kwargs):
        return custom_op_action(First, Second, None, Action), None


class CustomOutputOperation(CustomOperation):
    name = "Generic operation (write)"
    display_name = "📖 Generic operation (write)"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Action": (output_op_actions,),
            "First": (any,),
            "Second": (any,)
        },
            "optional": {
                "Third": (any),
                "Flow": ("FLOW",)
            }}

    RETURN_TYPES = ("FLOW",)
    RETURN_NAMES = ("Flow",)

    def custom_operation(self, Action, First, Second, Third, **kwargs):
        custom_op_action(First, Second, Third, Action)
        return (None,)


class ConsolePrint(BaseNode):
    name = "Console print"
    display_name = "💻 Print to console"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": (any,)
        }}

    RETURN_TYPES = ("FLOW",)
    RETURN_NAMES = ("Flow",)
    FUNCTION = "console_print"
    CATEGORY = category
    OUTPUT_NODE = True

    def console_print(self, Value):
        print(Value)
        return (None,)


class ExecuteScript(BaseNode):
    name = "Execute Python"
    display_name = "🐍 Execute python (UNSAFE)"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "Value": ("STRING", {"default": "out = inp", "multiline": True})
        }, "optional": {
            "Input": (any,),
            "Flow": ("FLOW",)
        }}

    RETURN_TYPES = (any, "FLOW")
    RETURN_NAMES = ("Output", "Flow")
    FUNCTION = "exec_script"
    CATEGORY = category

    def exec_script(self, Value, **kwargs):
        inp = kwargs["Input"] if "Input" in kwargs.keys() else None
        glob = {}
        loc = {"inp": inp, "out": None}
        exec(Value, glob, loc)  # defined function will be stored in locals
        return loc['out'], None
