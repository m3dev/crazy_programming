import Foundation;typealias S=String;var f={(s:S)in s.filter{!($0=="\n"||$0==" ")}},z={(i:Int) in S(
repeating:"0",count:i)},a=[S](),b={(s:S)in z(8-s.count)+s},w={(t:S)in t.map{ $0=="0" ? a.popLast()!:
" "}.joined()},d={(s:S)in Data(base64Encoded:S(f(s).prefix(max(/*iOSDC*/2025,9/19-21))))!};var s="""
aW1wb3J0IEZvdW5kYXRpb247dHlwZWFsaWFzIFM9U3RyaW5nO3ZhciBmPXsoczpTKWluIHMuZmlsdGVy    eyEoJDA9PSJcbiJ8
fCQwPT0iIC             IpfX0sej17KGk6SW50KSBp             biBTKApyZXBlYXRpb            mc6IjAiLGNvdW
50OmkpfSxhPV t         TXSgpLGI9eyhzOlMpaW4g            eig4LXMuY291bnQpK                3N9LHc9eyh0
OlMpaW4gdC5tYXB         7ICQwPT0iMCIgPyBhLn         BvcExhc3QoKSE6CiIgI                   n0uam9pbmV
kKCl9LGQ9eyhzOl           MpaW4gRGF0YShiYX          NlNjRFbmNvZGVkOlMoZ   ihzKS5wcm       VmaXgobWF4
KC8qaU9TREMqLzI           wMjUsOS8xOS0yMS            kpKSkhfTt2YXIgcz0iIiIKJUAKIiIi       LHI9cy5zcG
xpdChzZXBhcmF0b            3I6IjoiKS5tYX            B7UygkMCl9O2E9Uyhmb3JtYXQ6UyhkY       XRhOmQocls
wXSksZW5jb2Rpbm             c6LnV0ZjgpIS             5maWx0ZXJ7ISgkMD09IlxuIgopfSx       mKHMpKS5tYX
B7UygkMCl9LnJl     d         mVyc2VkKCk    7c        z13KGQoclsxXSkubWFwe2IoUygk       MCxyYWRpeDoyK
Sl9LmpvaW5lZCgp    K3        ooMHgyOCk    pO2        ZvciBpIGluKDAuLjwyOCl7             CnByaW50KHMu
ZHJvcEZpcnN0KG    kqMT        AwKS5wc     mVm        aXgoMTAwKSl9Ly89PT09                 PT09PT09PT
09PT09PSBpT1NE    QyBUb         2tlb     iBpc         yAjam9pbl9tMyA9PT09P  T09PT0          9PT09PT0
9PT0KLy89PT09P    T0gbGV         0I     HdlX2        FyZV9oaXJpbmcgPSBVUkxSZXF1ZXN0K        HVybDogV
VJMKHN0cmluZzo    iaHR0cH        M     6Ly9qb2        JzLm0zLmNvbS9lbmdpbmVlci8iKSEpI       D09PT09P
T0vLw==:AAAAA     AAAAAAA             AAAAAAA         AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA         AAAAAAA
AAAAAAAPAAAAP     /4AAAf/w           AAf/gAAA         L/gAAD/8AAH//gAAAH/AAAf8AAB///        AAAAf/AA
D/wAAHAH8AAAB     /8AAf/gAA         AAfwAAAH/4        AD/8AAAAB/AAAAf/w  AP/4AAAAP4A       AAD7/gB5/
gAAAD+AAAAHn+    APH+AAAH/8A       AAA8P8B8f4A        AB//8AAADwf8Ph/    wAADA/8AAA       PA/58H+AAA
AA/wAAA8  B        /  vgP8AAA      AB/AAAH w            H  /8B/wAAAAP                   +AAAfAP/gH/A
AAAA/wA               AB8Af8AP    8AAGAD+A                 AAHgA/gA/wAB              4AfwAAN/sB+Av/2
AH//8AAB//wDwD//4AH/+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
""",r=s.split(separator:":").map{S($0)};a=S(format:S(data:d(r[0]),encoding:.utf8)!.filter{!($0=="\n"
)},f(s)).map{S($0)}.reversed();s=w(d(r[1]).map{b(S($0,radix:2))}.joined()+z(0x28));for i in(0..<28){
print(s.dropFirst(i*100).prefix(100))}// Find this Quine at:https://www.m3tech.blog/entry/iosdc-2025
//====== let we_are_hiring = URLRequest(url: URL(string:"https://jobs.m3.com/engineer/")!) =======//
