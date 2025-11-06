# OCaml Quine

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

OCamlで作成したQuine。

## 実行

opamにより依存しているパッケージをインストールします。

```sh
opam install . --deps-only
```

ocaml cli commandから`quine.ml`を実行します。

```sh
ocaml quine.ml
```

## 開発ツール

以下の2つのコードを使う事でオリジナルのOcaml Quineを作成することができます。

```sh
# 0/1で構成されたaaをzstdで圧縮した後base64でエンコードする
ocaml aa2base64.ml

# base.mlスクリプトファイルを読み込んでbase64でエンコードする
ocaml code2base64.ml
```

以下のような形で開発しています。

1. `aa2base64.ml`内のAAを編集して実行
2. `aa2base64.ml`が出力したコードとlengthを`base.ml`の`XXXXXXXX...`部分に転記 (length初期値: 2625)
3. `code2base64.ml`を実行
4. `code2base64.ml`の出力で`base.ml`のプレースホルダ(`%s`)部分を置き換え
5. `base.ml`を実行

最終的に横幅が噛み合わない場合は、以下のような作業をした後、プレースホルダ等を元に戻して、1から繰り返し作業します。

- `aa2base64.ml`にあるzstdのcompress levelを調整する(1~22)
- `base.ml`の中で空白の位置やコメントの長さ等を調整する

## 解説

[M3 Tech Blog の 記事](https://www.m3tech.blog/entry/ocaml-quine)にて解説しています。
