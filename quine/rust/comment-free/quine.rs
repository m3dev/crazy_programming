fn main(){let payload=P.split_whitespace().collect::<String>();let mut parts=payload.rsplitn(3,'~');
parts.next();let runs=parts.next().unwrap().as_bytes().chunks(2).map(|n|26*usize::from(n[0]-b'A')+  
usize::from(n[1]-b'A'));let template=parts.next().unwrap().replace('\x24',"\x23");let(head,tail)=   
template.rsplit_once('@').unwrap();let source=[head,&payload,tail].concat();let     mut text=source.
chars();               let mut out=String::              new();let mut                 space=false; 
for len in             runs{for _ in 0..len{          out.push(if space{                 '\x20'}else
{text.next().           unwrap()});if out.          len()%101==100{out.     push(         '\n');}}  
space=!space;}            print!("{out}");          }const P:&str=r#"fn   main(){le       tpayload=P
.split_whitespa           ce().collect::<           String>();letmutparts=payload.r       splitn(3,'
~');parts.next(            );letruns=par            ts.next().unwrap().as_bytes().c      hunks(2).ma
p(|n|26*usize::             from(n[0]-b'            A')+usize::from(n[1]-b'A'));le      ttemplate=pa
rts.next().unwr    a         p().replac    e(       '\x24',"\x23");let(head,ta        il)=template.r
split_once('@')    .u        nwrap();l    ets        ource=[head,&payload,ta            il].concat()
;letmuttext=so    urce        .chars(     );l        etmutout=String::new                 ();letmuts
pace=false;for    lenin         runs     {for        _in0..len{out.push(ifspace{'\         x20'}else
{text.next().u    nwrap(         )}     );ifo        ut.len()%101==100{out.push('\n'        );}}spac
e=!space;}prin    t!("{ou        t     }");}c        onstP:&str=r$"@"$;~ACABAKABCAABA       DABBTABD
DACBBABCRADBM    ABBOAFAD             ABAUAPAD        ABADABAMAOAJABADARAMABADABADABA       CANAIABA
BABACABAHAKAL    ABAGARAYA           LANABAEAK        ATAFAFAJAIACAOAMAQAKAGABAMADAJ        AHAZALAP
ALBFAHAZAMANA    MBFAGBAANA         MAMBEAGBBA        EABAJAKAEACAHBAA   IBDAEACAIAJ       AEADAIAXA
MBAAEAEAIAHAF    ADAIAUARAYA       EAFAJAEAFAE        AIBDAJAXAEAGAJA    CAFAFAIBFA       IAWAEAHAIA
BAFAGAIB              GAHAVAE      AIANAIA                 IBFAHAVAEA                   JALAJAIBEAIA
VAEAKAJA              KAIAQADA    LAHAWAEA                 LAHALAIAPAEA              KAHASAOAHAGAHAR
AKATAUAOAIAEAIARAMAOJHABACABADABAGABACABBDABBA~M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M3M
====================================================================================================
========================== We are hiring !! https://jobs.m3.com/engineer/ ======================="#;
