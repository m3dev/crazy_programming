# Reduce 5000

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`map`や`numeric`を引数名にして組込みを隠した、5000兆クイズ。

```python
from functools import reduce
from unicodedata import numeric
print(reduce(lambda map,numeric:numeric*map,map(numeric,'5000兆')))
```

## 実行

```sh
uv run python main.py
```

## 解説

`explanation.md`で解説しています
