# 解説

この問題は`unicodedata.numeric`と`functools.reduce`を使い、さらに引数名で組込みを隠す目くらましを仕込んでいます。

まず`unicodedata.numeric`はUnicode文字が持つ数値としての値を返す関数です。漢数字なども数値に変換できます。

```python
>>> from unicodedata import numeric
>>> numeric('5')
5.0
>>> numeric('兆')
1000000000000.0
```

`map(numeric, '5000兆')`は文字列`'5000兆'`の各文字に`numeric`を適用し、次の値の列を作ります。

```python
>>> list(map(numeric, '5000兆'))
[5.0, 0.0, 0.0, 0.0, 1000000000000.0]
```

`reduce`はこの列を左から順に畳み込みます。lambdaの引数名が`map`と`numeric`になっていて、組込みの`map`関数や`numeric`関数と同じ名前なので混乱しますが、lambdaの中ではあくまでローカルな引数です。中身は`numeric * map`、つまり2つの値の掛け算です。

```python
>>> from functools import reduce
>>> reduce(lambda map, numeric: numeric * map, [5.0, 0.0, 0.0, 0.0, 1000000000000.0])
0.0
```

途中に`0.0`が含まれるため、掛け算の結果はどこかで`0.0`になり、最終的に`0.0`になります。

```python
>>> reduce(lambda map,numeric:numeric*map,map(numeric,'5000兆'))
0.0
```

答えは`0.0`です。
`map`や`numeric`という名前を引数に使って組込みを隠す目くらましがありますが、本質は0を含む積なので0になる、という問題でした。
