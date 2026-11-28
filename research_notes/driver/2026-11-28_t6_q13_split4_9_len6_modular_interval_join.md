# T6 q13 split(4,9), negative length 6 — exact modular interval join

Informed continuation of saved Driver research. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; same basis and proof as 0f5415ae2ef3e91852500912e71549b2e6285a51:research_notes/driver/2026-11-28_t6_q13_split4_9_len1to3_modular_interval_join.md. Exact source program below is the read-back predecessor with filter changed to equality (only length 6). All positive partitions of 4, all negative partitions of 9 with exactly six atoms, relaxed model including common atoms. Every surviving vector was reconstructed and checked in six original congruences and both mass budgets; rejection ledger checked per row. No formal acceptance or author-certificate field comparison; not a clean independent review of own method.

## Executed data
```json
{
  "rows": [
    {
      "pos_pattern": [
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 71547840,
      "search": 71194305,
      "index_pass": 18266553,
      "box_survivors": 235,
      "valid": 0,
      "rejects": [
        52927752,
        13344239,
        3519122,
        948159,
        299057,
        102893,
        33521,
        12745,
        4244,
        1399,
        615,
        324
      ],
      "minMaxBudgetExcess": 1354
    },
    {
      "pos_pattern": [
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 49061376,
      "search": 48818952,
      "index_pass": 13165495,
      "box_survivors": 263,
      "valid": 0,
      "rejects": [
        35653457,
        9442839,
        2608437,
        735674,
        244819,
        86087,
        29588,
        11003,
        4278,
        1583,
        556,
        368
      ],
      "minMaxBudgetExcess": 913
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 7547904,
      "search": 7510608,
      "index_pass": 2123462,
      "box_survivors": 74,
      "valid": 0,
      "rejects": [
        5387146,
        1494538,
        432630,
        127079,
        43581,
        16052,
        5879,
        2154,
        927,
        362,
        114,
        72
      ],
      "minMaxBudgetExcess": 1377
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 4088448,
      "search": 4068246,
      "index_pass": 1151760,
      "box_survivors": 43,
      "valid": 0,
      "rejects": [
        2916486,
        809755,
        234943,
        68622,
        24191,
        8898,
        3237,
        1199,
        527,
        205,
        91,
        49
      ],
      "minMaxBudgetExcess": 2132
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        1,
        4
      ],
      "raw": 628992,
      "search": 625884,
      "index_pass": 185217,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        440667,
        127866,
        38564,
        11914,
        4242,
        1574,
        664,
        220,
        91,
        46,
        18,
        10
      ],
      "minMaxBudgetExcess": 2103
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 268304400,
      "search": 267389850,
      "index_pass": 68593014,
      "box_survivors": 963,
      "valid": 0,
      "rejects": [
        198796836,
        50112831,
        13214887,
        3548967,
        1132070,
        384457,
        129878,
        44338,
        15739,
        6286,
        1786,
        812
      ],
      "minMaxBudgetExcess": 1273
    },
    {
      "pos_pattern": [
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 183980160,
      "search": 183353040,
      "index_pass": 49451071,
      "box_survivors": 1125,
      "valid": 0,
      "rejects": [
        133901969,
        35471993,
        9810588,
        2762813,
        910960,
        318452,
        110743,
        39430,
        15720,
        5827,
        2371,
        1049
      ],
      "minMaxBudgetExcess": 1100
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 28304640,
      "search": 28208160,
      "index_pass": 7979285,
      "box_survivors": 257,
      "valid": 0,
      "rejects": [
        20228875,
        5617292,
        1623590,
        477247,
        164927,
        60431,
        22053,
        8338,
        3183,
        1251,
        494,
        222
      ],
      "minMaxBudgetExcess": 1379
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 15331680,
      "search": 15279420,
      "index_pass": 4315940,
      "box_survivors": 130,
      "valid": 0,
      "rejects": [
        10963480,
        3037035,
        879913,
        256998,
        89748,
        32875,
        11925,
        4448,
        1796,
        693,
        268,
        111
      ],
      "minMaxBudgetExcess": 1663
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        1,
        1,
        2,
        3
      ],
      "raw": 2358720,
      "search": 2350680,
      "index_pass": 696038,
      "box_survivors": 23,
      "valid": 0,
      "rejects": [
        1654642,
        480721,
        144883,
        44386,
        15949,
        6241,
        2341,
        867,
        367,
        159,
        67,
        34
      ],
      "minMaxBudgetExcess": 2704
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 180857040,
      "search": 180233235,
      "index_pass": 46233024,
      "box_survivors": 690,
      "valid": 0,
      "rejects": [
        134000211,
        33797450,
        8889885,
        2396552,
        758929,
        255307,
        87566,
        29306,
        11173,
        4004,
        1572,
        590
      ],
      "minMaxBudgetExcess": 1218
    },
    {
      "pos_pattern": [
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 124016256,
      "search": 123588504,
      "index_pass": 33336414,
      "box_survivors": 721,
      "valid": 0,
      "rejects": [
        90252090,
        23953260,
        6585179,
        1849647,
        613867,
        215577,
        73726,
        26172,
        11361,
        4704,
        1531,
        669
      ],
      "minMaxBudgetExcess": 1102
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 19079424,
      "search": 19013616,
      "index_pass": 5378123,
      "box_survivors": 163,
      "valid": 0,
      "rejects": [
        13635493,
        3788959,
        1092576,
        320700,
        111042,
        40888,
        14833,
        5382,
        2214,
        846,
        358,
        162
      ],
      "minMaxBudgetExcess": 1518
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 10334688,
      "search": 10299042,
      "index_pass": 2916304,
      "box_survivors": 92,
      "valid": 0,
      "rejects": [
        7382738,
        2058304,
        590204,
        172756,
        59728,
        22438,
        8113,
        2800,
        1160,
        462,
        147,
        100
      ],
      "minMaxBudgetExcess": 1434
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        1,
        2,
        2,
        2
      ],
      "raw": 1589952,
      "search": 1584468,
      "index_pass": 468800,
      "box_survivors": 26,
      "valid": 0,
      "rejects": [
        1115668,
        324392,
        97151,
        29832,
        10743,
        4093,
        1543,
        583,
        266,
        107,
        40,
        24
      ],
      "minMaxBudgetExcess": 2088
    }
  ],
  "totals": {
    "raw": 967031520,
    "search": 963518010,
    "index_pass": 254260500,
    "box_survivors": 4813,
    "valid": 0
  },
  "minExcess": 913,
  "minWitness": {
    "pp": [
      1,
      1,
      2
    ],
    "np": [
      1,
      1,
      1,
      1,
      1,
      4
    ],
    "pos": [
      3,
      3,
      2
    ],
    "neg": [
      2,
      9,
      12,
      12,
      12,
      3
    ],
    "u": [
      "-39",
      "-3",
      "-4",
      "-5",
      "2",
      "5",
      "0",
      "4",
      "8",
      "-1",
      "0",
      "0"
    ],
    "masses": [
      "2630",
      "3244"
    ],
    "excess": 913
  },
  "width": "498515831/736645312",
  "det": "247064529073450392704413",
  "coordinate_order": [
    11,
    10,
    5,
    0,
    4,
    6,
    8,
    7,
    2,
    3,
    9,
    1
  ]
}
```

