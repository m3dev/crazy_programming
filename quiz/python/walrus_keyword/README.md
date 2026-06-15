# Walrus Keyword

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`_=...`がキーワード引数なのかセイウチ演算子なのか見分けがつかないクイズ。

```python
((lambda _=(_:=()):_)(_=(_:=())))
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
