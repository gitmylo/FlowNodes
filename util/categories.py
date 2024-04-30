from .util import format_name


def category(name: str) -> str:
    return format_name("FlowNodes/" + name)


categories = {
    "cond": category("conditions"),
    "comp": category("comparisons"),
    "logic": category("logic"),
    "math": category("math"),
    "func": category("function"),
    "conv": category("convert")
}
