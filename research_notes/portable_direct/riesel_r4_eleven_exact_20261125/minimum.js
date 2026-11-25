
const assert=(v,m)=>{if(!v)throw Error(m);};
const groupMap={"7":[63,126,252],"9":[81,162,324],"12":[432],"14":[504],"15":[135,270,540],"16":[192,576],"18":[648],"20":[80,240,720],"21":[189,378,756],"24":[864],"28":[112,336,1008],"30":[1080],"32":[128,384,1152],"35":[315,630,1260],"36":[1296],"40":[160,480,1440],"48":[1728],"60":[2160],"70":[280,840,2520],"80":[320,960,2880],"140":[560,1680,5040]};
const known={"63":["92737","649657"],"80":["4278255361"],"81":["2593","71119","97685839"],"112":["5153","54410972897"],"126":["77158673929"],"128":["274177"],"135":["271","348031","49971617830801"],"160":["414721","44479210368001"],"162":["163","135433","272010961"],"189":["1560007"],"192":["18446744069414584321"],"240":["394783681","46908728641"],"252":["40388473189","118750098349"],"270":["811","15121","385838642647891"],"280":["84179842077657862011867889681"],"315":["983431","870031","29728307155963706810228435378401"],"320":["3602561"],"324":["3618757","106979941","168410989","4977454861"],"336":["2017","25629623713","1538595959564161"],"378":["379","119827","127391413339","56202143607667"],"384":["769"],"432":["209924353","4261383649","24929060818265360451708193"],"480":["23041"],"504":["1009","21169","2627857","269389009","1475204679190128571777"],"540":["541","166242935471754241","165041853060421","30241","49681"],"560":["4481","557761","736961"],"576":["3457","816769","1562985901350085709953","1422346738975853644793916289"],"630":["1765891","11247702599676505481447137991664348691"],"648":["1297","3889","30433969","1164777409","3718266498433","134921168163073","1174029487714513"],"720":["8369281","750016890283777055704738227247474485366338380663681"],"756":["757","456376431053626339473533320957","304832756195865229284807891468769"],"840":["127681","1130641","755667361","54169520413224311136354324156824071681"],"864":["68016300334849"],"960":["26881","4855681","610548481","137603804161"],"1008":["34273"],"1080":["2161","21601","201519653761","1117180440577441"],"1152":["17047297","628582818817"],"1260":["2521","1711081","430839361","15169173997557864184867895400813639018421","17369459529909057773233442461"],"1296":["10369","259201","1824045366145909775041","524833094849624730914401"],"1440":["37441","170251201","322029272318997936286081"],"1680":["13441","4841172001","1586308510081"],"1728":["1718990209","8148919324033","672915391135935402269916482777538049"],"2160":["6281281","148759201","4518776161","30263419164953868175425499201"],"2520":["1325521","1626833408812908876721","164861463278712334259867127702044401","517496882214135484318298195143896326867475066317761"],"2880":["252581761","40056698881","35884034243486024947201"],"5040":[]};
const sourceCofactorDigits={"128":14,"189":27,"320":32,"384":36,"480":35,"560":43,"864":73,"960":47,"1008":83,"1080":53,"1152":97,"1296":76,"1440":80,"1680":90,"1728":116,"2160":121,"2520":61,"2880":190};
const fixedPrimes=["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const trial=n=>{for(let d=2;d*d<=n;d++)if(n%d===0)return false;return n>1;};
const gcd=(a,b)=>b?gcd(b,a%b):a;
const product=x=>x.reduce((a,b)=>a*b,1n);
function powmod(a,n,m){let r=1n;for(let e=BigInt(n);e;e>>=1n,a=a*a%m)if(e&1n)r=r*a%m;return r;}
function strip(a,b){let d;while((d=gcd(a,b))>1n)a/=d;return a;}
const rowsByOrder={};
for(const [h,ds] of Object.entries(groupMap))for(const d of ds){
 const r=Array.from({length:d},(_,i)=>i+1).filter(p=>!(d%p)&&trial(p));
 let carrier=(1n<<BigInt(d))-1n;
 for(const p of r)carrier=strip(carrier,(1n<<BigInt(d/p))-1n);
 for(const q of fixedPrimes)carrier=strip(carrier,q);
 const factors=known[d].map(BigInt), quotient=carrier/product(factors);
 if(sourceCofactorDigits[d]){
  assert(String(quotient).length===sourceCofactorDigits[d],'table cofactor '+d);
  factors.push(quotient);
 }
 const remaining=carrier/product(factors);
 assert(product(factors)*remaining===carrier&&(d===5040||remaining===1n),'exact product '+d);
 for(const q of factors)assert(q%BigInt(d)===1n&&powmod(2n,d,q)===1n&&r.every(p=>powmod(2n,d/p,q)!==1n),'exact order verification '+d);
 rowsByOrder[d]={h:Number(h),d,carrier,factors,remaining};
}
const support=Object.values(rowsByOrder).flatMap(({h,d,factors})=>factors.map(q=>({h,d,q})));
assert(support.length===142&&new Set(support.map(x=>x.q)).size===142,'142 identified primes');
const unresolved=rowsByOrder[5040].remaining;

const templates=require('./templates.json');

const rows=[0,1,2,3,5];
const compact=[
 ['12:0','12:8'],
 ['20:0','20:8','20:16'],
 ['12:0','24:8','24:20'],
 ['12:8','24:0','24:12'],
 ['16:0','16:4','16:8','16:12'],
 ['20:0','20:8','40:16','40:36'],
 ['20:0','20:16','40:8','40:28'],
 ['20:8','20:16','40:0','40:20'],
 ['7:0','7:1','7:3','7:5','35:23','35:30'],
 ['7:0','7:2','7:3','7:5','35:8','35:15']
];
for(let mask=0;mask<32;mask++){
 const assignment=rows.map((b,i)=>mask>>i&1?'14:'+(b+(b%2)*7):'7:'+b);
 compact.push(assignment.sort((a,b)=>{
   const [h,x]=a.split(':').map(Number),[j,y]=b.split(':').map(Number);
   return h-j||x-y;
 }));
}

const r3a=BigInt("191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163");
const r3s=BigInt("398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390");
const fixedZero=["29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const modulo=(a,m)=>(a%m+m)%m;
const inverse=(a,p)=>powmod(modulo(a,p),p-2n,p);
let a4=r3a,s4=r3s;
for(const p of fixedZero){
 const k=modulo(-a4*inverse(s4,p),p);
 a4+=s4*k;
 s4*=p;
}
assert(a4>0n&&a4<s4&&a4%r3s===r3a&&fixedZero.every(p=>a4%p===0n),'R4 base');

const options={};
for(const key of new Set(templates.flat())){
 const [h,b]=key.split(':').map(Number);
 options[key]=support.filter(x=>x.h===h).map(({q,d})=>{
   const r=powmod(2n,(-16-18*b)%d+d,q), inv=inverse(s4,q);
   return {q, values:[modulo((r-a4)*inv,q),modulo((-r-a4)*inv,q)],key};
 }).sort((a,b)=>a.q<b.q?-1:a.q>b.q?1:0);
}
const isTen=j=>compact.some(t=>t.every(key=>options[key].some(({q,values})=>values.includes(j%q))));
const score=key=>Math.log(Number(options[key][0].q));
const high=templates.filter(t=>t.some(s=>s.startsWith('140:')));
assert(high.length===91&&high.every(t=>t.includes('20:0')&&t.includes('20:8')),'high layer pair');
const terms=templates.filter(t=>!t.some(s=>s.startsWith('140:'))&&!compact.some(a=>a.length===t.length&&a.every(s=>t.includes(s))));
function search(terms,good,reverse){
 let best=null, bestSlots, leaves=0, pruned=0;
 const ts=terms.slice().sort((a,b)=>a.reduce((n,s)=>n+score(s),0)-b.reduce((n,s)=>n+score(s),0));
 if(reverse)ts.reverse();
 for(const term of ts){
  const order=term.slice().sort((a,b)=>score(a)-score(b));
  if(reverse)order.reverse();
  const active=new Set, chosen=[];
  const walk=(j,m,i)=>{
    if(best!==null&&j>=best){pruned++;return;}
    if(i===order.length){
      leaves++;
      for(let x=j;best===null||x<best;x+=m)if(good(x)){best=x;bestSlots=chosen.slice();break;}
      return;
    }
    for(const {q,values,key} of options[order[i]])if(!active.has(q)){
      const inv=inverse(m,q);
      active.add(q);
      for(const value of values){
        chosen.push({q,key,value});
        walk(j+m*modulo((value-j)*inv,q),m*q,i+1);
        chosen.pop();
      }
      active.delete(q);
    }
  };
  walk(0n,1n,0);
 }
 return {best,bestSlots,leaves,pruned};
}
const forward=search(terms,j=>!isTen(j),false);
const backward=search(terms,j=>!isTen(j),true);
const pairBound=search([['20:0','20:8']],()=>true,false);
assert(forward.best===backward.best&&forward.best<pairBound.best,'global minimum including missing layer');
const minimum=a4+s4*forward.best;
const dictionary=[7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417,5,13,19,73,38737,246241,487824887233,541,811,271,209924353].map(BigInt);
function order2(q){let x=2n,d=1;while(x!==1n){x=x*2n%q;d++;}return d;}
const coverPeriod=dictionary.map(order2).reduce((a,b)=>Number(BigInt(a)*BigInt(b)/gcd(BigInt(a),BigInt(b))));
const phase=dictionary.map(q=>(minimum%q)**2n%q);
for(let n=1;n<=coverPeriod;n++){
 let hits=0;
 for(let i=0;i<dictionary.length;i++){
  phase[i]=phase[i]*2n%dictionary[i];
  if(phase[i]===1n)hits++;
 }
 assert(hits>0,'coverage at '+n);
}
const witnessRecords=[[541,2912],[271,2048],[71,1133],[487824887233,2408],[246241,1040],[337,773],[29191,1013],[113,413],[811,320],[1321,257],[673,237],[281,233],[641,207],[19,152],[38737,140],[97,117],[127,113],[6700417,111],[31,89],[257,135],[65537,63],[14449,53],[151,41],[241,33],[209924353,3488],[73,128],[7,16],[13,12],[5,6],[41,5],[17,3]];
const integers=witnessRecords.map(([q,n])=>{
 const f=(minimum*minimum<<BigInt(n))-1n;
 assert(f>BigInt(q)&&f%BigInt(q)===0n&&dictionary.filter(p=>f%p===0n).length===1,'proper private witness');
 return f;
});
let pairChecks=0;
for(let i=1;i<integers.length;i++)for(let j=0;j<i;j++){assert(gcd(integers[i],integers[j])===1n,'coprime pair');pairChecks++;}
const minimumReport={forward,backward,pairBound,minimuma4:a4,step:s4,minimum,digits:String(minimum).length,coverPeriod,dictionary,witnessRecords,pairChecks};

console.log(JSON.stringify(minimumReport,(_,v)=>typeof v==='bigint'?String(v):v,2));
