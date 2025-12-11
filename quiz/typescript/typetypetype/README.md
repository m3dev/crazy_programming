# TypeTypeType

Author: [@yuta-ike](https://github.com/yuta-ike)

## 問題

a, b, c, d のうち、型エラーにならないものはどれ？

```ts
let type = "type";
type type<type> = type extends type ? type : typeof type;

const a: type<"type"> = type;
const b: type<"type"> = "type";
const c: type<"type"> = typeof type;
const d: type<"type"> = typeof "type";
```

[TypeScript Playground で確認する](https://www.typescriptlang.org/play/?#code/PTAEEMBpQI2hjaATUg7BkGIMhDBkIAMho9UBUMglwyA-DINYMgVgyCRDOYCIMgQQyqD2DIJYMgMQyD4-wFCcA2ApgBdQAgJ4AHPqAC8oAESiJsgNycFktQB41APmnDxkvgA8BfAHZIAzvomgA-DckAuRwHsAZo5Wd4rs5aFwF015A1ldGTUVX38hGGCDDVDFCLk1ZR8-ANB4BIkk9NS1Dy9M2NAkPL4CsKKDEuS+DKA)

<details>
  <summary>解答と解説</summary>

正解は b です。

`type` は JavaScript の予約語ではありません。TypeScript においても、変数名や型名、ジェネリクスの型変数名として使用可能です。

`type type<type> = type extends type ? type : typeof type;` をわかりやすく書き直すと以下のようになります。

```ts
type X<T> = T extends T ? T : typeof T;
```

さらに、T extends T は常に真なので、型 X は次のように簡略化できます。

```ts
type X<T> = T;
```

以上を踏まえて問題を分かりやすく書き直してみます。

```ts
let y = "type";
type X<T> = T;

const a: X<"type"> = y;
const b: X<"type"> = "type";
const c: X<"type"> = typeof y;
const d: X<"type"> = typeof "type";
```

ここで `X<"type">` は `"type"` というリテラル型に解決され、変数 y は let で宣言されているため string 型として扱われます。

以上を踏まえて各選択肢を確認します。

- a. `y`: y は string 型なので代入不可
- b. `"type"`: リテラル型 "type" と一致するので代入可能
- c. `typeof y`: typeof y は "string" | "number" | "bigint" | "boolean" | "symbol" | "undefined" | "object" | "function" に推論されるため代入不可
- d. `typeof "type"`: typeof "type"は、c と同様に "string" | "number" | "bigint" | "boolean" | "symbol" | "undefined" | "object" | "function" に推論されるため代入不可

以上より、型エラーにならないのは b のみです。

</details>
