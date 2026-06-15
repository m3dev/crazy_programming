# Nested F-string

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

f-stringを入れ子にして`=`デバッグを重ねた混乱する系のクイズ。

```python
f"""{f"{'a'+'b'=}"+f"{'c'+'d'=}"=}"""
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
