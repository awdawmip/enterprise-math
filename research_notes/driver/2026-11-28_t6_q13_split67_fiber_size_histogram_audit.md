# T6 q13 split (6,7): exact fiber-size histogram audit

Driver EM-DVR-DEBB5E. Shared research context, independent groupwise multiplicity-vector enumeration (not an independent audit of own previous lemma). Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. p=13, valuation 1, q=13, each side budget 2331. Source author certificate 907e3f4a28f705c965e8efa2ec1b7a56ab313497:research_checks/T6_P13_Q13_SPLIT6_7_LEN4_NEG1_1_2_3_EXTENSION_CERT_20261128.json, blob c48524ee5d5372d3b733f7f291f869076186ab3a. Author kernel exact-executed, unreviewed, not admitted; no rerun of its affine search.

## Fiber-size refinement

For each q group, let a,b be positive/negative multiplicities, n the number of allowed residues, and c the total cancelled multiplicity. The difference vector determines its disjoint-support remainders uniquely and hence c. Each such vector has exactly M(n,c)=binom(n+c-1,c) preimages, since every common multiset of size c can be inserted in both remainders without changing the difference (n>0). There are D(n,a-c,b-c) such difference vectors, with D defined in the previous audit 6112ba6f4672babeef61c569e0d19b31b5c01f10. Thus the histogram for the full partition pair is the multiplicative convolution over q of the per-group histograms:
H_q(t)=sum_{c: M(n,c)=t} D(n,a-c,b-c);
H(t)=sum_{product t_q=t} product H_q(t_q).
Then representatives=sum_t H(t), raw=sum_t t H(t). In these rows all n>=2, hence common-containing raw pairs = raw-H(1). In general n=1 requires tagging c explicitly; size-one fibers need not mean no cancellation. This refinement identifies exact maximum fiber sizes and weighted leaf expansion, without conflating different partition pairs. All vertical sides in these two rows satisfy standalone budget; no claim of full completion feasibility.

## Executed independent enumeration

Directly enumerated group multiplicity vectors and hashed their signed differences; no D formula used in computation. Product histogram obtained by convolution. Residue r=1..12, cofactor 13q+r; smooth means all prime factors <=13. Both rows share negative (1,1,2,3).

| pos | relaxed raw | relaxed common | relaxed reps | smooth raw | smooth common | smooth reps |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,3) | 49061376 | 20625408 | 29934576 | 2546775 | 1340199 | 1335537 |
| (1,1,2,2) | 68335488 | 26308800 | 43946640 | 2778300 | 1407672 | 1514590 |
| Total | 117396864 | 46934208 | 73881216 | 5325075 | 2747871 | 2850127 |

Six relaxed count fields match author exactly.
Histograms (fiber size: number of representatives):
- relaxed (1,1,1,3): {1:28435968,12:1469952,78:19008,144:9504,936:144}
- relaxed (1,1,2,2): {1:42026688,12:1891296,78:9504,144:19008,936:144}
- smooth (1,1,1,3): {1:1206576,7:28728,9:95256,45:2646,63:2268,315:63}
- smooth (1,1,2,2): {1:1370628,7:65268,9:74088,45:1029,63:3528,315:49}

For both rows maximum relaxed fiber size 936, smooth maximum 315. True smooth representative domain shrinks from 73881216 to 2850127 (96.1423% approximately). This is a candidate-domain reduction, not runtime or new full exclusion.

Two explicit author witnesses: using modular exponentiation with Euler inverse, sum u_s*s^(-k)+sum_pos(13q+r)^(-k)-sum_neg(13q+r)^(-k) mod 13^k for k=1..6 gives all twelve residues zero. Recompute masses with costs 13s-1 and 13(13q+r)-1: (3246,2411), (3106,2999). Both fail both budgets; nonsmooth cofactors respectively (19,29,38,43) and (38,41). Both have fiber size 1 in relaxed model (no shared exact atom). No witness survives true budget and maximal-prime conditions among reported witnesses; full author solver coverage remains author evidence.

