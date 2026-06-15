# Reduce 5000 Lambda

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

lambdaのデフォルト引数でセイウチ演算子を使い名前を再代入する、5000兆クイズの発展版。

```python
from functools import reduce
from unicodedata import numeric
print(reduce(lambda numeric=(reduce:=map), map=(reduce:=numeric):numeric*map, map(numeric,'5000兆')))
```

## 実行

```sh
uv run python main.py
```

## 解説

`explanation.md`で解説しています
