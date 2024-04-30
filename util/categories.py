from .util import format_name


def category(name: str) -> str:
    return format_name("FlowNodes/" + name)


categories = {
    "cond": category("conditions"),
    "loop": category("loops"),
    "logic": category("logic"),
}
