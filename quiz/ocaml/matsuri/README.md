# Matsuri

関数型まつり2026用のクイズです

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`"Matsuri"` という文字列を加工するOCamlのクイズです。実行すると何が出力されるでしょう？

```ocaml
"Matsuri"|>fun s->Printf.sprintf"%c%d"s.[0]((String.fold_left(fun n _->n+1)0 s)/2);;
```

## 実行

utopやREPLを使い実行してください。

```sh
ocaml
```

## 解説

`explanation.md`で解説しています
