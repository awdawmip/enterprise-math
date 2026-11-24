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
function pExtreme(top,restricted,event){
 const wc=coverMask(C,2,restricted),lo=coverMask(G,3,restricted),hi=coverMask(top,3,restricted);
 let n=0n;
 for(let l=0;l<8;l++)for(let h=0;h<8;h++)if((l|h)===7&&(event==="T"?h!==0:l!==7))n+=lo[l]*hi[h];
 return pair(wc[3]*n,prod([...C,...G,...top].map(p=>p.q)));
}
function allOccupied(qs,k){
 let n=0n;
 for(let j=0;j<=k;j++){
   const c=k===2?[1n,2n,1n][j]:[1n,3n,3n,1n][j];
   n+=(j%2?-1n:1n)*c*prod(qs.map(p=>p.q-2n*BigInt(j)));
 }
 return pair(n,prod(qs.map(p=>p.q)));
}
const unknownFill=Array.from({length:unkK},()=>({q:B+1n,f:105,d:1260}));
const t0=pExtreme(TOP,false,"T"),t1=pExtreme([...TOP,...unknownFill],false,"T"),
      d0=pExtreme(TOP,false,"D"),d1=pExtreme([...TOP,...unknownFill],false,"D");
for(const top of [TOP,[...TOP,...unknownFill]]){
  const p=allOccupied([...G,...top],3),l=allOccupied(G,3),c=allOccupied(C,2);
  const nohi=pair(prod(top.map(x=>x.q-6n)),prod(top.map(x=>x.q)));
  if(sub(times(c,sub(p,times(l,nohi))),pExtreme(top,false,"T"))[0]!==0n)throw Error("T IC");
  if(sub(times(c,sub(p,l)),pExtreme(top,false,"D"))[0]!==0n)throw Error("D IC");
}
const g0only=pExtreme(TOP,true,"D");
let inactive=pair(1n);
for(const p of rest)inactive=times(inactive,pair(p.q-2n*BigInt(p.f),p.q));
const inf=[];
for(const x of remainders){
 const b=x.d===1260?B:S;
 let k=0,p=1n;while((p*=b+1n)<=x.n)k++;
 inactive=times(inactive,pair(b+1n-2n*BigInt(k*x.f),b+1n));
 inf.push({d:x.d,f:x.f,remainder:String(x.n),factor_lower_bound:String(b+1n),distinct_at_most:k});
}
const gainLo=times(inactive,g0only);
if(gainLo[0]<=0n||sub(d1,gainLo)[0]<0n||sub(t1,t0)[0]<0n)throw Error("interval");

const pts=[21,26,31].map(w=>2+3*(w%2===0?w:w+35)); // three even w lifts
const bits=m=>[0,1,2].filter(i=>m&(1<<i));
const lp=coverMask(G,3,false), hp=coverMask(TOP,3,false);
const base=prod([...C,...G,...TOP].map(p=>p.q));
let bonLo=pair(0n),bonHi=pair(0n);
const terms=[];
for(let s=1;s<8;s++){
  const ix=bits(s);
  // Each C prime must avoid the short column (one phase mod15).
  const wc=coverMask(C.map(p=>({...p,q:p.q-2n})),2,false);
  let n=0n;
  for(let l=0;l<8;l++)for(let h=0;h<8;h++)
      if((l|h)===7&&(l&s)===0)n+=lp[l]*hp[h];
  let un=pair(wc[3]*n,base);
  for(const p of rest){
      const k=new Set(ix.map(i=>pts[i]%p.f)).size;
      un=times(un,pair(p.q-2n*BigInt(k),p.q));
  }
  let bound=un;
  for(const x of inf)if(x.d!==1260){
      const k=new Set(ix.map(i=>pts[i]%x.f)).size;
      const b=BigInt(x.factor_lower_bound);
      bound=times(bound,pair(b-2n*BigInt(k*x.distinct_at_most),b));
  }
  if(ix.length%2){bonLo=sub(bonLo,pair(-bound[0],bound[1]));bonHi=sub(bonHi,pair(-un[0],un[1]));}
  else{bonLo=sub(bonLo,un);bonHi=sub(bonHi,bound);}
  terms.push({s,lower:show(bound),upper:show(un)});
}
if(sub(bonLo,gainLo)[0]<=0n||sub(d1,bonLo)[0]<0n||sub(bonHi,bonLo)[0]<0n)throw Error("Bonferroni");
const result={gain_fraction_upper:show(pair(d1[0]*t0[1],d1[1]*t0[0])),even_v_points:pts,terms,strong_gain_lower:show(bonLo),strong_gain_fraction_lower:show(pair(bonLo[0]*t1[1],bonLo[1]*t1[0])),sizes:[C.length,G.length,TOP.length,rest.length],scan_cutoff:String(B),orders:rows.length,unresolved:inf,
 T_lower:show(t0),T_upper:show(t1),T_width:show(sub(t1,t0),50),T_optional_same_geometry_upper:show(sub(t1,d0)), D_lower:show(d0),D_upper:show(d1),
 extra_inactivity_lower:show(inactive),gain_lower:show(gainLo),gain_upper:show(d1),gain_over_T_lower:show(pair(gainLo[0]*t1[1],gainLo[1]*t1[0]))};

console.log(JSON.stringify(result,null,2));
