# 解説

```sh
node -e "console.log(String.fromCharCode.toString()[12] + 3)"
```

このクイズがなぜ `m3` を出力するのか、ステップごとに解説します。

---

## 1. 関数を文字列化する

`String.fromCharCode` は組み込み関数です。これを `toString()` すると、その関数のソース表現が文字列で得られます。

ネイティブ関数の場合、Node では次のような文字列になります。

```javascript
> String.fromCharCode.toString()
'function fromCharCode() { [native code] }'
```

---

## 2. インデックス12の文字を取り出す

得られた文字列の先頭から数えてみます。

```text
 f  u  n  c  t  i  o  n     f  r  o  m   C ...
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 ...
```

* 0〜7 が `function`
* 8 が半角スペース
* 9 が `f`、10 が `r`、11 が `o`、**12 が `m`**

したがって、

```javascript
> String.fromCharCode.toString()[12]
'm'
```

`'m'` が取り出せます。

---

## 3. 数値 `3` との連結

最後に `+ 3` をしています。左辺が文字列 `'m'` なので、`+` は文字列連結として働き、数値 `3` も文字列化されます。

```javascript
> 'm' + 3
'm3'
```

よって出力は

```text
m3
```

となります。

---

## まとめ

1. `String.fromCharCode.toString()` でネイティブ関数の文字列表現を得る
2. その12文字目がちょうど `'m'`
3. 文字列 `'m'` に数値 `3` を連結して `"m3"`
