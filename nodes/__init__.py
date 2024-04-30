# from .file import *
from .cond import *
conds = [
    IfCond
]

from .loop import *
loops = [

]

from .logic import *
logics = [
    AndNode,
    OrNode,
    EqNode,
    NeqNode,
    NotNode
]

nodes = conds + loops + logics
