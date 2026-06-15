# parse int tag

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

タグ付きテンプレートで `parseInt` と `toString` を呼んでいます。何が出力されるでしょう。

```javascript
parseInt`256${~-16}`.toString`24`
```

## 実行

```sh
nvm use
node -e 'console.log(parseInt`256${~-16}`.toString`24`)'
```

## 解説

`explanation.md`で解説しています
