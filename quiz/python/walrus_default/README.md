# Walrus Default

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

セイウチ演算子とlambdaのデフォルト引数が入り乱れるクイズ。

```python
(lambda _=(_:=()):_)(_:=())
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
