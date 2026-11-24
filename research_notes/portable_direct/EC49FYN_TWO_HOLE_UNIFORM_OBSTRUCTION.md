# EC49FYN — uniform two-hole obstruction and a weighted all-hole lower bound

Date: 2026-11-24. Portable continuation of EC49FYM, frozen auxiliary BRC16943, immutable parent 5a42a6421c60b1bf7a7b5ac82a2bb8731cb693ff, research_notes/portable_direct/EC49FYM_TWO_HOLE_POSITIVE_FIBRE_QUOTIENT.md. Extension theorem: EC49FYL at 5cbfe43ccd041b7b7fc458586d4384a0de074246, research_notes/portable_direct/EC49FYL_DENSE_HOLE_ADAPTIVE_EXACT_LAW.md. Prior researcher provenance EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76, original registration receipt succeeded. Current read r4-20261124-0830-ec49as-task-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at 8d7fbb6553961bf3b93e5a3b3928b4089da75a9b; limited directory observation, no formal shared CLAIM. No new authenticated Activity writer binding asserted.

## Model and principal theorem

F is the exact 50 nonempty ten-bit support masks listed below. For integer 1<=h<m, a raw state (U,Z) has U in F and a labeled hole subset Z of at most h columns; observation (t,j) is bit_t(U) times 1[j not in Z]. Unit noiseless Boolean queries, exact recovery of U and Z. Q_h(m) is minimum worst-case adaptive depth.

**Theorem 1.** For all m>h>=1,
Q_h(m) >= m+3+ceil((h-1)/3).
In particular for h=2, Q_2(m)>=m+4 for every m>=3.

By FYM's depth-12 tree at m=8 and FYL's extension Q_h(m+1)<=Q_h(m)+1, Q_2(m)<=m+4 for all m>=8. Thus **Q_2(m)=m+4 for all m>=8; c_2=4**. The earlier exact finite values from FYL/FYM give the entire double-hole law: m=3:11, m=4:10, m=5:10, m=6:11, m=7:12, m>=8:m+4. The upper construction and small-m classification are parent-dependent; this note proves the new uniform lower bound without a finite search or extrapolation.

## Proof: all-zero first-touch adversary and residual cost

For U define tau(U) as the transversal number of {V minus U: V in F, U proper subset V}. Consider any correct decision tree and follow its all-zero answers until exactly h-1 distinct physical columns have been touched (empty prefix if h=1). This prefix must be attainable: at every earlier prefix all touched columns can be holes, so every support U and the hole set equal to the touched columns is compatible, and at least 50 distinct states survive. A finite correct tree cannot terminate there or continue indefinitely without reaching h-1 distinct columns. Let Z be precisely those h-1 columns. Record the first query row t_j in each j in Z. All states (U,Z), U in F, are compatible with this prefix. Fix any such U.

On its entire path:
1. Each live column requires at least one positive query, since making that column an additional hole gives another legal state (|Z|+1=h) and would produce identical answers otherwise.
2. Each hole column requires at least one query at a row in U, since filling this hole alone is legal and otherwise indistinguishable. Its answer is zero. If its first query row is outside U, that first query is additional to the mandatory query at a row in U.
3. For every strict superset V, (V,Z) is legal, and differs only in live columns at rows of V minus U. At least tau(U) negative queries in live columns are therefore required. These are disjoint from the previous mandatory queries and extra queries in holes.

Consequently the depth on this state is at least
m + tau(U) + sum_{j in Z} 1[t_j not in U].
This is a simultaneous joint-state bound: the same fixed Z is used for the entire support family, and the live/filled-hole/extra-hole competitors all remain in the permitted original state space.

The three supports 101,788,833 have tau=3, witnessed respectively by disjoint difference masks (144,266,512), (1,40,192), (24,34,132). Their triple intersection is zero. Each first-touch row misses at least one of the three supports, so one support misses at least ceil((h-1)/3) first touches. The claimed bound follows. In h=2, the proof needs only the root: some hard support excludes its row, and putting a hole in that column forces a wasted probe. This defeats every possible depth m+3 strategy, including arbitrarily many columns. No search cutoff enters the argument.

