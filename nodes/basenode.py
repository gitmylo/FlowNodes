from abc import abstractmethod

from util.categories import category


class BaseNode:
    name = "Node"
    display_name = name

    @classmethod
    @abstractmethod
    def INPUT_TYPES(s):
        pass  # required, optional, hidden

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = ""
    CATEGORY = category("uncategorized")
