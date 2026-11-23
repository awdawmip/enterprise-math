# EC49FYK extension — exact all-hole-count nonadaptive law

Date 2026-11-24; frozen BRC16943 support atlas as in EC49FYK_ALL_COLUMN_NONADAPTIVE_LAW.md at 3cf8d1234260bd01db59d449e38c15c4b667012a (same draft PR). This extends and closes the multi-hole question left at the end of that note. Author proof with exact finite replay; independent review pending. Research provenance EM-DIRECT-23537B. No formal CLAIM.

## Theorem

For m>=1 labeled columns and hole budget 1<=h<m, fixed unit-cost noiseless Boolean site observations identifying every (U,Z), U in the frozen atlas, |Z|<=h, require exactly
N_h(m)=max(8(h+1), 3m+2(h+1)).
For h>=m all-hole supports collapse, so N_h(m)=infinity. For h=0 and m>=1, N_0(m)=8.

## Proof

Put d=h+1. Prior note proves the exact criterion: every column hits all supports, and every pairwise XOR difference intersects at least d distinct columns. Its eight disjoint difference witnesses and weighted hitting inequality give lower bound max(8d,3m+2d). These are necessary for every h>=1.

Define a block with parameter d0 and length l if every column hits all supports and every XOR intersects at least d0 columns. Concatenation adds the d0 guarantees, because columns in disjoint blocks are distinct. The previous note gives d0=2 blocks at lengths 2,3,4, each with cost 16. Here are d0=3 blocks of lengths 3,4,5,6, each with cost 24:
{"3":[703,703,703],"4":[358,571,669,695],"5":[187,372,519,523,692],"6":[7,177,356,523,540,690]}

The attached integer verification checks each block directly. For any d>=2, express d as a sum of twos if even, or one three plus twos if odd. For each summand d0, any integer block length from d0 to 2d0 is available at cost 8d0. Sums of these integer intervals fill every integer m from d to 2d. Thus concatenate blocks to realize cost 8d throughout that interval. For m>2d, first take the length-2d construction and append m-2d copies of hitting triple 7. This maintains all XOR coverage and costs 8d+3(m-2d)=3m+2d. Lower and upper bounds match. No limit or solver extrapolation enters the proof.

When h=0 all columns are present; only one occurrence of each XOR difference is needed. Eight disjoint differences force eight probes, and the eight-row mask 703 in one column distinguishes the entire atlas (also shown by the two identical masks in the previous note). No other column need be read. When h>=m, choose Z=all columns: all 50 supports yield the same word. This covers all integer parameters.

## Exact executed JS check

Frozen atlas:
[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
Block check outputs:
[
  {
    "m": 3,
    "cost": 24,
    "minimum_distinguishing_columns": 3,
    "states": 350
  },
  {
    "m": 4,
    "cost": 24,
    "minimum_distinguishing_columns": 3,
    "states": 550
  },
  {
    "m": 5,
    "cost": 24,
    "minimum_distinguishing_columns": 3,
    "states": 800
  },
  {
    "m": 6,
    "cost": 24,
    "minimum_distinguishing_columns": 3,
    "states": 1100
  }
]
Each row of the output checks all 1225 distinct support pairs, all columns against all supports, and raw labeled signatures for every hole set of size 0,1,2. Exact bitwise integers only; no solver correctness assumption. Layout discovery used a finite MILP; the following verification does not require it.

```js
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005], L={"3":[703,703,703],"4":[358,571,669,695],"5":[187,372,519,523,692],"6":[7,177,356,523,540,690]};
const pc=x=>x.toString(2).replace(/0/g,"").length;
const ck=x=>{if(!x)throw Error("assert")};
for(const [k,T] of Object.entries(L)){
 const m=+k;ck(T.length===m&&T.reduce((s,t)=>s+pc(t),0)===24);
 ck(T.every(t=>F.every(u=>t&u)));
 let min=m;
 for(let i=0;i<F.length;i++)for(let j=i+1;j<F.length;j++)min=Math.min(min,T.filter(t=>t&(F[i]^F[j])).length);
 ck(min>=3);
 const words=new Set();
 for(const u of F)for(let z=0;z<(1<<m);z++)if(pc(z)<=2){
 const w=T.map((t,j)=>z&(1<<j)?0:u&t).join(",");
 ck(!words.has(w));words.add(w);
 }
 ck(words.size===50*(1+m+m*(m-1)/2));
 console.log(m,min,words.size);
}
```

## Next

The fixed-observation problem is closed for all column counts and hole budgets in this frozen support atlas. Next investigate the adaptive multi-hole minimax law and the benefit of adaptivity versus hole density, using the residual fibre observer with exact labeled multiplicities. Arithmetic realizability under changed moduli/hole budgets and native X6 dynamical connection remain separate questions.