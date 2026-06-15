# Enum Hash Collision

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

Enumのエイリアスと辞書の後勝ちが重なるクイズ

```python
from enum import Enum
class Ex(Enum):
    int_num = 1
    bool_num = True
    float_num = 1.0
print({Ex['int_num']:'int', Ex['bool_num']:'bool', Ex['float_num']:'float'})
```

## 実行

```sh
uv run python main.py
```

## 解説

`explanation.md`で解説しています
