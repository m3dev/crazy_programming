# Crazy Programming

## Description

実行するとソースコード自身と同じ文字列が返ってくるコード「Quine」、社内で開発された「プログラミングクイズ」を掲載しています。
社内Slackにおけるプログラミングの雑学を共有するチャンネル `#crazy-programming` より命名されたリポジトリです。

## Quine

<details>

<summary>Quine Table</summary>

|lang|title(link)|
|---|---|
|Dart|[M3 Dart Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/dart)|
|Go|[M3 Go Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/go)|
|Kotlin|[M3 Kotlin Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/kotlin)|
|OCaml|[M3 OCaml Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/ocaml)|
|Python|[M3 Python Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/python)|
|Python|[出力が動くFukuoka採用Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/python)|
|Ruby|[M3 Ruby Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/ruby)|
|Ruby|[M3 Logo Ruby Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/ruby)|
|Scala|[M3 Scala Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/scala)|
|Swift|[M3 Swift Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/swift)|
|Swift|[M3 Swift Quine: iOSDC Japan 2025 edition](https://github.com/m3dev/crazy_programming/tree/main/quine/swift)|
|TypeScript|[M3 TypeScript Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/typescript)|
|Terraform|[M3 Terraform Quine](https://github.com/m3dev/crazy_programming/tree/main/quine/terraform)|

</details>

## Programming Quiz

<details>

<summary>JavaScript Quiz Table</summary>

|title(link)|code|
|---|---|
|[技育プロジェクト](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/geek)|`[_='GEEK'.small()[2]]+[-~_._\|2];`|
|[TypeTypeType](https://github.com/m3dev/crazy_programming/tree/main/quiz/typescript/typetypetype)|`let type = "type";...`|
|[Colab](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/colab)|`((_,$=[].push(_,_))=>...`|
|[undefined label](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/undefined_label)|`console.log(eval("{undefined:[1]}['undefined'][0]"))`|
|[from char code](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/from_char_code)|`String.fromCharCode.toString()[12] + 3`|
|[math max](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/math_max)|`10000000000+(0[1]+Math.max)[3]+-1+-0-0`|
|[hex zero](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/hex_zero)|`0x0_0-0x0_0`|
|[regex filter](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/regex_filter)|`(r => ["3M", "M3"].filter(s => r.test(s)))(/[0-9]+/g)`|
|[parse int tag](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/parse_int_tag)|`` parseInt`256${~-16}`.toString`24` ``|
|[parse int radix](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/parse_int_radix)|`parseInt("256", ~-16).toString(0+11..toString(16)+11000)`|
|[octal add](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/octal_add)|`0011 + 0009`|
|[radix literals](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/radix_literals)|`010 + 0b10 + 0o10 + 0x10`|
|[dollar tag](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/dollar_tag)|`````$=()=>$;`${$````}`[4]`````|
|[dollar tag yoshi](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/dollar_tag_yoshi)|`````$$$$=()=>$$$$;`$$$${$$$$````}`[`𠮷𠮷`.length]`````|
|[map block](https://github.com/m3dev/crazy_programming/tree/main/quiz/javascript/map_block)|`[1, 2, 3].map(n => {num: n}).join()[1]`|

</details>

<details>

<summary>Python Quiz Table</summary>

|title(link)|code|
|---|---|
|[Is Face Mark?](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/is_face_mark)|`(d >_< b) if (c:=('ω')<"hi") else (c^0^c)-~3`|
|[While trick](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/while_trick)|`[1,2,3,4];while _:_,*_=_;_`|
|[Slice list](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/slice_list)|`[x:=1,x:=-~x,-~x][:][::-1][:1]`|
|[Slice hint](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/slice_hint)|`_:...=[];_[:]:...=f'{f"{[...][::][0]}"::^0}';_`|
|[Long addition](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/long_addition)|`0+~-~-~-~-~-~-~-~-~-~0`|
|[Numpy long addition](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/numpy_long_addition)|`import numpy as np;x = np.arange(3);x-+~--~+-~~++~+-x;`|
|[Numpy array to array](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/numpy_array_to_array)|`import numpy as np;print(np.zeros(((_:=1),_))[[(((~-_,),),)],(...)])`|
|[Numpy sum](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/numpy_sum)|`import numpy as np;print(sum([sum:=-1],np.sum([sum],sum)))`|
|[Sum trick](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/sum_trick)|`sum(((1,(2,(3),),(4,)),(5,),),())`|
|[Zeros](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/zeros)|`000_0&00^00-0x0_0_00^0o0_00-~0^-0b0_0_0`|
|[To int](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/to_int)|`int("%s_0%%s"%0x0%10)`|
|[Equals](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/equals)|`f"{'='=}={'='=}"`|
|[Method chaining](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/method_chaining)|`().__iter__().__class__.__name__[_:=-2]+[].__class__.__name__[_]`|
|[GeeK split](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/geek_split)|`"g_e_e_k".split(_:="_",_:=len(_))[_].split(_:="_",_:=len(_))[_].split(_:="_")[len(_)]+"p"`|
|[X Face](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/x_face)|`_C:3J /2=3;-~-( _C-8) *["布団"]`|
|[All empty](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/all_empty)|`-~(-~(()==()))`|
|[String of string](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/string_of_string)|`"%%%s%%%%%%%%%%%%ss"%"d"%1%"%"%()%"2"`|
|[Zero to one](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/zero_to_one)|`~1<<1&-~1`|
|[Formula type](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/formula_type)|`O:1+1=2;O`|
|[Append magic](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/append_magic)|`(x:=[[]]*3)[0].append(1);x`|
|[MMM](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/mmm)|`*M,M=[*"123"];"M"+M`|
|[Tuple merge](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/tuple_merge)|`(((0)\|1)\|2)\|3`|
|[I am m3](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/i_am_m3)|`'IAMM3'[(x:=-~(1==1))::x]`|
|[is](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/is)|`...is...is...is...is...is...`|
|[dot](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/dot)|`f"{(':')[::]::^5}"`|
|[map to map](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/map_to_map)|`list(map(list,list(map(map,map(lambda map:list,map:='map'),map))))`|
|[Make parentheses](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/make_parentheses)|`();((((_,_))))`|
|[Percent Equals](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/percent_equals)|`f"{'%s'%'='=}"`|
|[Walrus Default](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/walrus_default)|`(lambda _=(_:=()):_)(_:=())`|
|[Walrus Keyword](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/walrus_keyword)|`((lambda _=(_:=()):_)(_=(_:=())))`|
|[技術書典](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/gijutsushoten)|`f"{chr(len(dir(dir:='技術書典'))-len(dir))}{~(-len(dir))}"`|
|[Pandas Loc](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/pandas_loc)|`import pandas as pd;pd.DataFrame({(_:=f"{':'::^3}"):[(':')[::]]}).loc[::,':':_]`|
|[Dict Minus Zero](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/dict_minus_zero)|`{-.0_0:00_0,00:.0,.0:-0}`|
|[Reduce 5000](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/reduce_5000)|`from functools import reduce;from unicodedata import numeric;reduce(lambda map,numeric:numeric*map,map(numeric,'5000兆'))`|
|[Empty Dict Key](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/empty_dict_key)|`[{(()):([])}[()]]`|
|[Year Slice](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/year_slice)|`"2025"[2:5]*2`|
|[Reduce 5000 Lambda](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/reduce_5000_lambda)|`from functools import reduce;from unicodedata import numeric;reduce(lambda numeric=(reduce:=map), map=(reduce:=numeric):numeric*map, map(numeric,'5000兆'))`|
|[Triple Quote](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/triple_quote)|`"""'"\/\'''"'"""`|
|[Nested F-string](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/nested_fstring)|`f"""{f"{'a'+'b'=}"+f"{'c'+'d'=}"=}"""`|
|[Empty Tuple Key](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/empty_tuple_key)|`{():()}[()]`|
|[None Equals](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/none_equals)|`f"{None=}={None=}"`|
|[Len Ellipsis](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/len_ellipsis)|`f"{len(f'{...=}')=}"`|
|[Dict Key Type Collision](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/dict_key_type_collision)|`{'1':'str', True:'bool', 1:'int', 1.0:'float'}`|
|[Nested Tuple Key](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/nested_tuple_key)|`{((())):(())}[(((())))]`|
|[Enum Hash Collision](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/enum_hash_collision)|`from enum import Enum;class Ex(Enum):int_num=1;bool_num=True;float_num=1.0` ...|
|[Numpy Ones Scalar](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/numpy_ones_scalar)|`import numpy as np;np.ones(())`|
|[Numpy PyCon](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/numpy_pycon)|`import numpy as np;np.__name__[-2:]+np.conj.__name__[:3]`|
|[Numpy Newaxis](https://github.com/m3dev/crazy_programming/tree/main/quiz/python/numpy_newaxis)|`import numpy as np;x=np.ones((2,2));x[(None,...,None)]`|

</details>

<details>

<summary>Ruby Quiz Table</summary>

|title(link)|code|
|---|---|
|[RubyKaigi 2019 Day1-1](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_kaigi_2019)|`!????!:!?!`|
|[RubyKaigi 2019 Day2-1](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_kaigi_2019)|`%%%%%%..%%[0].size[0]`|
|[RubyKaigi 2019 Day2-1](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_kaigi_2019)|`puts=:puts;puts=send(puts,puts)\|\|puts(puts){puts="puts"};puts`|
|[RubyKaigi 2019 Day2-2](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_kaigi_2019)|`%%%%%%%%?????:??`|
|[RubyKaigi 2019 Day2-3](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_kaigi_2019)|`a=0.0/0;a==a?a:irb.quit`|
|[RubyWorldConference2022 day0-1](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`-a=--1.to_s`|
|[RubyWorldConference2022 day0-2](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`[1_1, 1_2, 1_3].map{_2}\|[]`|
|[RubyWorldConference2022 day0-3](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`_=_\|_=__=_\|_=_`|
|[RubyWorldConference2022 day1-1](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`!??[??]`|
|[RubyWorldConference2022 day1-2](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`!%.!..!`|
|[RubyWorldConference2022 day1-3](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`?%%/?%/`|
|[RubyWorldConference2022 day2-1](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`+-+-+-1===-+-+-+1`|
|[RubyWorldConference2022 day2-2](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`().\|(0).!()`|
|[RubyWorldConference2022 day2-3](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/ruby_world_conference_2022)|`(?a..?A).to_a[-2]`|
|[nilキー](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/nil_key)|`{nil:1}[nil]`|
|[pとブロック](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/p_block)|`p {nil: 1}`|
|[tapの戻り値](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/tap_index)|`{}.tap{\|h\|h[1]=1}[1]`|
|[縦棒の群れ](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/bang_question_or)|`!?\|\|\|?\|`|
|[波括弧とクエスチョン](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/question_hash)|`{?}=>?{}[{}]`|
|[宇宙船とハッシュ](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/spaceship_hash)|`{?<=>{}}<=>{?<=>{}}`|
|[pの論理和](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/p_or)|`p\|p\|p`|
|[代入と論理和](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/assign_or)|`a=a\|a=a`|
|[空ハッシュとブロック](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/empty_hash_block)|`{}[{}]{}`|
|[二重否定とクエスチョン](https://github.com/m3dev/crazy_programming/tree/main/quiz/ruby/bang_bang_question)|`!!?[??]`|

</details>

<details>

<summary>Kotlin Quiz Table</summary>

|title(link)|code|
|---|---|
|[data object](https://github.com/m3dev/crazy_programming/tree/main/quiz/kotlin/data_object)|`` data object `・^・`;{`・^・`:`・^・`->(`・^・`)}(`・^・`) ``|

</details>

# We are hiring!!

ギークな学びが大好きな皆さん、エムスリーで一緒に働いてみませんか？

私達のミッションは、インターネットを活用し、健康で楽しく長生きする人を１人でも増やし、不必要な医療コストを１円でも減らすこと。
エンジニアリングの力を活かし、共に医療の課題解決に向かう仲間を募集しています。

## エンジニア採用ページはこちら

[https://jobs.m3.com/engineer/](https://jobs.m3.com/engineer/)

## 新卒採用、インターンも常時募集しています

[https://fresh.m3recruit.com/engineer](https://fresh.m3recruit.com/engineer)

