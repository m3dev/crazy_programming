from enum import Enum
class Ex(Enum):
    int_num = 1
    bool_num = True
    float_num = 1.0
print({Ex['int_num']:'int', Ex['bool_num']:'bool', Ex['float_num']:'float'})
