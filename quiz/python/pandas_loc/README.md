# Pandas Loc

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

コロンだらけのf-stringとpandasの`.loc`スライスを組み合わせたクイズ。

```python
import pandas as pd
print(pd.DataFrame({(_:=f"{':'::^3}"):[(':')[::]]}).loc[::,':':_])
```

## 実行

```sh
uv run python main.py
```

## 解説

`explanation.md`で解説しています
