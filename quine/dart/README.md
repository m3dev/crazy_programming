# Dart Quine

Author: [@AAkira](https://github.com/aakira)

Dartで作成したQuine

## 実行

dart runでquineを実行します。

```sh
dart run quine.dart
```

## 解説

古いバージョンですが、こちらで解説しています。

- [DartでQuineをダーッと書きました](https://www.m3tech.blog/entry/dart-quine)

### 前回との差分

新しいバージョンはAAがエムスリー社内で統一されたため、AAを変更しています。  
それに伴い、古いバージョンはAAでquineの長さ調整をしていた箇所をbase64エンコードの文字列で調整しています。
コード部分もListの長さチェックがなくなり短くなりました。(古いバージョンの `E<u.length?u[E++]:'';` 部分)  
また、調整で長くなったbase64部分(`:`で分割した3つ目の文字列)をデコードすると以下のリンクが埋め込まれています。

```
* Tech blog: https://www.m3tech.blog
* X: https://x.com/m3_engineering
* YouTube: https://www.youtube.com/@m3techchannel160
* GitHub: https://github.com/m3dev
```

その他、文字列調整のために変数を増やし、変数宣言で `WE are HIRING! join M3 group!` という遊びを入れています。

