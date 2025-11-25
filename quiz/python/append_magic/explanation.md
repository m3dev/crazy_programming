# 解説

Pythonのリストのappendメソッドのトリックを使ったワンライナー問題です。

```python
(x:=[[]]*3)[0].append(1);x
```

冒頭の`:=`の部分は、Python3.8で導入されたセイウチ演算子です。
Walrus operator（セイウチ演算子）と公式でも呼ぶものだと思っていましたが、Pythonでの正式名称はAssignment Expressionsみたいです。

- [https://peps.python.org/pep-0572/](https://peps.python.org/pep-0572/)

セイウチ演算子は評価のタイミングで代入を行える演算子です。
評価結果は代入値になります。

```python
>>> print(x:=1)
1

>>> print(x)
1
```

リストのリストに数値を掛けると中身が増えます。

```python
>>> print([[]] * 3)
[[], [], []]
```

上記で増やしたリストは同じポインタを見ています。
故にappendすると全ての配列にappendされます。

```python
>>> x = [[]] * 3
>>> x[0].append(1)
>>> print(x)
[[1], [1], [1]]
```

上記の流れをワンライナーで表現したのが`(x:=[[]]*3)[0].append(1);x`で、答えは`[[1], [1], [1]]`でした。
