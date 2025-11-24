# 難読Rubyコードクイズ問題 in RubyWorldConference2022

- Author: [@Owl](https://github.com/owl-bo)

RubyWorldConference2022にてスポンサーブースで紹介した問題です。
以下のブログで解説しています。

- [難読RubyクイズReturns Day0 @RubyWorldConference2022 - エムスリーテックブログ](https://www.m3tech.blog/entry/2022/11/01/143000)

## requierments

irbを使い実行してください。

```sh
rbenv install
rbenv local
irb
```

## Quiz

### 1. マイナスのマイナスは？

```ruby
-a=--1.to_s
```

### 2. アンダースコアの意味

```ruby
[1_1, 1_2, 1_3].map{_2}|[]
```

### 3. 綺麗で不可解で無意味

```ruby
_=_|_=__=_|_=_
```
