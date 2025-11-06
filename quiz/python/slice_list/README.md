# Slice List

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

リストのスライスの知識を深める難読クイズ。

```python
[x:=1,x:=-~x,-~x][:][::-1][:1]
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