## Reproduction
Load pinned U, call audit(U,6).
```js
function audit(U0, maxLen=3){
const P=13n,B=P**6n,N=12,C=2331,BN=Number(B);
const abs=a=>a<0n?-a:a,mod=(a,m)=>(a%m+m)%m,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a};
const f=(a,b=1n)=>{if(!b)throw Error("division");if(b<0n){a=-a;b=-b}let d=gcd(a,b);return [a/d,b/d]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),lt=(a,b)=>a[0]*b[1]<b[0]*a[1],floor=(a,b)=>a/b-(a<0n&&a%b?1n:0n),ceil=(a,b)=>-floor(-a,b);
const inv=(a,m)=>{let b=m,x=1n,y=0n;a=mod(a,m);while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y]}if(a!==1n)throw Error("unit");return mod(x,m)};
const H=Array.from({length:6},(_,k)=>Array.from({length:N},(_,i)=>inv(BigInt(i+1)**BigInt(k+1),P**BigInt(k+1))));
const U=U0.map(r=>r.map(BigInt)),W=Array.from({length:N},(_,i)=>P*BigInt(i+1)-1n);
const check=(v,t)=>H.every((h,k)=>mod(h.reduce((s,a,i)=>s+a*v[i],0n)-t[k],P**BigInt(k+1))===0n);
for(let u of U)if(!check(u,Array(6).fill(0n)))throw Error("kernel");
let A=U.map((r,i)=>[...r.map(x=>f(x)),...Array.from({length:N},(_,j)=>f(BigInt(i===j)))]),det=f(1n);
for(let i=0;i<N;i++){let j=A.findIndex((r,k)=>k>=i&&r[i][0]);if(j<0)throw Error("singular");if(i!==j){[A[i],A[j]]=[A[j],A[i]];det=mul(det,f(-1n))}let p=A[i][i];det=mul(det,p);A[i]=A[i].map(x=>div(x,p));for(let j=0;j<N;j++)if(j!==i){let c=A[j][i];A[j]=A[j].map((x,k)=>sub(x,mul(c,A[i][k])))}}
if(det[1]!==1n||abs(det[0])!==P**21n)throw Error("det");
const UI=A.map(r=>r.slice(N)),D=UI.map(r=>r.map(x=>{let z=mul(x,f(B));if(z[1]!==1n)throw Error("denom");return z[0]}));
function lift(t){let x=Array(N).fill(0n);for(let j=0;j<6;j++){let q=P**BigInt(j),m=6-j;let a=H.slice(j).map((h,k)=>{let d=t[j+k]-h.reduce((s,v,i)=>s+v*x[i],0n);if(d%q)throw Error("lift residue");return [...h.slice(0,m).map(v=>mod(v,P)),mod(d/q,P)]});for(let k=0;k<m;k++){let l=a.findIndex((r,i)=>i>=k&&r[k]);if(l<0)throw Error("rank");[a[k],a[l]]=[a[l],a[k]];let s=inv(a[k][k],P);a[k]=a[k].map(v=>mod(v*s,P));for(let i=0;i<m;i++)if(i!==k){let c=a[i][k];a[i]=a[i].map((v,h)=>mod(v-c*a[k][h],P))}}for(let i=0;i<m;i++)x[i]+=q*a[i][m]}if(!check(x,t))throw Error("lift check");return x}
const coords=new Map(),targets=new Map();for(let q=1;q<=9;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));targets.set(q*100+r,t);let x=lift(t);coords.set(q*100+r,Array.from({length:N},(_,i)=>Number(mod(x.reduce((a,v,j)=>a+v*D[j][i],0n),B))))}
const bounds=Array.from({length:N},(_,i)=>{let g=UI.map((r,j)=>div(r[i],f(W[j]))),lo=g.reduce((a,b)=>lt(a,b)?a:b,f(0n)),hi=g.reduce((a,b)=>lt(a,b)?b:a,f(0n));return {i,lo,hi,width:sub(hi,lo)}}).sort((a,b)=>lt(a.width,b.width)?-1:lt(b.width,a.width)?1:0);
const width=mul(bounds.at(-1).width,f(2453n));if(!lt(width,f(1n)))throw Error("width");
const cache=new Map(),i0=bounds[0].i;
function box(mp,mn){let key=mp*3000+mn;if(cache.has(key))return cache.get(key);let ap=f(BigInt(C-mp)),am=f(BigInt(C-mn)),arr=bounds.map(({i,lo,hi})=>{let l=mul(f(B),sub(mul(ap,lo),mul(am,hi))),h=mul(f(B),sub(mul(ap,hi),mul(am,lo)));let low=Number(ceil(l[0],l[1])),high=Number(floor(h[0],h[1]));if(low>0||high<0||high-low>=BN)throw Error("box");return {i,low,high}});cache.set(key,arr);return arr}
function* parts(n,lo=1){if(!n){yield [];return}for(let q=lo;q<=n;q++)for(let r of parts(n-q,q))yield [q,...r]}
function roster(pat){let out=[],v=Array(N).fill(0),rs=[];const tail=Array(pat.length+1).fill(0);for(let i=pat.length-1;i>=0;i--)tail[i]=tail[i+1]+169*pat[i]+12;function go(i,m){if(i===pat.length){out.push({m,rs:rs.slice(),v:v.slice()});return}let start=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=start;r<=12;r++){let cost=169*pat[i]+13*r-1;if(m+cost+tail[i+1]>C)break;let a=coords.get(pat[i]*100+r);rs.push(r);for(let k=0;k<N;k++)v[k]=(v[k]+a[k])%BN;go(i+1,m+cost);for(let k=0;k<N;k++)v[k]=(v[k]-a[k]+BN)%BN;rs.pop()}}go(0,0);return out}
function raw(pat){let counts={};for(let q of pat)counts[q]=(counts[q]??0)+1;let p=1;for(let k of Object.values(counts)){let c=1;for(let j=1;j<=k;j++)c=c*(12+j-1)/j;p*=c}if(!Number.isSafeInteger(p))throw Error("raw");return p}
function group(list){let m=new Map();for(let p of list){if(!m.has(p.m))m.set(p.m,[]);m.get(p.m).push(p)}for(let a of m.values())a.sort((p,q)=>p.v[i0]-q.v[i0]);return m}
function lb(a,x){let l=0,h=a.length;while(l<h){let k=(l+h)>>1;if(a[k].v[i0]<x)l=k+1;else h=k}return l}
function ranges(a,c,low,high){let l=(c-high+BN)%BN,h=(c-low+BN)%BN;return l<=h?[[lb(a,l),lb(a,h+1)]]:[[0,lb(a,h+1)],[lb(a,l),a.length]]}
let rows=[],minExcess=Infinity,minWitness=null;
const ppList=[...parts(4)].map(pp=>{let pos=roster(pp);return {pp,pos,groups:group(pos)}});
for(let np of [...parts(9)].filter(p=>p.length===maxLen)){let neg=roster(np);for(let {pp,pos,groups} of ppList){let row={pos_pattern:pp,neg_pattern:np,raw:raw(pp)*raw(np),search:pos.length*neg.length,index_pass:0,box_survivors:0,valid:0,rejects:Array(N).fill(0),minMaxBudgetExcess:null};
for(let n of neg)for(let [mp0,list] of groups){let bs=box(mp0,n.m),rs=ranges(list,n.v[i0],bs[0].low,bs[0].high);let nPass=rs.reduce((s,[l,h])=>s+h-l,0);row.index_pass+=nPass;row.rejects[0]+=list.length-nPass;
for(let [l,h] of rs)for(let k0=l;k0<h;k0++){let p=list[k0],z=Array(N),ok=true;for(let j=0;j<N;j++){let {i,low,high}=bs[j],c=(n.v[i]-p.v[i]+BN)%BN;if(c<=high)z[i]=c;else if(c-BN>=low)z[i]=c-BN;else{if(j===0)throw Error("index false positive");row.rejects[j]++;ok=false;break}}if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let x=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(x%B)throw Error("integrality");return x/B});
let rhs=Array.from({length:6},(_,k)=>n.rs.reduce((s,r,j)=>s+targets.get(np[j]*100+r)[k],0n)-p.rs.reduce((s,r,j)=>s+targets.get(pp[j]*100+r)[k],0n));if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(p.m)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=BigInt(n.m)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);let excess=Number((mp>mn?mp:mn)-BigInt(C));if(row.minMaxBudgetExcess===null||excess<row.minMaxBudgetExcess)row.minMaxBudgetExcess=excess;if(excess<minExcess){minExcess=excess;minWitness={pp,np,pos:p.rs,neg:n.rs,u:u.map(String),masses:[String(mp),String(mn)],excess}}if(excess<=0)row.valid++}}
if(row.rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");if(row.index_pass!==row.search-row.rejects[0])throw Error("index coverage");rows.push(row)}}
return {rows,totals:Object.fromEntries(["raw","search","index_pass","box_survivors","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),minExcess,minWitness,width:width.join("/"),det:abs(det[0]).toString(),coordinate_order:bounds.map(b=>b.i)}
}
```
