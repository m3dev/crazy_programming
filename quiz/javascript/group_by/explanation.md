# 解説

```javascript
Object.entries(Object.groupBy(["Medicine","Media","Metamorphosis"],([m]) => m))[0].map(m=>Array.isArray(m)?m.length:m).join("")
```

このコードの実行結果は `"M3"` です。

---

## 1. `Object.groupBy` でキーごとにまとめる

```javascript
Object.groupBy(["Medicine","Media","Metamorphosis"], ([m]) => m)
```

`Object.groupBy`（ES2024）は配列の各要素をコールバックの戻り値をキーにしてグループ化します。

コールバック `([m]) => m` は引数を **分割代入** しています。文字列に対して配列の分割代入をすると **先頭の1文字** が取り出せるため、`[m]` は各単語の頭文字です。

* `"Medicine"` → `'M'`
* `"Media"` → `'M'`
* `"Metamorphosis"` → `'M'`

すべて `'M'` 始まりなので、1つのグループにまとまります。

```javascript
{ M: ["Medicine", "Media", "Metamorphosis"] }
```

---

## 2. `Object.entries(...)[0]` で最初のエントリを取る

```javascript
Object.entries({ M: [...] })   // => [ ["M", ["Medicine","Media","Metamorphosis"]] ]
[0]                            // => ["M", ["Medicine","Media","Metamorphosis"]]
```

`[キー, 値]` の形のペア（2要素の配列）が得られます。

---

## 3. `.map(...)` で要素ごとに変換

```javascript
.map(m => Array.isArray(m) ? m.length : m)
```

ペアの各要素に対して「配列なら長さ、そうでなければそのまま」を返します。

* 1つ目 `"M"` → 配列ではない → そのまま `"M"`
* 2つ目 `["Medicine","Media","Metamorphosis"]` → 配列 → 長さ `3`

```javascript
["M", 3]
```

---

## 4. `.join("")` で結合 → `"M3"`

```javascript
["M", 3].join("")   // => "M3"
```

数値 `3` も文字列化されて結合され、結果は `"M3"` になります。

---

## まとめ

1. `Object.groupBy` で頭文字をキーにグループ化すると、全部 `'M'` 始まりなので `{ M: [3単語] }`
2. `Object.entries(...)[0]` で `["M", [3単語]]` を取り出す
3. `map` でキー `"M"` はそのまま、値の配列は長さ `3` に変換
4. `join("")` で `"M3"`

`Object.groupBy` と文字列の分割代入を組み合わせた問題でした。
