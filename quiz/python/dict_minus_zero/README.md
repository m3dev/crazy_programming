# Dict Minus Zero

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

数値リテラルとdictのキー衝突を扱う、0だらけのクイズ。

```python
{-.0_0:00_0,00:.0,.0:-0}
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
