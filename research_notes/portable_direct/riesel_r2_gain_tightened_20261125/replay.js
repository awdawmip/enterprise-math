"use strict";
// Node.js standard BigInt; no dependencies.
const A2=9807947978443488306255509703402695727949968778703073231931137913705883712843n;
const S2=11356718000553566643685496313583434507970452519839503606327232707476034989690n;
const H=new Set([1,2,3,4,5,6,7,8,9,10,12,15,16,20,35]), F=new Set([7,10,14,28,35,70]);
function gcd(a,b){while(b)[a,b]=[b,a%b];return a<0n?-a:a}
function strip(a,b){let g;while((g=gcd(a,b))>1n)a/=g;return a}
function prod(xs){let v=1n;for(const x of xs)v*=x;return v}
function pf(d){const r=[];for(let p=2;p*p<=d;p++)if(d%p===0){r.push(p);while(d%p===0)d/=p;}if(d>1)r.push(d);return r;}
function gcdNum(a,b){return Number(gcd(BigInt(a),BigInt(b)))}
function pow(a,b,n){let r=1n;for(a%=n;b;b>>=1n){if(b&1n)r=r*a%n;a=a*a%n;}return r;}
const rows=[];
for(let d=1;d<=1260;d++){const h=d/gcdNum(d,36),f=d/gcdNum(d,12);if(!H.has(h)&&!F.has(f))continue;const c=strip(strip((1n<<BigInt(d))-1n,prod(pf(d).map(p=>(1n<<BigInt(d/p))-1n))),S2);if(c>1n)rows.push({d,f,h,c});}
function order(q){for(let d=1;d<=1260;d++)if(pow(2n,BigInt(d),q)===1n)return d;throw new Error("order");}
const pinned=["577","487824887233","181","631","23311","54001","18837001","29247661","87211","246241","262657","279073","29","43","1429","5419","3361","15790321","88959882481","211","421","86171","106681","122921","152041","664441","1564921","7416361","47392381","146919792181","1041815865690181","193","1153","6337","22253377","38941695937","278452876033","33975937","138991501037953","61681","4562284561","168692292721","469775495062434961","92737","649657","40388473189","77158673929","118750098349","209924353","4261383649","24929060818265360451708193","8369281","394783681","4278255361","46908728641","750016890283777055704738227247474485366338380663681","3457","816769","18446744069414584321","1562985901350085709953","1422346738975853644793916289","2017","5153","25629623713","54410972897","1538595959564161","127681","1130641","755667361","84179842077657862011867889681","54169520413224311136354324156824071681","983431","870031","29728307155963706810228435378401","1765891","11247702599676505481447137991664348691","2521","1711081","430839361","163","2593","71119","271","541","811","166242935471754241","165041853060421"].map(BigInt);
const unknown=263480353852730122330752072139697321699158754520077217531258822574081n;
const B=10000000000n, S=100000n;
let unkK=0,t=1n;while((t*=B+1n)<=unknown)unkK++;
if(unkK!==6||pow(3n,unknown-1n,unknown)===1n)throw Error("unknown certificate");

