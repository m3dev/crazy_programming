# 解説

```sh
node -e 'console.log([1, 2, 3].map(n => {num: n}).join()[1])'
```

このクイズがなぜ `,`（カンマ）を出力するのか、ステップごとに解説します。

---

## 1. `n => {num: n}` の `{}` はブロック文

アロー関数の本体に `{` を書くと、それは **関数本体のブロック** として解釈されます。オブジェクトリテラルではありません。

```javascript
n => { num: n }
```

このブロックの中身は次のように読まれます。

* `num:` … **ラベル文**（`num` という名前のラベル）
* `n` … ラベル付きの式文

オブジェクトの `{ num: n }` を作っているのではなく、ただラベルと式が並んでいるだけです。
そして `return` が無いので、この関数は毎回 **`undefined`** を返します。

```javascript
> (n => {num: n})(1)
undefined
```

オブジェクトを返したいなら、`n => ({num: n})` のように括弧で包む必要があります。

---

## 2. `map` の結果は `undefined` 3つ

```javascript
> [1, 2, 3].map(n => {num: n})
[ undefined, undefined, undefined ]
```

各要素が `undefined` になります。

---

## 3. `.join()` で文字列化

`Array.prototype.join()` は要素をカンマで連結します。このとき `undefined`（と `null`）は **空文字列** として扱われます。

```javascript
> [undefined, undefined, undefined].join()
',,'
```

要素3つを区切るカンマは2つなので、結果は `",,"` です。

---

## 4. インデックス1の文字

```text
 ,  ,
 0  1
```

```javascript
> ',,'[1]
','
```

index 1 はカンマ `','` です。

出力は

```text
,
```

となります。

---

## まとめ

1. アロー関数本体の `{...}` はオブジェクトではなく **ブロック文**（`num:` はラベル）
2. `return` が無いので各要素は `undefined` を返し、`map` の結果は `[undefined, undefined, undefined]`
3. `.join()` で `undefined` は空文字列になり `",,"`
4. その index 1 はカンマ `','`
5. オブジェクトを返すなら `n => ({num: n})` と括弧が必要、という罠