## Reproduction (JavaScript, same groupwise algorithm)
```js
const allowed=(q,smooth)=>Array.from({length:12},(_,i)=>i+1).filter(r=>{
 if(!smooth)return true;let d=13*q+r;for(const p of [2,3,5,7,11,13])while(d%p===0)d/=p;return d===1
});
function multisets(n,k){let out=[],v=Array(n).fill(0);function rec(i,left){if(i===n){if(left===0)out.push(v.slice());return}for(let j=0;j<=left;j++){v[i]=j;rec(i+1,left-j)}}rec(0,k);return out}
function census(n,a,b){const map=new Map();for(const u of multisets(n,a))for(const v of multisets(n,b)){const k=u.map((x,i)=>x-v[i]).join(",");map.set(k,(map.get(k)||0)+1)}const h={};for(const v of map.values())h[v]=(h[v]||0)+1;return h}
function calc(pos,neg,smooth){let h={1:1};for(let q=1;q<=6;q++){let n=allowed(q,smooth).length,a=pos.filter(x=>x===q).length,b=neg.filter(x=>x===q).length,hh=census(n,a,b),z={};for(let [i,v] of Object.entries(h))for(let [j,w] of Object.entries(hh)){let k=Number(i)*Number(j);z[k]=(z[k]||0)+v*w}h=z}let reps=0,raw=0;for(let [k,v] of Object.entries(h)){reps+=v;raw+=Number(k)*v}return {hist:h,reps,raw,common:raw-(h[1]||0)}}
for(const pos of [[1,1,1,3],[1,1,2,2]])for(const smooth of [false,true])console.log(calc(pos,[1,1,2,3],smooth))
const mod=(a,m)=>((a%m)+m)%m;
function pow(a,k,m){let v=1n;while(k){if(k&1n)v=v*a%m;a=a*a%m;k>>=1n}return v}
function witness(w){let vals=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),phi=m-m/13n;const invpow=s=>pow(BigInt(s),phi-BigInt(k),m);let v=0n;for(let i=0;i<12;i++)v+=BigInt(w.u[i])*invpow(i+1);for(let [q,r] of w.pos)v+=invpow(13*q+r);for(let [q,r] of w.neg)v-=invpow(13*q+r);vals.push(Number(mod(v,m)))}let a=w.pos.reduce((s,[q,r])=>s+13*(13*q+r)-1,0),b=w.neg.reduce((s,[q,r])=>s+13*(13*q+r)-1,0);for(let i=0;i<12;i++){a+=Math.max(w.u[i],0)*(13*(i+1)-1);b+=Math.max(-w.u[i],0)*(13*(i+1)-1)}return {residues:vals,masses:[a,b],nonsmooth:[...w.pos,...w.neg].filter(([q,r])=>!allowed(q,true).includes(r)).map(([q,r])=>13*q+r)}}
// Run witness(w) for both witnesses in the exact author JSON pinned above.
```

## Coordination

Previous canonical selection dvr-20261128-0203-post-child-closure-dispatch-v1 SUCCEEDED, 285 candidates, selected RS-BRC-UNKNOWN-ORDER-BITWISE-FOURIER-SAMPLING-20261005 (P12). Exact current task read dvr-20261128-0303-p12-current-owner-v1 SUCCEEDED at Source dd4e9b54806064d54e14b0367ee710c20da3cb04: TP2-BC1A7FA0007357402667, READY / NEEDS_DISPATCH, unassigned, no claim/actor. Its own taskbook read matches published blob 53dfbc58dbd45f73b3d3a006fba08e6dbebdaf7e. Selection/read is not a claim. Driver has not launched a researcher, claimed or published a duplicate task. Route to genuine existing researcher via current canonical selection; preserve P01/v03/S1 provenance and P12 hard target. T6 original synthesis still SUCCEEDED and nonterminal; no new Result or Task acceptance.
