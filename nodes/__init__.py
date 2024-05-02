from .cond import *
conds = [
    IfCond,
    BoolSwitchExpr,
    SwitchExpr,
    FlowStartNode,
    FlowMergeNode
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
    RegexMatch,
    ConsolePrint,
    CustomOperation,
    CustomOutputOperation,
    ExecuteScript,
    StackParams,
    GetGlobalObject
]

from .convert import *
converts = [
    ConvertToType,
    CreateEmpty
]

nodes = conds + comps + logics + maths + functions + converts
