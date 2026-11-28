# T6 q13 split(4,9), negative lengths 7–9, positive lengths 1–2 — exact modular interval join

Informed continuation of saved Driver research. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; same basis and proof as 0f5415ae2ef3e91852500912e71549b2e6285a51:research_notes/driver/2026-11-28_t6_q13_split4_9_len1to3_modular_interval_join.md. Predecessor whole length7–9 run timed out without returned data or durable destination at subsequent read; this is a bounded partial scientific calculation, not replay of a protected write. Exact source program below filters negative length>=7 and positive length<=2, all three positive partitions (4),(1,3),(2,2). Relaxed model including common atoms. Every surviving vector reconstructed and checked in six original congruences and both mass budgets; rejection ledger checked per row. No formal acceptance or author-certificate field comparison; not a clean independent review of own method. Remaining positive patterns (1,1,2),(1,1,1,1) for negative lengths7–9.

## Executed data
```json
{
  "rows": [
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
        1,
        1,
        1,
        1
      ],
      "raw": 24186240,
      "search": 15596496,
      "index_pass": 4033130,
      "box_survivors": 39,
      "valid": 0,
      "rejects": [
        11563366,
        2939372,
        781341,
        210473,
        67312,
        22581,
        7761,
        2743,
        956,
        383,
        122,
        47
      ],
      "minMaxBudgetExcess": 2040
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
        1,
        1,
        1,
        1
      ],
      "raw": 13100880,
      "search": 8448102,
      "index_pass": 2187169,
      "box_survivors": 34,
      "valid": 0,
      "rejects": [
        6260933,
        1592422,
        424615,
        115031,
        36574,
        12204,
        4073,
        1407,
        522,
        190,
        64,
        33
      ],
      "minMaxBudgetExcess": 2048
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
        1,
        1,
        1,
        1
      ],
      "raw": 2015520,
      "search": 1299708,
      "index_pass": 353335,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        946373,
        252531,
        70588,
        19942,
        6648,
        2344,
        801,
        291,
        114,
        47,
        16,
        5
      ],
      "minMaxBudgetExcess": 1487
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
        1,
        1,
        2
      ],
      "raw": 54991872,
      "search": 44746992,
      "index_pass": 11819472,
      "box_survivors": 228,
      "valid": 0,
      "rejects": [
        32927520,
        8548940,
        2315353,
        639743,
        206983,
        70625,
        24595,
        8057,
        3177,
        1103,
        473,
        195
      ],
      "minMaxBudgetExcess": 1153
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
        1,
        1,
        2
      ],
      "raw": 29787264,
      "search": 24237954,
      "index_pass": 6405902,
      "box_survivors": 102,
      "valid": 0,
      "rejects": [
        17832052,
        4627187,
        1259320,
        346947,
        112669,
        38738,
        13434,
        4648,
        1824,
        649,
        261,
        123
      ],
      "minMaxBudgetExcess": 1447
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
        1,
        1,
        2
      ],
      "raw": 4582656,
      "search": 3728916,
      "index_pass": 1032802,
      "box_survivors": 32,
      "valid": 0,
      "rejects": [
        2696114,
        732451,
        208551,
        60053,
        20307,
        7289,
        2622,
        916,
        361,
        129,
        60,
        31
      ],
      "minMaxBudgetExcess": 1991
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
        1,
        3
      ],
      "raw": 21385728,
      "search": 20233872,
      "index_pass": 5502506,
      "box_survivors": 121,
      "valid": 0,
      "rejects": [
        14731366,
        3934091,
        1096526,
        311813,
        103838,
        35784,
        12666,
        4734,
        1753,
        759,
        285,
        136
      ],
      "minMaxBudgetExcess": 884
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
        1,
        3
      ],
      "raw": 11583936,
      "search": 10960014,
      "index_pass": 2981365,
      "box_survivors": 64,
      "valid": 0,
      "rejects": [
        7978649,
        2131364,
        594556,
        167829,
        56511,
        20168,
        6828,
        2512,
        975,
        366,
        125,
        67
      ],
      "minMaxBudgetExcess": 1425
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
        1,
        3
      ],
      "raw": 1782144,
      "search": 1686156,
      "index_pass": 480970,
      "box_survivors": 25,
      "valid": 0,
      "rejects": [
        1205186,
        337243,
        98316,
        29334,
        10087,
        3803,
        1327,
        501,
        199,
        87,
        28,
        20
      ],
      "minMaxBudgetExcess": 2280
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
        2,
        2
      ],
      "raw": 49061376,
      "search": 46721664,
      "index_pass": 12693535,
      "box_survivors": 241,
      "valid": 0,
      "rejects": [
        34028129,
        9083783,
        2525422,
        713314,
        238778,
        84729,
        29858,
        10694,
        4197,
        1635,
        620,
        264
      ],
      "minMaxBudgetExcess": 1558
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
        2,
        2
      ],
      "raw": 26574912,
      "search": 25307568,
      "index_pass": 6871930,
      "box_survivors": 190,
      "valid": 0,
      "rejects": [
        18435638,
        4915944,
        1368489,
        387689,
        129015,
        45411,
        16058,
        5666,
        2193,
        818,
        335,
        122
      ],
      "minMaxBudgetExcess": 1297
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
        2,
        2
      ],
      "raw": 4088448,
      "search": 3893472,
      "index_pass": 1108158,
      "box_survivors": 35,
      "valid": 0,
      "rejects": [
        2785314,
        778200,
        226418,
        66576,
        23191,
        8585,
        3182,
        1186,
        482,
        188,
        78,
        37
      ],
      "minMaxBudgetExcess": 1605
    }
  ],
  "totals": {
    "raw": 243140976,
    "search": 206860914,
    "index_pass": 55470274,
    "box_survivors": 1119,
    "valid": 0
  },
  "minExcess": 884,
  "minWitness": {
    "pp": [
      1,
      3
    ],
    "np": [
      1,
      1,
      1,
      1,
      1,
      1,
      3
    ],
    "pos": [
      3,
      5
    ],
    "neg": [
      7,
      7,
      7,
      7,
      8,
      10,
      12
    ],
    "u": [
      "-9",
      "-11",
      "-5",
      "13",
      "1",
      "1",
      "3",
      "5",
      "-1",
      "-2",
      "0",
      "0"
    ],
    "masses": [
      "2367",
      "3215"
    ],
    "excess": 884
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
Load pinned U, call audit(U,7).
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
const ppList=[...parts(4)].filter(p=>p.length<=2).map(pp=>{let pos=roster(pp);return {pp,pos,groups:group(pos)}});
for(let np of [...parts(9)].filter(p=>p.length>=maxLen)){let neg=roster(np);for(let {pp,pos,groups} of ppList){let row={pos_pattern:pp,neg_pattern:np,raw:raw(pp)*raw(np),search:pos.length*neg.length,index_pass:0,box_survivors:0,valid:0,rejects:Array(N).fill(0),minMaxBudgetExcess:null};
for(let n of neg)for(let [mp0,list] of groups){let bs=box(mp0,n.m),rs=ranges(list,n.v[i0],bs[0].low,bs[0].high);let nPass=rs.reduce((s,[l,h])=>s+h-l,0);row.index_pass+=nPass;row.rejects[0]+=list.length-nPass;
for(let [l,h] of rs)for(let k0=l;k0<h;k0++){let p=list[k0],z=Array(N),ok=true;for(let j=0;j<N;j++){let {i,low,high}=bs[j],c=(n.v[i]-p.v[i]+BN)%BN;if(c<=high)z[i]=c;else if(c-BN>=low)z[i]=c-BN;else{if(j===0)throw Error("index false positive");row.rejects[j]++;ok=false;break}}if(!ok)continue;row.box_survivors++;
let u=Array.from({length:N},(_,j)=>{let x=z.reduce((s,v,k)=>s+BigInt(v)*U[k][j],0n);if(x%B)throw Error("integrality");return x/B});
let rhs=Array.from({length:6},(_,k)=>n.rs.reduce((s,r,j)=>s+targets.get(np[j]*100+r)[k],0n)-p.rs.reduce((s,r,j)=>s+targets.get(pp[j]*100+r)[k],0n));if(!check(u,rhs))throw Error("congruences");
let mp=BigInt(p.m)+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=BigInt(n.m)+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);let excess=Number((mp>mn?mp:mn)-BigInt(C));if(row.minMaxBudgetExcess===null||excess<row.minMaxBudgetExcess)row.minMaxBudgetExcess=excess;if(excess<minExcess){minExcess=excess;minWitness={pp,np,pos:p.rs,neg:n.rs,u:u.map(String),masses:[String(mp),String(mn)],excess}}if(excess<=0)row.valid++}}
if(row.rejects.reduce((a,b)=>a+b,0)+row.box_survivors!==row.search)throw Error("coverage");if(row.index_pass!==row.search-row.rejects[0])throw Error("index coverage");rows.push(row)}}
return {rows,totals:Object.fromEntries(["raw","search","index_pass","box_survivors","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),minExcess,minWitness,width:width.join("/"),det:abs(det[0]).toString(),coordinate_order:bounds.map(b=>b.i)}
}
```
