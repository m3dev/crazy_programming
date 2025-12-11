# TypeScript Quine

## 実行

Quine の実行

```sh
npm run quine
```

開発用（Watch モード + Quine 成立判定）

```sh
npm run dev
```

## セットアップ

Node.js 環境のセットアップ後、インストールを実行してください。

```sh
npm install
```

### 注意点

TypeScript を直接実行する都合上、v23.6.0 以降の Node.js が必要です。
22 系であれば v22.18.0 以降が必要です。

それ以前の Node.js のバージョンでは実行できないか、`--experimental-strip-types` フラグが必要です。

## ファイル構成

- `quine.ts`: Quine 本体
- `index.ts`: 開発用のエントリポイント
- `aa.ts`: アスキーアートのエンコード用の補助スクリプト