for(let q=1261n;q<=B;q+=1260n)if(unknown%q===0n)throw Error("small order-1260 factor");
function primeSmall(n){if(n<2n)return false;for(let p=2n;p*p<=n;p++)if(n%p===0n)return false;return true;}
function pair(n,d=1n){const g=gcd(n,d);return [n/g,d/g];}
function times(a,b){return pair(a[0]*b[0],a[1]*b[1]);}
function sub(a,b){return pair(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}
function show(a,k=45){const sign=a[0]<0n?"-":"";const n=a[0]<0n?-a[0]:a[0];const d=a[1];return {num:String(a[0]),den:String(d),floor_decimal:sign+String(n/d)+"."+String((n%d)*10n**BigInt(k)/d).padStart(k,"0")};}
function coverMask(qs,k,restricted) {
  const w=Array(1<<k).fill(0n);w[0]=1n;
  for(const p of qs){
    const v=Array(1<<k).fill(0n);
    for(let m=0;m<w.length;m++){
       v[m]+=w[m]*(p.q-2n*BigInt(restricted?p.f:k));
       for(let b=0;b<k;b++)v[m|1<<b]+=2n*w[m];
    }
    for(let m=0;m<w.length;m++)w[m]=v[m];
  }
  return w;
}
const allPinned=prod(pinned);
const C=[],G=[],TOP=[],rest=[],remainders=[];
for(const r of rows){
 let n=strip(r.c,allPinned);
 const factors=pinned.filter(q=>r.c%q===0n);
 if(r.d!==1260){
   for(let p=2n;p<=S&&p*p<=n;p++)if(n%p===0n){if(!primeSmall(p))throw Error("trial ordering");factors.push(p);n=strip(n,p);}
   if(n>1n&&n<=S*S){if(!primeSmall(n))throw Error("prime");factors.push(n);n=1n;}
 }
 const group=r.h===5?C:r.d===1260?TOP:r.h===35||r.h===7?G:rest;
 for(const q of factors){if(order(q)!==r.d)throw Error("wrong order");group.push({q,f:r.f,d:r.d});}
 if(n!==1n)remainders.push({d:r.d,f:r.f,n});
}
if(C.length!==6||G.length!==26||TOP.length!==3)throw Error("group counts "+[C.length,G.length,TOP.length]);
if(remainders.find(x=>x.d===1260)?.n!==unknown)throw Error("changed remainder");
if(remainders.some(x=>x.d!==1260&&(x.f===15||[7,21,35,105].includes(x.f))))throw Error("unresolved in geometry");

const L=1000000000n;
const found=[],tested=[];
for(const r of remainders.filter(x=>x.d!==1260)){
 if(pow(2n,BigInt(r.d),r.n)!==1n)throw Error("residual order divisor");
 let n=r.n,count=0;
 for(let q=BigInt(r.d)+1n;q<=L && q*q<=n;q+=BigInt(r.d)){
   count++;
   if(n%q!==0n)continue;
   if(!primeSmall(q)||order(q)!==r.d)throw Error("discovered factor");
   rest.push({q,f:r.f,d:r.d});
   found.push({q:String(q),d:r.d,f:r.f});
   n=strip(n,q);
 }
 if(n>1n&&n<=L){if(!primeSmall(n)||order(n)!==r.d)throw Error("remaining prime");rest.push({q:n,f:r.f,d:r.d});found.push({q:String(n),d:r.d,f:r.f});n=1n;}
 if(n>1n&&BigInt(r.d)*(BigInt(count)+1n)+1n<=L){
   if(n>L*L)throw Error("trial ended too early");
   // Early termination at sqrt(n) proves the remainder prime.
   if(order(n)!==r.d)throw Error("remaining prime order");
   rest.push({q:n,f:r.f,d:r.d});found.push({q:String(n),d:r.d,f:r.f});
   n=1n;
 }
 r.n=n;
 tested.push({d:r.d,candidates:count,residue:String(n)});
}

const TOPRemainders=remainders.filter(x=>x.d===1260);
const knownDen=prod([...C,...G,...TOP,...rest].map(z=>z.q));
let extraSafe=[1n,1n];
const remainderDetails=[];
for(const x of remainders.filter(x=>x.d!==1260)){
 let n=0,v=L+1n;for(;v<=x.n;v*=L+1n)n++;
 extraSafe=times(extraSafe,pair(L+1n-2n*BigInt(n),L+1n));
 remainderDetails.push({d:x.d,f:x.f,count:n});
}
const wc=coverMask(C.map(p=>({...p,q:p.q-2n})),2,false)[3];
const lp=coverMask(G,3,false), hp=coverMask(TOP,3,false);
const geometry=Array(8).fill(0n);
for(let m=1;m<8;m++)for(let l=0;l<8;l++)for(let h=0;h<8;h++)
 if((l|h)===7&&(l&m)===0)geometry[m]+=wc*lp[l]*hp[h];
function witnessUnion(shifts,offsets=[0,0,0]){
 const initial=[170,80,200];
 const pts=initial.flatMap((v,cell)=>shifts.map(shift=>({v:v+210*(shift+offsets[cell]),cell})));
 if(pts.length>21)throw Error("too many IE terms");
 const steps=Array.from(new Set(rest.map(r=>r.f))).map(f=>{
   const index=new Map(pts.map(({v})=>v%f).map((v,i)=>[v,i]));
   const bit=pts.map(({v})=>1<<index.get(v%f));
   const table=Array.from({length:index.size+1},(_,k)=>prod(rest.filter(z=>z.f===f).map(z=>z.q-2n*BigInt(k))));
   return {bit,table};
 });
 const cell=Array.from({length:1<<pts.length},()=>0), sign=new Int8Array(1<<pts.length);sign[0]=-1;
 let sum=0n;
 const masks=steps.map(()=>new Int32Array(1<<pts.length));
 const count=m=>{let k=0;while(m){m&=m-1;k++;}return k};
 for(let m=1;m<1<<pts.length;m++){
   const prev=m&(m-1), k=31-Math.clz32(m^prev);
   cell[m]=cell[prev]|1<<pts[k].cell;sign[m]=-sign[prev];
   let n=geometry[cell[m]];
   for(let j=0;j<steps.length;j++){
    const state=masks[j][m]=masks[j][prev]|steps[j].bit[k];
    n*=steps[j].table[count(state)];
   }
   sum+=BigInt(sign[m])*n;
 }
 const known=pair(sum,knownDen), lower=times(known,extraSafe);
 return {shifts,offsets,pts:pts.map(z=>z.v),terms:(1<<pts.length)-1,known:show(known),lower:show(lower)};
}
const geometryUpper=(()=>{
 const list=[...TOP,...Array.from({length:unkK},()=>({q:B+1n,f:105,d:1260}))];
 const c=coverMask(C,2,false), l=coverMask(G,3,false), h=coverMask(list,3,false);
 let n=0n;
 for(let i=0;i<7;i++)for(let j=0;j<8;j++)if((i|j)===7)n+=l[i]*h[j];
 return pair(c[3]*n,prod([...C,...G,...list].map(z=>z.q)));
})();

function byIndependentMaskDP(shifts){
 const pts=[170,80,200].flatMap((v,cell)=>shifts.map(k=>({v:v+210*k,cell})));
 const size=1<<pts.length;
 let w=Array(size).fill(0n);
 w[0]=1n;
 for(const p of rest){
   const classes=new Map();
   for(let i=0;i<pts.length;i++){
     const v=pts[i].v%p.f;
     classes.set(v,(classes.get(v)??0)|1<<i);
   }
   const weights=Array(size).fill(0n);
   for(let m=0;m<size;m++){
     if(w[m]===0n)continue;
     weights[m]+=w[m]*(p.q-2n*BigInt(classes.size));
     for(const k of classes.values())weights[m|k]+=w[m]*2n;
   }
   w=weights;
 }
 let answer=0n;
 for(let l=0;l<8;l++)for(let h=0;h<8;h++){
   if((l|h)!==7||l===7)continue;
   let candidate=0;
   for(let i=0;i<pts.length;i++)if(!(l&(1<<pts[i].cell)))candidate|=1<<i;
   let weight=0n;
   for(let m=0;m<size;m++)if(candidate&~m)weight+=w[m];
   answer+=wc*lp[l]*hp[h]*weight;
 }
 return show(pair(answer,knownDen));
}const small=[1,2,3].map(n=>Array.from({length:n},(_,i)=>i));
for(const shifts of small){
 const x=witnessUnion(shifts).known, y=byIndependentMaskDP(shifts);
 if(x.num!==y.num||x.den!==y.den)throw Error("independent weighting disagrees");
}
const large=witnessUnion([0,1,2,3,4,5,6]);

function occupied(qs,k){
 let n=0n;const bin=k===2?[1n,2n,1n]:[1n,3n,3n,1n];
 for(let j=0;j<=k;j++)n+=(j%2?-1n:1n)*bin[j]*prod(qs.map(p=>p.q-2n*BigInt(j)));
 return pair(n,prod(qs.map(q=>q.q)));
}
function topEvent(top){
 const p=occupied([...G,...top],3), l=occupied(G,3), c=occupied(C,2);
 const none=pair(prod(top.map(x=>x.q-6n)),prod(top.map(x=>x.q)));
 return times(c,sub(p,times(l,none)));
}
const TLo=topEvent(TOP), THi=topEvent([...TOP,...Array.from({length:unkK},()=>({q:B+1n,f:105,d:1260}))]);
const gainLower=pair(BigInt(large.lower.num),BigInt(large.lower.den));
const divide=(a,b)=>pair(a[0]*b[1],a[1]*b[0]);
const ratioLower=divide(gainLower,THi), ratioUpper=divide(geometryUpper,TLo);
const intervalWidth=sub(geometryUpper,gainLower);

if(large.lower.floor_decimal.slice(0,24)!=="0.0000000016755028689053".slice(0,24))throw Error("gain endpoint mismatch");

const lowOrders=rows.filter(r=>r.d<=840).map(r=>{
 const factors=[...C,...G,...rest].filter(x=>x.d===r.d).map(x=>x.q);
 if(factors.length===0||strip(r.c,prod(factors))!==1n)throw Error("low order inventory incomplete");
 return {d:r.d,f:r.f,carrier:String(r.c),primeFactors:factors.map(String)};
});
const lowPrimeCount=lowOrders.reduce((s,x)=>s+x.primeFactors.length,0);
if(lowPrimeCount!==97||new Set(lowOrders.flatMap(x=>x.primeFactors)).size!==97)throw Error("low distinctness");
if(lowOrders.some(r=>prod(r.primeFactors.map(BigInt))!==BigInt(r.carrier)))throw Error("low product");
function kthFloor(n,k){
 let lo=1n,hi=1n<<BigInt(Math.ceil(n.toString(2).length/Number(k)));
 while(lo<hi){const m=(lo+hi+1n)>>1n;if(m**k<=n)lo=m;else hi=m-1n;}return lo;
}
const highPowerCertificate=[];
for(let k=2n;k<=6n;k++){const y=kthFloor(unknown,k);if(y**k===unknown)throw Error("residual is a power");highPowerCertificate.push({e:Number(k),floor:String(y)});}
if(gcd(unknown,prod(TOP.map(x=>x.q)))!==1n)throw Error("top repeated");
const necessarySupport={R2:[lowPrimeCount+TOP.length+2,lowPrimeCount+TOP.length+unkK],R1:[lowPrimeCount+TOP.length+4,lowPrimeCount+TOP.length+unkK+2]};
if(remainderDetails.some(x=>x.count!==0)||extraSafe[0]!==extraSafe[1])throw Error("unexpected unresolved low order factor");
console.log(JSON.stringify({lowPrimeCount,lowOrders,large,found,tested,extraSafe:show(extraSafe),remainders:remainderDetails,upper:show(geometryUpper),
 TLo:show(TLo),THi:show(THi),ratioLower:show(ratioLower),ratioUpper:show(ratioUpper),intervalWidth:show(intervalWidth),independentMaskDPs:small.length,highPowerCertificate,necessarySupport},null,2));
