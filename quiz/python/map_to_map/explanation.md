# 解説

mapが沢山ならんだ問題です。

```pyhton
list(map(list,list(map(map,map(lambda map:list,map:='map'),map))))
```

mapの挙動に詳しく見てみます。
mapはiterableなオブジェクト全てに関数を適応します。
返り値はIteratorなのでlist function等を適応する必要があります。

```python
>>> print(map(str, [1, 2, 3]))
<map object at ...>

>>> print(list(map(str, [1, 2, 3])))
["1", "2", "3"]
```

mapの第一引数にlistを入れると第2引数のiteratorを回してlist化します。

```python
>>> print(list(map(list, '123')))
[["1"], ["2"], ["3"]]
```

mapの第2引数以降はzipのように扱えます。
これを利用してmapの中にmapを書いてみます。

```python
>>> x = map(map, [list,list,list,list], "test")

>>> print(list(x))
[<map...>, <map...>,  <map...>,  <map...>]

>>> print([list(y) for y in x])
[[['t']], [['e']], [['s']], [['t']]]
```

上記のままだと"test"という長さ4の文字列に対して長さ4の[list,...]が必要です。
エレガントではないので任意の長さの[list,...]なiterable objectを生成します。

```python
>>> x = map(lambda map:list, "test")
>>> print(list(x))
[list, list, list, list]
```

上記までを利用するとmapの中にmapをエレガントに書くことができます。

```python
>>> x = map(map,map(lambda map:list, 'test'), 'test')
>>> print([list(y) for y in x])
[[['t']], [['e']], [['s']], [['t']]]
```

ですが"test"を2回書いているのはエレガントではないですね。
セイウチ演算子を使ってmapという変数に"map"という文字を入れてあげます。
この時、一番最後のmapだけが変数のmap、それ以外は全てmap関数です。

```python
>>> x = map(map,map(lambda map:list, map:='map'), map)
>>> print([list(y) for y in x])
[[['m']], [['a']], [['p']]]
```

最後にfor文も消してよりエレガントにすれば完成です。

```python
>>> x = map(list, list(map(map,map(lambda map:list, map:='map'), map)))
>>> print(list(x))
[[['m']], [['a']], [['p']]]
```

という訳で、`[[['m']], [['a']], [['p']]]`が正解なのでした。
この問題、セイウチ演算子のところでmap関数をmap変数として上書きしているので、当然Pythonスクリプトの中で連続して実行できません。
それでもmapを1つでも多く書きたいという熱い想いの籠もった問題になっています。
実はちょうど問題作成時期に「Pythonのmapが苦手」という記事がインターネットで話題になっており、mapの研究をしていたら出来上がった問題なのでした。
こんな書き方をプロダクションコードでしたら、レビューで一刀両断されるでしょうね。
mapだけに、真っ二つってね。
