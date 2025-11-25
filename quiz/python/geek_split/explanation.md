# 解説

"geek"という文字列を操作しているようです。
Assignment Expressionsを使った問題です。

まず、strのsplitメソッドの第2引数を指定すると最大分割数を設定できます。

```python
>>> print( "a b c d e".split(" ", 2) )
["a", "b", "c d e"]
```

問題の最初のsplitの中でAssignment Expressionsを使っています。
変数_の中に文列`"_"`を代入した後、その長さを変数`_`に再代入しています。

```python
>>> "g_e_e_k".split(_:="_",_:=len(_))
['g', 'e_e_k']

>>> "g_e_e_k".split("_", 1)
['g', 'e_e_k']
```

変数`_`には数値1が入っているのでその後ろの配列indexで1の値が取り出されます。

```python
>>> "g_e_e_k".split("_", 1)[1]
'e_e_k'
```

2つ目のsplitも同様のトリックが使われています。

```python
>>> "e_e_k".split(_:="_",_:=len(_))[_]
'e_k'

>>> "e_e_k".split("_", 1)[1]
'e_k'
```

最後のsplitは第2引数なしですが同様のトリックです。

```python
>>> "e_k".split(_:="_")[len(_)]
'k'
```

最後に文字列"p"を足して乾杯です！

```python
>>> "k" + "p"
'kp'
```

Pythonの仕様を使いながら、綺麗な挙動に収めていく事を意識して作られた問題です。ギークに乾杯！
