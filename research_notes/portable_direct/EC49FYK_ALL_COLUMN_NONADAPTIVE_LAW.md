# EC49FYK — Exact nonadaptive all-column law and general hole-residual criterion

Date 2026-11-24. Research provenance EM-DIRECT-23537B, TASK_RESEARCH, RA-2D7B4AD1AA5CD3F5D9EF1C76. No formal CLAIM or independent review. Frozen BRC16943 atlas copied from EC49FYJ@5ae20314d4709ae4913154874de4ca5da7a874b1:research_notes/portable_direct/EC49FYJ_ALL_COLUMN_COUNT_ADAPTIVE_LAW.md. Also reuse FYB@4ff425bf1abc0e00fe3c5d2d81bd74b3aecb1dad:research_notes/portable_direct/EC49FYB_NONADAPTIVE_37_THEOREM.md. Auxiliary static Boolean observer only; different moduli's arithmetic realizability and native X6 embedding remain separate. AUTHOR_PROVED / EXACT_FINITE_CONSTRUCTIVE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## General residual separation lemma

Let F be a finite family of distinct nonempty row supports. Let m labeled columns and hole set Z with |Z|<=h<m. Site readout is bit_t(U) times 1[j not in Z]. Choose fixed row subsets T_j. For h>=1, exact identification of (U,Z) is equivalent to both:
(A) T_j intersects every U for each j.
(B) for every U!=V, at least h+1 different columns have T_j intersect U xor V.

Necessity A: compare (U,empty) and (U,{j}); B: if at most h distinguishing columns exist, choose those as the common hole set and the pair is indistinguishable. Sufficiency: A makes the zero column signatures exactly the labeled holes, hence equal signatures imply equal Z. B leaves a distinguishing column outside Z for unequal supports. This is an exact criterion for full recovery of labeled Boolean states under the declared static observation, not erasure of physical relations or native branch provenance. For h=0, only B (with threshold 1) is necessary and sufficient. If h>=m and |F|>1 the all-hole states coincide and exact identification is impossible.

## Exact one-hole theorem

For the frozen 50-mask atlas, N(1)=infinity and N(m)=max(16,3m+4) for every integer m>=2. In particular 2,3,4 columns all cost 16, 5 costs 19, 6 costs 22, and 11 costs 37.

Lower bound I: FYB's atlas fact, independently checked over all 1024 ten-bit subsets, is that every hitting T satisfies |T|>=3+1[5 in T]+1[9 in T]. Singleton support differences at rows 5 and 9 require at least two distinct columns each by (B). Sum gives N>=3m+4.

Lower bound II: eight pairwise disjoint difference masks partition all ten rows. Explicit support pairs and their XORs: (788,789):1; (613,615):2; (697,701):4; (394,410):16; (91,123):32; (101,613):512; (646,718):72; (243,371):384. Each difference requires two distinct intersecting columns by B. Each individual physical probe belongs to exactly one of these difference sets, hence at least 16 probes. This proof is independent of solver optimality.

Upper bound: use column masks below. Each hits all 50 supports, and every pairwise XOR hits at least two columns; direct labeled signature replay also passes. Cost is sum of popcounts.
{"2":[703,703],"3":[187,535,684],"4":[7,145,572,682],"5":[7,177,356,523,785],"6":[7,7,177,177,523,523]}

For every m>=4 append m-4 copies of hitting triple 7 to the m=4 layout. A holds in the new columns and B remains true in the original block. Cost 16+3(m-4)=3m+4. This is an unbounded analytic extension, not extrapolation of a finite fit. The m=2 and m=3 witnesses give cost 16. m=1 collapses every support with a hole to the same word. Thus all m are closed. The m=5 and m=6 witnesses are optional extra finite checks.

## Executed evidence

Python exact integer replay (2026-11-24): 618 hitting masks, hitting triples [7,13,145,259], zero violations of the weighted hitting inequality. Minimal inclusion-wise pair-difference masks [1,2,4,16,32,512,72,136,192,264,384]. For m=2,3,4,5,6 respectively (cost, distinct signatures, minimum number of distinguishing columns): (16,150,2),(16,200,2),(16,250,2),(19,300,2),(22,350,2). 1250 raw states across these five cases. Layout discovery used scipy MILP; proof requires no solver status or floating-point evidence. The following compact exact JavaScript verifier also checks the same finite obligations; it can be copied into Node.js.

```js
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
const L={2:[703,703],3:[187,535,684],4:[7,145,572,682],5:[7,177,356,523,785],6:[7,7,177,177,523,523]};
const pc=x=>x.toString(2).replace(/0/g,'').length;
const ck=x=>{if(!x)throw Error('assertion failed')};
const H=Array.from({length:1024},(_,t)=>t).filter(t=>F.every(u=>u&t));
ck(H.length===618);
ck(H.every(t=>pc(t)>=3+Number(Boolean(t&32))+Number(Boolean(t&512))));
const pairs=[[788,789],[613,615],[697,701],[394,410],[91,123],[101,613],[646,718],[243,371]];
let union=0;
for(const [u,v] of pairs){ck(F.includes(u)&&F.includes(v));const d=u^v;ck(d&&(union&d)===0);union|=d}
ck(union===1023);
for(const [key,T] of Object.entries(L)){const m=Number(key);
ck(T.every(t=>H.includes(t)));
for(const u of F)for(const v of F)if(u!==v)ck(T.filter(t=>t&(u^v)).length>=2);
const words=new Set();
for(const u of F)for(let z=-1;z<m;z++){const w=T.map((t,j)=>j===z?0:t&u).join(',');ck(!words.has(w));words.add(w)}
const cost=T.reduce((a,t)=>a+pc(t),0);ck(cost===Math.max(16,3*m+4));console.log(m,cost,words.size)
}
```

## Reusable extension and next question

For h>=1, m>h, the same disjoint difference argument gives N_h(m)>=(h+1)*8 and weighted hitting gives N_h(m)>=3m+2(h+1). Repeating the valid four-column one-hole layout r times makes each pair distinguishable in at least 2r columns. For arbitrary h choose r=ceil((h+1)/2); this gives N_h(m)<=16r+3(m-4r) for m>=4r. Sharpen: when h is odd, h+1=2r, this matches the lower bound 3m+2(h+1) for every m>=4r=2(h+1). This is an analytic corollary of the exact criterion. Next: determine the small-m spectrum and even-h sharp threshold using the general residual multicover formulation; distinguish static observation from native time dynamics.
