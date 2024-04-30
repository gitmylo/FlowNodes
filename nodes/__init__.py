from .cond import *
conds = [
    IfCond,
    BoolSwitchExpr,
    SwitchExpr
]

from .comp import *
comps = [
    IntCompare,
    FloatCompare
]

from .logic import *
logics = [
    LogicNode,
    NotNode
]

from .math import *
maths = [
    IntExpression,
    FloatExpression
]

from .function import *
functions = [

]

from .convert import *
converts = [
    ConvertToType
]

nodes = conds + comps + logics + maths + functions + converts
