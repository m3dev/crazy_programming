# Kotlin Quine

Author: [@satorufujiwara](https://github.com/satorufujiwara)

Kotlinで作成したQuine

## 実行

コンパイルして実行してください。

```sh
kotlinc quine.kt -include-runtime -d quine.jar
java -jar quine.jar
```

[Kotlin Playground](https://pl.kotl.in/1k8Q0GWtj)でもお楽しみいただけます。

## 解説

古いバージョンですが、こちらで解説しています。

- [エムスリーがKotlin Loverに贈るノベルティ、Kotlin Quineクリアファイルを作りました](https://www.m3tech.blog/entry/kotlin-quine)

### 前回との差分

コード自体は大きく変えていませんが、新しいバージョンはAAがエムスリー社内で統一されたため、AAを変更しています。  
それに伴い行数が2行減った=使える文字数が200文字減ったので、AA部分までコードを紛れ込ませるなど、細かい文字数調整を頑張りました。

