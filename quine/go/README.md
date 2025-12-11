# Go Quine

Author: [@inakam00](https://github.com/inakam00)

m3ロゴの形をしたGo言語のQuine。

## 実行

```sh
go run quine.go
```

## ジェネレータ

以下のコードを使う事でオリジナルのGo Quineを作成することができます。

```sh
# m3_mask.txtをマスクとしてQuineを生成
python generator.py
```

以下のような形で開発しています。

1. `m3_mask.txt`に0/1でAAを定義（0: コード、1: 空白）
2. `generator.py`を実行してQuineを生成
3. 生成された`main.go`を実行して確認
4. Base64エンコードされた文字列の末尾に任意の文字列を追加（空白が必要であればマスクを再度調整して再生成する）

## 解説

[Goでgo fmtしたくないコードを書いた（Go版Quine）](https://www.m3tech.blog/entry/golang-quine)にて解説しています。
