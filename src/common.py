from collections import namedtuple

Instruction = namedtuple(
    "_Instruction",
    [
        'opname',
        'opcode',
        'arg',
        'argval',
        'offset',
        'lineno',
    ]
)
