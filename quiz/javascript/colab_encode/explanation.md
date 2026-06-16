# 解説

```javascript
((s,[a,b,c,d,e]=new TextEncoder().encode(s))=>String.fromCharCode(a+c-e)+(b-c))("Colab")
```

このクイズコードがなぜ `M3` を出力するのか、ステップごとに解説します。

---

## 全体の構造

* 即時実行関数（IIFE）
* 第1引数：`s` に `"Colab"` が渡される
* 第2引数 `[a,b,c,d,e]` はデフォルト値で、`new TextEncoder().encode(s)` を分割代入している

---

## 1. `TextEncoder().encode(s)` でバイト列を作る

```javascript
new TextEncoder().encode("Colab")
```

`TextEncoder` は文字列をUTF-8の **バイト列（`Uint8Array`）** に変換します。`"Colab"` はすべてASCII文字なので、各文字のコードポイントがそのままバイトになります。

| 文字 | `C` | `o` | `l` | `a` | `b` |
|---|---|---|---|---|---|
| バイト | 67 | 111 | 108 | 97 | 98 |

これを `[a,b,c,d,e]` に分割代入するので、

```javascript
a = 67   // 'C'
b = 111  // 'o'
c = 108  // 'l'
d = 97   // 'a'
e = 98   // 'b'
```

となります（`d` は使われません）。

---

## 2. `String.fromCharCode(a+c-e)` で `'M'` を作る

```javascript
a + c - e   // 67 + 108 - 98 = 77
```

`String.fromCharCode(77)` は文字コード77の文字、つまり大文字の **`'M'`** です。

```javascript
String.fromCharCode(77)   // => "M"
```

---

## 3. `(b-c)` で `3` を作る

```javascript
b - c   // 111 - 108 = 3
```

数値の `3` になります。

---

## 4. 文字列と数値の `+` で結合 → `"M3"`

```javascript
"M" + 3
```

`+` の左が文字列なので数値 `3` も文字列に変換され、結合されて `"M3"` になります。

```javascript
"M" + 3   // => "M3"
```

---

## まとめ

1. `TextEncoder().encode("Colab")` で `[67,111,108,97,98]` というバイト列を得る
2. `a+c-e = 77` を `String.fromCharCode` で `'M'` に変換
3. `b-c = 3`
4. `"M" + 3` の文字列結合で `"M3"`

「文字のバイト値を足し引きしてエムスリーのロゴ `M3` を作り出す」という問題でした。