## Theorem 2: exact fractional first-touch coefficient

For all m>h>=1, also
Q_h(m) >= m+ceil((49+15(h-1))/26).
Combine by taking the maximum with Theorem 1 and other established lower bounds (including the separate maximal-density exact law).

Proof: apply the same path inequality to the eight supports with integer weights
(U,w,tau) = (86,3,1),(101,4,3),(281,2,2),(394,5,2),(460,1,1),(602,3,0),(673,5,2),(788,3,3).
Weights total 26 and weighted tau total 49. Across rows 0..9, weighted positive incidence is [11,11,11,11,11,9,11,11,11,11], so every first touch contributes at least 15 weighted misses. The weighted average depth lower bound is m+(49+15(h-1))/26; one actual target reaches at least its ceiling. The tau values are independently enumerated below. This finite certificate suffices without trusting a numerical optimizer.

Moreover, the 15/26 coefficient is exact for the relaxed fractional first-touch miss game: assign row weights [6,5,4,1,1,0,1,2,3,3]/26. Every support has row-weight mass >=11/26 (verified all 50). Therefore worst expected miss <=15/26, matching the dual support weights above. This characterizes only the fractional first-touch game, not the entire adaptive tree. In particular the stabilized constants now obey
max(3+ceil((h-1)/3), ceil((49+15(h-1))/26)) <= c_h <= 2h (h>=2),
using FYM's upper. Thus the residual excess grows at least linearly with fixed hole budget h. For h=2 the exact constant is 4. For h=3 the bound leaves c_3 in {4,5,6}. Future work: exploit later joint residual constraints or construct a three-hole tree with smaller excess, rather than continuing the now-unnecessary m>=10 two-hole search.

## Exact integer verification (executed JavaScript; reproducible Node.js)

```js
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
const tau=u=>{const ds=F.filter(v=>v!==u&&(v&u)===u).map(v=>v^u);let k=10;for(let t=0;t<1024;t++)if(ds.every(d=>d&t))k=Math.min(k,pc(t));return k};
const hard=F.filter(u=>tau(u)===3);
const weights=[[86,3],[101,4],[281,2],[394,5],[460,1],[602,3],[673,5],[788,3]],p=[6,5,4,1,1,0,1,2,3,3];
const hits=Array.from({length:10},(_,i)=>weights.reduce((s,[u,w])=>s+w*((u>>i)&1),0));
const tw=weights.reduce((s,[u,w])=>s+w*tau(u),0);
const minp=Math.min(...F.map(u=>p.reduce((s,w,i)=>s+w*((u>>i)&1),0)));
const witness=[[101,[144,266,512]],[788,[1,40,192]],[833,[24,34,132]]];
if(hard.join()!=="101,788,833"||hard.reduce((a,b)=>a&b)!==0||tw!==49||minp!==11||Math.max(...hits)!==11||!witness.every(([u,ds])=>ds.every((d,i)=>!(u&d)&&F.includes(u|d)&&ds.slice(0,i).every(e=>!(e&d)))))throw Error("verification failed");
console.log({hard,intersection:0,witness,weights,hits,tw,p,minp,tauHistogram:F.reduce((o,u)=>(o[tau(u)]=(o[tau(u)]??0)+1,o),{})});
```

Actual exact output: hard [101,788,833], intersection 0, witnesses and weights as listed, hits [11,11,11,11,11,9,11,11,11,11], tw 49, minp 11, tauHistogram {0:22,1:17,2:8,3:3}. All assertions passed. Weight and row denominators each 26 by direct sum. Each tau enumerates all 1024 row masks against all strict supersets. The proof is unbounded in m,h; finite computation checks only the fixed support-family facts. No new replay of FYM's tree, no new independent review.

Status: AUTHOR_PROVED / EXACT_FINITE_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. Auxiliary observation model only; no P000, native X6 dynamics, task ownership or promotion changes.
