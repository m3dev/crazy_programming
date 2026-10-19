fn/**/main(){let/**/payload=P.split_whitespace().collect::<String>();let/**/mut/**/parts=payload./*_
*/rsplitn(3,'~');parts.next();let/**/runs=parts.next().unwrap().as_bytes().chunks(2).map(|n|26*usize
::from(n[0]-b'A')+usize::from(n[1]-b'A'));let/**/template=parts.next().unwrap().replace('\x24',/*_*/
"\x23");let(head,tail)=template.rsplit_once('@').unwrap();let/**/source=[head,/*    */&payload,tail]
.concat();             let/**/mut/**/text=/*_            */source.chars()/*            */;let/**/mut
/**/out=/**/           String::new();let/**/          mut/**/space=false;                for/**//**/
len/**/in/**//*         */runs{for/**/_/**/         in/**/0..len{out./*     */push        (if/**//*_
_*/space{'\x20'           }else{text.next(          ).unwrap()});if/**/   out.len()       %101==100{
out.push('\n');           }}space=!space;           }print!("{out}");}const/**/P:/*       */&str=r#"
fn/**/main(){le            t/**/payload=            P.split_whitespace().collect::<      String>();l
et/**/mut/**/pa             rts=payload.            /*_*/rsplitn(3,'~');parts.next      ();let/**/ru
ns=parts.next()    .         unwrap().a    s_       bytes().chunks(2).map(|n|2        6*usize::from(
n[0]-b'A')+usiz    e:        :from(n[1    ]-b        'A'));let/**/template=p            arts.next().
unwrap().repla    ce('        \x24',/     *_*        /"\x23");let(head,ta                 il)=templa
te.rsplit_once    ('@')         .unw     rap(        );let/**/source=[head,/**/&pa         yload,tai
l].concat();le    t/**/m         ut     /**/t        ext=/*_*/source.chars()/**/;let        /**/mut/
**/out=/**/Str    ing::ne        w     ();let        /**/mut/**/space=false;for/**//*       */len/**
/in/**//**/ru    ns{for/*             */_/**/i        n/**/0..len{out./**/push(if/**/       /*__*/sp
ace{'\x20'}el    se{text.n           ext().unw        rap()});if/**/out.len()%101==1        00{out.p
ush('\n');}}s    pace=!spac         e;}print!(        "{out}");}const/   **/P:/**/&s       tr=r$"@"$
;~OQAEBAANAWA    MASAMAZALAV       AKATAQBAAJA        TAJATAFAGAIAZAL    AQAKATADAJ       AHAZALAPAL
BFAHAZAM              ANAMBFA      GBAANAM                 AMBEAGBBAE                   ABAJAKAEACAH
BAAIBDAE              ACAIAJAE    ADAIAXAM                 BAAEAEAIAHAF              ADAIAUARAYAEAFA
JAEAFAEAIBDAJAXAEAGAJACAFAFAIBFAIAWAEAHAIABAFAGAIBGAHAVAEAIANAIAIBFAHAVAEAJALAJAIBEAIAVAEAKAJAKAIAQA
DALAHAWAEALAHALAIAPAEAKAHASAOAHAGAHARAKATAUAOAIAEAIARAMAOJHABACABADABAGABACABBDABBA~M3M3M3M3M3M3M3M3
========================== We are hiring !! https://jobs.m3.com/engineer/ ======================="#;
