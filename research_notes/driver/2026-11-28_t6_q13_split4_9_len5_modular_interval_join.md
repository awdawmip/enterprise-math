# T6 q13 split(4,9), negative length 5 — exact modular interval join

Informed continuation of saved Driver research. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; same basis and proof as 0f5415ae2ef3e91852500912e71549b2e6285a51:research_notes/driver/2026-11-28_t6_q13_split4_9_len1to3_modular_interval_join.md. Exact source program below is the read-back predecessor with filter changed to equality (only length 5). All positive partitions of 4, all negative partitions of 9 with exactly five atoms, relaxed model including common atoms. Every surviving vector was reconstructed and checked in six original congruences and both mass budgets; rejection ledger checked per row. No formal acceptance or author-certificate field comparison; not a clean independent review of own method.

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
        5
      ],
      "raw": 22358700,
      "search": 22358700,
      "index_pass": 6026254,
      "box_survivors": 159,
      "valid": 0,
      "rejects": [
        16332446,
        4321714,
        1195388,
        335487,
        111885,
        39355,
        13987,
        5142,
        1829,
        784,
        357,
        167
      ],
      "minMaxBudgetExcess": 1276
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
        5
      ],
      "raw": 15331680,
      "search": 15331680,
      "index_pass": 4334483,
      "box_survivors": 183,
      "valid": 0,
      "rejects": [
        10997197,
        3056580,
        878584,
        256199,
        91170,
        32496,
        11707,
        4526,
        1936,
        737,
        246,
        119
      ],
      "minMaxBudgetExcess": 1521
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
        5
      ],
      "raw": 2358720,
      "search": 2358720,
      "index_pass": 698865,
      "box_survivors": 20,
      "valid": 0,
      "rejects": [
        1659855,
        482441,
        145613,
        45231,
        15685,
        6106,
        2339,
        834,
        343,
        141,
        75,
        37
      ],
      "minMaxBudgetExcess": 2850
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
        5
      ],
      "raw": 1277640,
      "search": 1277640,
      "index_pass": 377441,
      "box_survivors": 17,
      "valid": 0,
      "rejects": [
        900199,
        261820,
        77981,
        23555,
        8692,
        3278,
        1242,
        490,
        238,
        84,
        30,
        14
      ],
      "minMaxBudgetExcess": 2519
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
        5
      ],
      "raw": 196560,
      "search": 196560,
      "index_pass": 60730,
      "box_survivors": 9,
      "valid": 0,
      "rejects": [
        135830,
        41182,
        12851,
        4076,
        1561,
        626,
        253,
        101,
        44,
        14,
        10,
        3
      ],
      "minMaxBudgetExcess": 3104
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
        4
      ],
      "raw": 71547840,
      "search": 71547840,
      "index_pass": 19281608,
      "box_survivors": 407,
      "valid": 0,
      "rejects": [
        52266232,
        13836870,
        3824051,
        1064762,
        358373,
        126121,
        44610,
        16437,
        6315,
        2394,
        859,
        409
      ],
      "minMaxBudgetExcess": 1698
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
        4
      ],
      "raw": 49061376,
      "search": 49061376,
      "index_pass": 13862516,
      "box_survivors": 508,
      "valid": 0,
      "rejects": [
        35198860,
        9770691,
        2809702,
        828879,
        285152,
        105961,
        37863,
        14718,
        5697,
        2039,
        876,
        430
      ],
      "minMaxBudgetExcess": 1176
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
        4
      ],
      "raw": 7547904,
      "search": 7547904,
      "index_pass": 2233277,
      "box_survivors": 124,
      "valid": 0,
      "rejects": [
        5314627,
        1542781,
        465553,
        142020,
        50991,
        19821,
        7274,
        2641,
        1299,
        480,
        188,
        105
      ],
      "minMaxBudgetExcess": 1509
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
        4
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1206308,
      "box_survivors": 56,
      "valid": 0,
      "rejects": [
        2882140,
        834266,
        250785,
        76714,
        27633,
        10370,
        3843,
        1502,
        704,
        267,
        101,
        67
      ],
      "minMaxBudgetExcess": 2110
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
        4
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194472,
      "box_survivors": 17,
      "valid": 0,
      "rejects": [
        434520,
        132166,
        41001,
        13288,
        4775,
        1932,
        771,
        324,
        123,
        47,
        21,
        7
      ],
      "minMaxBudgetExcess": 1996
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
        3,
        3
      ],
      "raw": 38755080,
      "search": 38755080,
      "index_pass": 10442293,
      "box_survivors": 222,
      "valid": 0,
      "rejects": [
        28312787,
        7489190,
        2066845,
        587034,
        192789,
        68022,
        24662,
        8328,
        3318,
        1227,
        470,
        186
      ],
      "minMaxBudgetExcess": 1752
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
        3,
        3
      ],
      "raw": 26574912,
      "search": 26574912,
      "index_pass": 7511861,
      "box_survivors": 298,
      "valid": 0,
      "rejects": [
        19063051,
        5289715,
        1528639,
        448763,
        154907,
        56308,
        20843,
        7627,
        2863,
        1250,
        430,
        218
      ],
      "minMaxBudgetExcess": 1359
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
        3,
        3
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1208950,
      "box_survivors": 94,
      "valid": 0,
      "rejects": [
        2879498,
        834117,
        253131,
        76705,
        27998,
        10447,
        3912,
        1449,
        581,
        273,
        182,
        61
      ],
      "minMaxBudgetExcess": 1626
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
        3,
        3
      ],
      "raw": 2214576,
      "search": 2214576,
      "index_pass": 654131,
      "box_survivors": 45,
      "valid": 0,
      "rejects": [
        1560445,
        451900,
        136484,
        41228,
        15056,
        5804,
        2232,
        824,
        332,
        137,
        66,
        23
      ],
      "minMaxBudgetExcess": 1477
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        1,
        3,
        3
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105207,
      "box_survivors": 8,
      "valid": 0,
      "rejects": [
        235497,
        71228,
        22392,
        7169,
        2653,
        1044,
        434,
        159,
        73,
        27,
        17,
        3
      ],
      "minMaxBudgetExcess": 1704
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
        2,
        2,
        3
      ],
      "raw": 99655920,
      "search": 99655920,
      "index_pass": 26848040,
      "box_survivors": 567,
      "valid": 0,
      "rejects": [
        72807880,
        19264690,
        5319883,
        1496689,
        496938,
        173858,
        60350,
        21399,
        8603,
        3148,
        1229,
        686
      ],
      "minMaxBudgetExcess": 1001
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
        2,
        2,
        3
      ],
      "raw": 68335488,
      "search": 68335488,
      "index_pass": 19310769,
      "box_survivors": 785,
      "valid": 0,
      "rejects": [
        49024719,
        13604138,
        3927709,
        1151064,
        396693,
        144219,
        53617,
        19424,
        8205,
        3334,
        1031,
        550
      ],
      "minMaxBudgetExcess": 1176
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3
      ],
      "raw": 10513152,
      "search": 10513152,
      "index_pass": 3110498,
      "box_survivors": 174,
      "valid": 0,
      "rejects": [
        7402654,
        2150581,
        647682,
        196638,
        71153,
        27628,
        10190,
        3652,
        1601,
        814,
        277,
        108
      ],
      "minMaxBudgetExcess": 2016
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3
      ],
      "raw": 5694624,
      "search": 5694624,
      "index_pass": 1686866,
      "box_survivors": 86,
      "valid": 0,
      "rejects": [
        4007758,
        1165840,
        351570,
        107564,
        38251,
        14325,
        5535,
        2172,
        884,
        370,
        189,
        80
      ],
      "minMaxBudgetExcess": 2345
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        2,
        2,
        3
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270638,
      "box_survivors": 17,
      "valid": 0,
      "rejects": [
        605458,
        183661,
        57520,
        18143,
        6874,
        2615,
        1062,
        420,
        185,
        91,
        31,
        19
      ],
      "minMaxBudgetExcess": 1912
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
        2,
        2,
        2,
        2
      ],
      "raw": 22358700,
      "search": 22358700,
      "index_pass": 6027469,
      "box_survivors": 156,
      "valid": 0,
      "rejects": [
        16331231,
        4324680,
        1192964,
        337001,
        111964,
        39172,
        13732,
        4689,
        1927,
        796,
        274,
        114
      ],
      "minMaxBudgetExcess": 1589
    },
    {
      "pos_pattern": [
        1,
        1,
        2
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 15331680,
      "search": 15331680,
      "index_pass": 4326994,
      "box_survivors": 175,
      "valid": 0,
      "rejects": [
        11004686,
        3053590,
        876274,
        257724,
        87759,
        32341,
        11837,
        4396,
        1746,
        775,
        250,
        127
      ],
      "minMaxBudgetExcess": 1259
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 2358720,
      "search": 2358720,
      "index_pass": 696181,
      "box_survivors": 37,
      "valid": 0,
      "rejects": [
        1662539,
        480951,
        145105,
        44280,
        15981,
        6081,
        2316,
        800,
        389,
        156,
        60,
        25
      ],
      "minMaxBudgetExcess": 2052
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 1277640,
      "search": 1277640,
      "index_pass": 378652,
      "box_survivors": 5,
      "valid": 0,
      "rejects": [
        898988,
        263231,
        77794,
        23953,
        8375,
        3260,
        1122,
        473,
        200,
        175,
        39,
        25
      ],
      "minMaxBudgetExcess": 2222
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        2,
        2,
        2,
        2
      ],
      "raw": 196560,
      "search": 196560,
      "index_pass": 60420,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        136140,
        41120,
        12752,
        4038,
        1521,
        623,
        223,
        68,
        38,
        20,
        9,
        4
      ],
      "minMaxBudgetExcess": 3731
    }
  ],
  "totals": {
    "raw": 472970160,
    "search": 472970160,
    "index_pass": 130914923,
    "box_survivors": 4173,
    "valid": 0
  },
  "minExcess": 1001,
  "minWitness": {
    "pp": [
      1,
      1,
      1,
      1
    ],
    "np": [
      1,
      1,
      2,
      2,
      3
    ],
    "pos": [
      1,
      2,
      5,
      7
    ],
    "neg": [
      4,
      4,
      1,
      1,
      4
    ],
    "u": [
      "18",
      "-16",
      "9",
      "-6",
      "7",
      "6",
      "8",
      "-4",
      "-2",
      "0",
      "-2",
      "0"
    ],
    "masses": [
      "3055",
      "3332"
    ],
    "excess": 1001
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
Load pinned U, call audit(U,5).
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
