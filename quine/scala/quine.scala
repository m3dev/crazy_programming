//> using dep org.scala-lang::scala3-compiler // ---------------- We are hiring!! -------------------
import javax.script._; @main def f():Unit={{ // ----------------- @m3_engineering -------------------
ScriptEngineManager().getEngineByName("scala").eval("""import#java.util._;import#java.util.zip._;impo
rt#java.io._;var#s=new#String(Base64.getDecoder.decode("Ly8+IHVzaW5nIGRlcCBvcmcuc2NhbGEtbGFuZzo6c2Nhb
GEzLWNvbXBpbGVyIC8vIC0tLS0tLS0tLS0tLS0tLS0gV2UgYXJlIGhpcmluZyEhIC0tLS0tLS0tLS0tLS0tLS0tLS1pbXBvcnQgam
F2YXguc2NyaXB0Ll          87IEBtYWluIGRlZiBmKCk6          VW5pdD17eyA        vLyAtLS0tLS0tLS0tLS0tLS0
tLSBAbTMjZW5naW5lZXJ       pbmcgLS0tLS0tLS0tLS0t      LS0tLS0tLVNj              cmlwdEVuZ2luZU1hbmFnZ
XIoKS5nZXRFbmdpbmVCeU       5hbWUoInNjYWxhIiku       ZXZhbCgiIiJp  bXBvcnQ      jamF2YS51dGlsLl87aW1w
b3J0I2phdmEudXRpbC56a        XAuXztpbXBvcnQjam        F2YS5pby5fO3ZhciNzPW5      ldyNTdHJpbmcoQmFzZTY
0LmdldERlY29kZXIuZGVj  b     2RlKCIlcyIpKTtzP  X     MuZm9ybWF0KG5ldyNTdHJpb    mcoQmFzZTY0LmdldEVuY2
9kZXIuZW5jb2RlKHMuZ2   V       0Qnl0ZXMoKSkp  KT      twcmludChzY2FsYS5pby5     Tb3VyY2UuZnJvbUlucHV0
U3RyZWFtKG5ldyNJbmZsY  XR       lcklucHV0U3  RyZ      WFtKG5ldyNCeXRlQXJyY    XlJbnB1dFN0cmVhbShCYXNl
NjQuZ2V0RGVjb2Rlci5k  ZWNv      ZGUoImVKen  RsY0      VTaERBSVErLzdOZkQ   vUDdmajdGZ3BUVUoxMVlNanQ1S0
dWNVNxK3czeHVRUHlVdj  ZuV0F      0c2dMcTJ   rRjZV     WjVTc2kza0t4d             0Noclk1U1JvczhNWmNZeG
FHRDVRTUdDdXk5d0llMk  xLdGU1      aW1obkt  Xc29JZ     21TUy90YUZabE53UWhGSl      JVMEdJMkU0NU04cnEzOD
NWSldHdmZqTVhLcTg4Z   0dXS0Fx      Q2tl   S1BXSm      VaOHpGSXVRS3lqZ3NwOUh5       VWFacUNFMVpiQ213VX
Q5UTNxbW9NRWZYdE5QM   3E2UDZ3O     FA2U  1dIdXRXT      kxYYzgrci8vVW9yNEFoRjh     IT1k9IikpKSkuZm9sZE
xlZnQoMCwwLFNlcS5lb   XB0eVtDa      GF  yXSl7Y2Fz      ZSgoaSxkLGMpLCcxJyk9Pi     hpKzEsZCxjOitzLmxpZ
nQoaS1kKS5nZXRPckVs   c2UoJyMnK        Sk7Y2FzZSg      oaSxkLGMpLCcwJyk9PihpK     zEsZCsxLGM6KycjJyk7
Y2FzZSgoaSxkLGMpLCd  cbicpPT4oaS      sxLGQrMSxjO      isnXG4nKTt9KDIpLm1rU3     RyaW5nKTsiIiIucmVwbG
FjZSgiXG4iLCIiKS5yZ  XBsYWNlKCIgI     iwiIikucmVw      bGFjZSg    iIyIsIiAi    KSl9fQ=="));s=s.format
(new#String(Ba           se64.getE   ncoder.e           n  code(   s .g      etBytes())));print(scala
.io.Source.fromInputStream(new#Infl aterInputStream(new#ByteArrayIn     putStream(Base64.getDecoder.d
ecode("eJztlcEShDAIQ+/7NfD/P7fj7FgpTUJ11YMjt5KGV5Sq+w3xuQPyUv6nWAtsgLq2kF6UZ5Ssi3kKxwChrY5SRos8MZcYxa
GD5QMGCuy9wIe2LKte5imhnKWsoIgmSS/taFZlNwQhFJRU0GI2E45M8rq383VJWGvfjMXKq88gGWKAqCkeKPWJeZ8zFIuQKyjgsp9
HyUaZqCE1ZbCmwUt9Q3qmoMEfXtNP3q6P6w8P6SWHutWNLXc8+r//Uor4AhF8HOY=")))).foldLeft(0,0,Seq.empty[Char]){
case((i,d,c),'1')=>(i+1,d,c:+s.lift(i-d).getOrElse('#'));case((i,d,c),'0')=>(i+1,d+1,c:+'#');case((i,
d,c),'\n')=>(i+1,d+1,c:+'\n');}(2).mkString);""".replace("\n","").replace(" ","").replace("#"," "))}}
