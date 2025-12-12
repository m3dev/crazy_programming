# 解説

```bash
node -e "console.log(((_,$=[].push(_,_))=>`${(typeof $)[$]}${String($/$.$).length}`)(\"Colab\"));"
```

このクイズコードがなぜ `m3` を出力するのか、ステップごとに解説します。

---

## 全体の構造

中身だけ抜き出すと、こういう形です。

```javascript
((_,$=[].push(_,_)) => `${(typeof $)[$]}${String($/$.$).length}`)("Colab")
```

* 即時実行関数（IIFE）
* 第1引数：`_` に `"Colab"` が渡される
* 関数本体の戻り値を `console.log` で出力している

---

## 1. 引数とデフォルト値

```javascript
(_,$=[].push(_,_)) => ...
```

ここでのポイントは `$` の初期化です。

```javascript
$ = [].push(_,_)
```

* `[]` は空配列
* `[].push(_, _)` は

  * 配列に 2 つ要素を追加し
  * 戻り値として「新しい配列の長さ」を返す

したがって、

```javascript
$ === 2
```

となります。
ここで渡した `_("Colab")` の中身そのものは、「値としては」どこでも直接使われていません（あくまで「2 個 push するため」に使っているだけ）。

---

## 2. `(typeof $)[$]` で `'m'` を取り出す

次の部分を見ます。

```javascript
(typeof $)[$]
```

* さきほどの計算で `$ === 2`
* `typeof $` は

```javascript
typeof 2   // "number"
```

となるので、これは

```javascript
"number"[2]
```

と同じです。

文字列 `"number"` を配列のようにインデックスアクセスすると、

* `"number"[0]` → `'n'`
* `"number"[1]` → `'u'`
* `"number"[2]` → `'m'`

したがって、

```javascript
(typeof $)[$] === "m"
```

になります。

---

## 3. `String($/$.$).length` で `3` を取り出す

次の部分はこちらです。

```javascript
String($ / $.$).length
```

### 3-1. `$ / $.$` の中身

* `$` は数値 `2`
* `$.$` は「数値 2 のプロパティ `.$`」ですが、そんなプロパティは存在しないので `undefined`

したがって、

```javascript
$ / $.$   // 2 / undefined → NaN
```

`NaN`（Not-a-Number）が得られます。

### 3-2. `String(NaN).length`

次にそれを `String(...)` で文字列化し、長さを取っています。

```javascript
String(NaN)   // "NaN"
String(NaN).length  // 3
```

よって、

```javascript
String($/$.$).length === 3
```

です。

---

## 4. テンプレートリテラルで結合 → `"m3"`

最終的な戻り値はテンプレートリテラルで作られています。

```javascript
`${(typeof $)[$]}${String($/$.$).length}`
```

ここにこれまでの結果を代入すると、

* `(typeof $)[$]` → `"m"`
* `String($/$.$).length` → `3`

なので、

```javascript
`${...}${...}` → "m3"
```

になります。
この文字列が `console.log` に渡されるため、最終的な出力は

```text
m3
```

となります。

---

## まとめ

このワンライナーのポイントは：

1. `[].push(_, _)` の戻り値で「2」を作る
2. `typeof 2` → `"number"` からインデックス `[2]` で `"m"` を抜き出す
3. `2 / undefined` で `NaN` を作り、`String(NaN).length` で `3` を取り出す
4. それらをテンプレートリテラルで `"m3"` に結合する

という、「型名 `number` と `NaN` の文字列表現を利用した」かなりきれいな難読パターンになっています。

