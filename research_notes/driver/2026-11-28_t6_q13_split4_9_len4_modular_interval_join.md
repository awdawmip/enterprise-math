# T6 q13 split(4,9), negative length 4 — exact modular interval join

Informed continuation of saved Driver research. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; same basis and proof as 0f5415ae2ef3e91852500912e71549b2e6285a51:research_notes/driver/2026-11-28_t6_q13_split4_9_len1to3_modular_interval_join.md. Exact source program below is the read-back predecessor with filter changed to equality (only length 4). All positive partitions of 4, all negative partitions of 9 with exactly four atoms, relaxed model including common atoms. Every surviving vector was reconstructed and checked in six original congruences and both mass budgets; rejection ledger checked per row. No formal acceptance or author-certificate field comparison; not a clean independent review of own method.

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
        6
      ],
      "raw": 5962320,
      "search": 5962320,
      "index_pass": 1684579,
      "box_survivors": 44,
      "valid": 0,
      "rejects": [
        4277741,
        1185797,
        342587,
        100667,
        35705,
        12205,
        4700,
        1593,
        845,
        320,
        70,
        46
      ],
      "minMaxBudgetExcess": 1936
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
        6
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1208286,
      "box_survivors": 53,
      "valid": 0,
      "rejects": [
        2880162,
        835633,
        250981,
        76898,
        27661,
        10547,
        3947,
        1474,
        693,
        289,
        84,
        26
      ],
      "minMaxBudgetExcess": 1257
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
        6
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 194244,
      "box_survivors": 10,
      "valid": 0,
      "rejects": [
        434748,
        131799,
        41268,
        13105,
        4871,
        1924,
        743,
        286,
        141,
        64,
        20,
        13
      ],
      "minMaxBudgetExcess": 3150
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
        6
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 105080,
      "box_survivors": 5,
      "valid": 0,
      "rejects": [
        235624,
        71514,
        22115,
        6967,
        2677,
        1079,
        436,
        170,
        76,
        27,
        12,
        2
      ],
      "minMaxBudgetExcess": 3040
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        1,
        6
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16886,
      "box_survivors": 1,
      "valid": 0,
      "rejects": [
        35530,
        11304,
        3612,
        1202,
        486,
        164,
        78,
        20,
        14,
        2,
        2,
        1
      ],
      "minMaxBudgetExcess": 3450
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
        5
      ],
      "raw": 15331680,
      "search": 15331680,
      "index_pass": 4333945,
      "box_survivors": 136,
      "valid": 0,
      "rejects": [
        10997735,
        3044726,
        885350,
        259157,
        91583,
        33470,
        11809,
        4581,
        1909,
        847,
        241,
        136
      ],
      "minMaxBudgetExcess": 1492
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
        5
      ],
      "raw": 10513152,
      "search": 10513152,
      "index_pass": 3109489,
      "box_survivors": 165,
      "valid": 0,
      "rejects": [
        7403663,
        2146986,
        650136,
        195952,
        71781,
        27276,
        10502,
        3817,
        1619,
        819,
        313,
        123
      ],
      "minMaxBudgetExcess": 1688
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
        5
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 499272,
      "box_survivors": 27,
      "valid": 0,
      "rejects": [
        1118136,
        337953,
        106380,
        34082,
        12734,
        4799,
        1914,
        817,
        292,
        161,
        83,
        30
      ],
      "minMaxBudgetExcess": 2209
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
        5
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 271257,
      "box_survivors": 26,
      "valid": 0,
      "rejects": [
        604839,
        184169,
        57592,
        18179,
        6952,
        2594,
        998,
        441,
        191,
        74,
        28,
        13
      ],
      "minMaxBudgetExcess": 2705
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        2,
        5
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43286,
      "box_survivors": 4,
      "valid": 0,
      "rejects": [
        91498,
        28685,
        9466,
        3046,
        1201,
        512,
        200,
        101,
        39,
        11,
        14,
        7
      ],
      "minMaxBudgetExcess": 3447
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
        3,
        4
      ],
      "raw": 15331680,
      "search": 15331680,
      "index_pass": 4332497,
      "box_survivors": 214,
      "valid": 0,
      "rejects": [
        10999183,
        3051429,
        880885,
        258542,
        88815,
        33407,
        12030,
        4443,
        1647,
        732,
        242,
        111
      ],
      "minMaxBudgetExcess": 1203
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
        3,
        4
      ],
      "raw": 10513152,
      "search": 10513152,
      "index_pass": 3112025,
      "box_survivors": 180,
      "valid": 0,
      "rejects": [
        7401127,
        2150178,
        648868,
        198393,
        70756,
        26906,
        10317,
        3718,
        1545,
        723,
        325,
        116
      ],
      "minMaxBudgetExcess": 1353
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        1,
        3,
        4
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 499969,
      "box_survivors": 18,
      "valid": 0,
      "rejects": [
        1117439,
        339555,
        105638,
        33501,
        12654,
        5089,
        2033,
        893,
        336,
        155,
        46,
        51
      ],
      "minMaxBudgetExcess": 2162
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        1,
        3,
        4
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 269974,
      "box_survivors": 23,
      "valid": 0,
      "rejects": [
        606122,
        183045,
        57527,
        18086,
        6790,
        2716,
        1042,
        418,
        194,
        86,
        31,
        16
      ],
      "minMaxBudgetExcess": 2128
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        1,
        3,
        4
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43457,
      "box_survivors": 17,
      "valid": 0,
      "rejects": [
        91327,
        28700,
        9521,
        3152,
        1202,
        546,
        181,
        69,
        31,
        14,
        20,
        4
      ],
      "minMaxBudgetExcess": 3244
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
        4
      ],
      "raw": 15331680,
      "search": 15331680,
      "index_pass": 4331997,
      "box_survivors": 137,
      "valid": 0,
      "rejects": [
        10999683,
        3050055,
        881521,
        258896,
        89295,
        32881,
        11909,
        4377,
        1752,
        708,
        318,
        148
      ],
      "minMaxBudgetExcess": 1687
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
        4
      ],
      "raw": 10513152,
      "search": 10513152,
      "index_pass": 3108924,
      "box_survivors": 127,
      "valid": 0,
      "rejects": [
        7404228,
        2151480,
        646238,
        195408,
        71553,
        27291,
        10236,
        3827,
        1678,
        669,
        268,
        149
      ],
      "minMaxBudgetExcess": 1961
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
        4
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 499985,
      "box_survivors": 33,
      "valid": 0,
      "rejects": [
        1117423,
        338766,
        106426,
        33658,
        12740,
        4869,
        2045,
        789,
        452,
        137,
        52,
        18
      ],
      "minMaxBudgetExcess": 3163
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
        4
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 270616,
      "box_survivors": 26,
      "valid": 0,
      "rejects": [
        605480,
        184144,
        56526,
        18172,
        6877,
        2980,
        1083,
        502,
        187,
        86,
        26,
        7
      ],
      "minMaxBudgetExcess": 2706
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        2,
        2,
        4
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43476,
      "box_survivors": 6,
      "valid": 0,
      "rejects": [
        91308,
        28962,
        9386,
        3091,
        1190,
        486,
        202,
        77,
        32,
        30,
        11,
        3
      ],
      "minMaxBudgetExcess": 3285
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
        3,
        3
      ],
      "raw": 15331680,
      "search": 15331680,
      "index_pass": 4331628,
      "box_survivors": 156,
      "valid": 0,
      "rejects": [
        11000052,
        3048448,
        882093,
        259133,
        89247,
        32950,
        12199,
        4419,
        1808,
        771,
        251,
        153
      ],
      "minMaxBudgetExcess": 1749
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
        3,
        3
      ],
      "raw": 10513152,
      "search": 10513152,
      "index_pass": 3107302,
      "box_survivors": 171,
      "valid": 0,
      "rejects": [
        7405850,
        2144207,
        649082,
        198075,
        71385,
        27287,
        10452,
        3919,
        1655,
        682,
        259,
        128
      ],
      "minMaxBudgetExcess": 1550
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        1,
        2,
        3,
        3
      ],
      "raw": 1617408,
      "search": 1617408,
      "index_pass": 499340,
      "box_survivors": 34,
      "valid": 0,
      "rejects": [
        1118068,
        338270,
        106109,
        33955,
        12439,
        4935,
        2212,
        744,
        368,
        208,
        44,
        22
      ],
      "minMaxBudgetExcess": 2102
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        1,
        2,
        3,
        3
      ],
      "raw": 876096,
      "search": 876096,
      "index_pass": 271374,
      "box_survivors": 19,
      "valid": 0,
      "rejects": [
        604722,
        184128,
        57684,
        18279,
        6813,
        2617,
        1091,
        477,
        136,
        74,
        39,
        17
      ],
      "minMaxBudgetExcess": 2553
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        1,
        2,
        3,
        3
      ],
      "raw": 134784,
      "search": 134784,
      "index_pass": 43339,
      "box_survivors": 7,
      "valid": 0,
      "rejects": [
        91445,
        28737,
        9382,
        3126,
        1199,
        543,
        205,
        74,
        40,
        14,
        5,
        7
      ],
      "minMaxBudgetExcess": 3723
    },
    {
      "pos_pattern": [
        1,
        1,
        1,
        1
      ],
      "neg_pattern": [
        2,
        2,
        2,
        3
      ],
      "raw": 5962320,
      "search": 5962320,
      "index_pass": 1686942,
      "box_survivors": 55,
      "valid": 0,
      "rejects": [
        4275378,
        1188024,
        343091,
        101026,
        34486,
        12803,
        4604,
        1721,
        670,
        306,
        102,
        54
      ],
      "minMaxBudgetExcess": 2146
    },
    {
      "pos_pattern": [
        1,
        1,
        2
      ],
      "neg_pattern": [
        2,
        2,
        2,
        3
      ],
      "raw": 4088448,
      "search": 4088448,
      "index_pass": 1207607,
      "box_survivors": 42,
      "valid": 0,
      "rejects": [
        2880841,
        834340,
        251723,
        76389,
        27888,
        10545,
        3960,
        1584,
        728,
        266,
        81,
        61
      ],
      "minMaxBudgetExcess": 2095
    },
    {
      "pos_pattern": [
        1,
        3
      ],
      "neg_pattern": [
        2,
        2,
        2,
        3
      ],
      "raw": 628992,
      "search": 628992,
      "index_pass": 193629,
      "box_survivors": 14,
      "valid": 0,
      "rejects": [
        435363,
        131209,
        41064,
        13171,
        4910,
        2027,
        745,
        285,
        119,
        59,
        17,
        9
      ],
      "minMaxBudgetExcess": 2856
    },
    {
      "pos_pattern": [
        2,
        2
      ],
      "neg_pattern": [
        2,
        2,
        2,
        3
      ],
      "raw": 340704,
      "search": 340704,
      "index_pass": 104988,
      "box_survivors": 18,
      "valid": 0,
      "rejects": [
        235716,
        71106,
        22357,
        7332,
        2440,
        978,
        494,
        160,
        68,
        25,
        5,
        5
      ],
      "minMaxBudgetExcess": 2726
    },
    {
      "pos_pattern": [
        4
      ],
      "neg_pattern": [
        2,
        2,
        2,
        3
      ],
      "raw": 52416,
      "search": 52416,
      "index_pass": 16792,
      "box_survivors": 0,
      "valid": 0,
      "rejects": [
        35624,
        11202,
        3591,
        1182,
        490,
        194,
        73,
        33,
        18,
        6,
        0,
        3
      ],
      "minMaxBudgetExcess": null
    }
  ],
  "totals": {
    "raw": 136038240,
    "search": 136038240,
    "index_pass": 39442185,
    "box_survivors": 1768,
    "valid": 0
  },
  "minExcess": 1203,
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
      3,
      4
    ],
    "pos": [
      2,
      4,
      9,
      12
    ],
    "neg": [
      7,
      7,
      8,
      3
    ],
    "u": [
      "-21",
      "13",
      "17",
      "11",
      "-3",
      "-3",
      "6",
      "-6",
      "-2",
      "-1",
      "2",
      "1"
    ],
    "masses": [
      "3534",
      "3496"
    ],
    "excess": 1203
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
Load pinned U, call audit(U,4).
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
