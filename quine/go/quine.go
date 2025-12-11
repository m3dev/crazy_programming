package main;import(b"encoding/base64";f"fmt";s"strings");func main() {r:=s.ReplaceAll(s.ReplaceAll(
p," ",""),"\n","");u:=s.SplitN(r,"::M3::",2);d:=b.StdEncoding.DecodeString;t,_:=d(u[0]);m,_:=d(u[1])
;q:=f.Sprintf(string(t),r);i:=0;for n:=0;n<2600;n++{if n>0&&n%100==0{f.Println()}; x:=m[n/8];b:=(x>>
(7-uint(n%8)))&1;if b==1{f.Print(" ")}else{f.Printf("%c",q[i]);i++}};f.Println();};const p=`cGFja2Fn
ZSBtYWluO2             ltcG9ydChiImVuY29kaW5n            L2Jhc2U2NCI7ZiJmbX            QiO3Mic3RyaW5
ncyIpO2Z1bmM           gbWFpbigpIHtyOj1zLlJl          cGxhY2VBbGwocy5SZXB                sYWNlQWxsKH
AsIiAiLCIiKSwiX         G4iLCIiKTt1Oj1zLlNw         bGl0TihyLCI6Ok0zOjo     iLDIpO        2Q6PWIuU3R
kRW5jb2RpbmcuRG           Vjb2RlU3RyaW5nO3          QsXzo9ZCh1WzBdKTttL   F86PWQodV       sxXSk7cTo9
Zi5TcHJpbnRmKHN           0cmluZyh0KSxyKT           tpOj0wO2ZvciBuOj0wO248MjYwMDtuK       yt7aWYgbj4
wJiZuJSUxMDA9PT            B7Zi5QcmludGx            uKCl9OyB4Oj1tW24vOF07Yjo9KHg+Pi      g3LXVpbnQob
iUlOCkpKSYxO2lm             IGI9PTF7Zi5Q            cmludCgiICIpfWVsc2V7Zi5QcmludG      YoIiUlYyIscV
tpXSk7aSsrfX07Z    i         5QcmludGxu    KC       k7fTtjb25zdCBwPWAlc2AgICAg        ICAgICAgICAgIC
AgICAgICAgICAgI    CA        gICAgICAg    ICA        gICAgICAgICAgICAgICAgIC            AgICAgICAgIC
AgICAgICAgICAg    ICAg        ICAgICA     gIC        AgICAgICAgICAgICAgIC                 AgICAgICAg
ICAgICAgICAgIC    AgICA         gICA     gICA        gICAgICAgICAgICAgICAgICAgICAg         ICAgICAgI
CAgICAgICAgICA    gICAgI         CA     gICAg        ICAgICAgICAgICAgICAgICAgICAgICA        gICAgICA
gICAgICAgICAgI    CAgICAg        I     CAgICA        gICAgICAgICAgICAgICA=::M3::AAAAA       AAAAAAAA
AAAAAAAAAAAAA    AAAAAAAA             AAAAAAAA        AAAAAAAAAAAAAAAAAAAAAAAAAAP/4AA       Af/gAAf/
gAAAP/gAAD/wA    AH//gAAAH           /AAAf8AAB        8D/AAAAf/AAD/wAAHAH8AAAB/8AAf/        AAAAAfwA
AAH/4AD/8AAAA    B+AAAAf/wA         P/wAAAAPwA        AAB7/gB5/AAAAP8A   AAAHn+APH+A       AAD/8AAAA
8P8B8f4AAB//8    AAADwf8Ph/g       AAAA/4AAAPA        /58H+AAAAA/wAAA    8B/vgf4AAA       AB/AAAHgH/
8A/wAAAA              H8AAAeA      P/gD/AA                 AAA/wAAB4A                   f8AP8AAOAD+A
AAHgA/gA              /wAB4Afw    AAP/8B+A                 //+AH//8AAA/              /wDwD//4AH/+AAA
AAAAAAAAAAAAAAAAAAAAAABIgSAAAAAAAAAAAAIAAAAIAAAAAA==M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3
========================================= We are hiring !! =========================================
================================== https://jobs.m3.com/engineer/ ==================================`