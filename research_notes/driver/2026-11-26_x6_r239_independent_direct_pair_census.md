# X6 R239 independent direct pair census

2026-11-26. Frozen R239 input at 13b49598c381b21e899704d21e8498071c852565:research_notes/portable_direct/2026-11-26_r2_x6_r239_factor_free_reducible_root_xor_capacity.md. Same Port 10, 1935 directions, six BRC, positive weights (17t,B,22t,D), 47 necessary labels, 49 active components, strict 3/2 near set and legal optimizer. Separate implementation of rank-three eventual-sign bank and direct capacity census, preserving author attribution. Each unordered full factor partition pair, including repeated factors, yields an XOR root mask modulo complement. The capacity 31 per depth-five linear child is necessary under the inherited necessary-wall premise. All direct counts and the three R240 residual pair multiplicities match author figures. This does not independently reproduce the R239 second capacity screen or R240 full recursive exclusions. No formal Review or Result acceptance.

Actual output (no cutoff):
```json
{
  "points": 51,
  "germs": 98,
  "linear": 2225,
  "F": 2178,
  "total": 2372931,
  "direct": 2296890,
  "passed": 76041,
  "distinct": 69057,
  "hist": {
    "25": 2,
    "26": 53,
    "27": 341,
    "28": 1987,
    "29": 7391,
    "30": 19768,
    "31": 39515
  },
  "residualMultiplicities": [
    [
      "33cf330384c0033038fffff0",
      1
    ],
    [
      "33cf330384c003303afffff0",
      1
    ],
    [
      "33cf330384c0233038fffff0",
      1
    ]
  ]
}
```

Independent reproducible implementation (data from the above pinned source):
```js
function directAudit(data){
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n), cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sign=x=>x>0n?1:x<0n?-1:0, gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,pr=v=>{let g=v.reduce(gcd,0n);return g?v.map(x=>x/g):v},canon=(a,b)=>a<b?a:b;
 let pts=[],ids=new Map(),germs=[],tags=[],starts=[],dups=[];function id(v){v=pr(v.map(BigInt));let k=v.join();if(!ids.has(k)){ids.set(k,pts.length);pts.push(v)}return ids.get(k)}
 for(let d of data){let parts=d.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:d.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[d.endpoints];let t=0n,ss=0n;for(let [a,b] of parts){let x=id(a),y=id(b),i=BigInt(germs.length);if(x===y||dot(pts[x],d.normal.map(BigInt))||dot(pts[y],d.normal.map(BigInt)))throw Error("wall");germs.push([x,y],[y,x]);t|=3n<<i;ss|=1n<<i;starts.push(1n<<i)}tags.push(t);if(parts.length===2)dups.push(ss)}
 const U=(1n<<BigInt(germs.length))-1n,even=starts.reduce((a,b)=>a|b,0n),bits=germs.map((_,i)=>1n<<BigInt(i));
 let bank=new Map();function put(z){let p=0n,q=0n;for(let i=0;i<germs.length;i++){let [a,b]=germs[i],v=z[a]||z[b];if(v>0)p|=bits[i];else if(v<0)q|=bits[i]}if(p>q)[p,q]=[q,p];bank.set(p+","+q,[p,q])}
 let rays=new Map();for(let i=0;i<pts.length;i++)for(let j=0;j<i;j++){let v=pr(cross(pts[i],pts[j]));if(v.every(x=>!x))continue;if(v.find(x=>x)<0n)v=v.map(x=>-x);rays.set(v.join(),v)}
 for(let v of rays.values()){let z=pts.map(p=>sign(dot(v,p)));put(z);for(let i=0;i<pts.length;i++)if(!z[i]){let w=cross(v,pts[i]),s=pts.map(p=>sign(dot(w,p))),t=pts.map(p=>sign(dot(pts[i],p)));for(let a of [-1,1]){put(z.map((x,j)=>x||a*s[j]));for(let b of [-1,1])put(z.map((x,j)=>x||a*s[j]||b*t[j]))}}}
 const pc32=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return ((((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24)};
 function count(s){let a=(s|s>>1n)&even;let n=pc32(Number(a&0xffffffffn))+pc32(Number(a>>32n&0xffffffffn))+pc32(Number(a>>64n&0xffffffffn))+pc32(Number(a>>96n));for(let d of dups)if((a&d)===d)n--;return n}
 for(let [a,b] of bank.values())for(let s of [a,b,a|b])if(count(s)!==tags.filter(t=>s&t).length)throw Error("count");
 const F=[...bank.values()].filter(([a,b])=>(a|b)===U).map(([a])=>a);
 let total=0,direct=0,pass=new Map(),hist={};for(let i=0;i<F.length;i++)for(let j=0;j<=i;j++){total++;let a=F[i]^F[j],b=U^a,x=count(a);if(x>31){direct++;continue}let y=count(b);if(y>31){direct++;continue}let k=canon(a,b);pass.set(k,(pass.get(k)||0)+1)}
 for(let a of pass.keys()){let c=Math.max(count(a),count(U^a));hist[c]=(hist[c]||0)+1}
 const targets=["33cf330384c0033038fffff0","33cf330384c003303afffff0","33cf330384c0233038fffff0"];
 return {points:pts.length,germs:germs.length,linear:bank.size,F:F.length,total,direct,passed:total-direct,distinct:pass.size,hist,residualMultiplicities:targets.map(x=>[x,pass.get(BigInt("0x"+x))])};
}
```
