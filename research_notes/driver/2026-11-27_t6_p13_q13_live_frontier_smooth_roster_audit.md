# T6 p13 q13: scoped roster audit and exact smooth prefilter on live author frontier

2026-11-27, original Driver lane EM-DVR-DEBB5E. Shared directed context; this is a nonblind implementation crosscheck of the other author's finite input counts and explicit witnesses, not a fresh author CLAIM, a complete independent kernel audit, or native admission. Preserve original EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F contribution and prior plan contributors.

## Control
Original dvr-20261127-1057-t6-current-frontier-rebase-v1 SUCCEEDED (03:00 UTC), publication TP2-34B106D2512A298C9647, HANDOFF_READY/NEEDS_DISPATCH as of that receipt, no live owner in that snapshot. Its q14 preflight wording is stale; retain previous 10:57 correction and author-side full-observer q14 proof. Fresh em_status observed Source 0b97bc054094c693608c3ebf48e41b60bba86ed2, runtime code 377d036316e10ade56d6c555358cd394e73a6e90, CODE_UPGRADE_AVAILABLE, active jobs 0 at observation. Own managed registration original start d25-sites-permanent-driver-start-20261110-v1 SUCCEEDED; current recovery dvr-20261127-1205-own-recovery-v1 returned original SID and no pending own review requests in returned recent request set. Historical F7 rejection not replayed. No new active DA authority asserted from these read-only receipts.

Current actual author progress is later than the prior T6 handoff: [12:00 journal](https://github.com/awdawmip/chatgpt-global-knowledge/blob/1a50b7d719b2baed7a980bd04a914c128ed11f92/journal/enterprise-math/2026-11-27/20261127-1200-p13q13-split4-9-len7-first-complete.md) reports p13 q13 split (4,9), 303/343 author families, split49 27/30; first seven-atom negative family complete, next (1,1,1,1,1,2,2). This is author-reported coverage, not an independent proof of those 303 families. Do not dispatch or redo this active scientific direction solely because the formal global Task has stale handoff. Search located q12 split66 row21 certificate a93ae46c70f6d2596a7b0c5c84cffc1e2e21ad6d and q13 split2/11 first length6 certificate a4783a93b205a74580652a35dbbcc2557e511efb. Search misses for q17–19 are not absence evidence.

## Exact smoothness filter
In the original maximal denominator prime p=13 stratum, after higher valuations have been removed, each once-13-divisible denominator is 13a, a=13q+r, 1<=r<=12, cost w=169q+13r-1. Since every prime divisor of 13a is <=13, necessarily a is 13-smooth. The test by repeated division by 2,3,5,7,11,13 is exact. It preserves all actual integer multiplicities; opposite supports must be disjoint after common-denomination cancellation. Each side's vertical mass is bounded by 2331 (q0 mass can only increase it). Filtering is necessary, not a sufficient moment collision test. The original relaxed roster certificates are valid on a superset; the filter does not retroactively change their domain or claim a novel general method.

For fixed q patterns, enumerate nondecreasing r within equal q, retain vertical mass<=2331, count full multiplicities per support mask, then sum products of multiplicities over disjoint support masks. Each multiset has exactly one sorted enumeration; disjoint-support product counts every ordered pair once. Exact JS arithmetic below uses BigInt masks; count magnitudes remain safe integers.

## Current split (4,9) finite check
Source: [first 7-atom complete pos1111 certificate](https://github.com/awdawmip/enterprise-math/blob/96875df7e9c5ef54ab837b48ca64703e8bc9e72e/research_checks/T6_P13_Q13_SPLIT4_9_LEN7_NEG1_1_1_1_1_1_3_POS1111_COMPLETE_CERT_20261127.json), blob a1b9328c68295a90c20ecadb644dc15fbf74d8a1.

Negative pattern (1,1,1,1,1,1,3): raw 148512, budget-feasible 140513 (matches author), smooth raw 21021, smooth feasible 19569. Next negative pattern (1,1,1,1,1,2,2): raw 340704, budget-feasible 324456 (matches author journal), smooth raw 36036, smooth feasible 34632.

| Positive q pattern | Smooth positive count | First family smooth disjoint pairs | Next family smooth disjoint pairs |
|---|---:|---:|---:|
| 4 | 6 | 117414 | 207792 |
| 1,3 | 63 | 598572 | 1336286 |
| 2,2 | 28 | 547932 | 570786 |
| 1,1,2 | 315 | 2186079 | 3324525 |
| 1,1,1,1 | 495 | 1634643 | 3610835 |

These are original cancellation-normalized vertical input pair counts, **not** the author's GS representative-search counts or a completed six-congruence lattice calculation. The next negative domain is reduced from 324456 to 34632 before opposite pairing, with no loss of true maximal-p13 candidates. Preserve the author's relaxed-superset route if its broader scope is desired; the result is an optional exact prefilter, not an instruction to switch an active execution.

All three explicit relaxed-sphere witnesses in the cited pos1111 certificate were independently evaluated in the original denominator coordinates, using six exact residues mod 13^k (k=1..6) and actual q0 signed mass. All residue vectors are zero; masses exactly (4893,2745), (2088,4821), (2305,4161), all violate at least one 2331 side budget. Additionally each includes at least one cofactor with prime divisor >13: witness1 has 19 and 46, witness2 has 17 and 19, witness3 has 19. No witness survives true maximal-p13 scope. This does not independently establish sphere-search completeness.

## Earlier split (2,11) bounded crosscheck
[Author certificate](https://github.com/awdawmip/enterprise-math/blob/a4783a93b205a74580652a35dbbcc2557e511efb/research_checks/T6_P13_Q13_SPLIT2_11_LEN6_FIRST_FAMILY_CERT_20261126.json), blob dad857ef54839f848fc18c5e6bbef04acaba21ac. Negative pattern (1,1,1,1,1,6), raw negative 52416. Exact independent recursion for positive (1,1): raw pairs 4088448, over-budget 2457780, feasible 1630668, common-support feasible 818075. Positive (2): raw 628992, over 378120, feasible 250872, common 0. All match published counts. Smooth disjoint pairs are 49798 and 18683 respectively. Its single explicit witness has six zero residues and masses (3904,3511), with forbidden cofactors 19,23,82. This is a bounded audit only; lattice coverage not reexecuted.

## Reproduction core (executed JavaScript)
```js
const mass=a=>a.reduce((s,[q,r])=>s+169*q+13*r-1,0);
const smooth=n=>{for(const p of [2,3,5,7,11,13])while(n%p===0)n/=p;return n===1};
function enumR(qs,sm,fn){let a=[];function rec(i){if(i===qs.length){fn(a);return}let q=qs[i],l=i&&qs[i-1]===q?a[i-1][1]:1;for(let r=l;r<=12;r++){if(sm&&!smooth(13*q+r))continue;a.push([q,r]);rec(i+1);a.pop()}}rec(0)}
const bit=([q,r])=>1n<<BigInt(12*(q-1)+r-1);
function count(qs,sm){let raw=0,feasible=0;const hist=new Map();enumR(qs,sm,a=>{raw++;if(mass(a)>2331)return;feasible++;let mask=a.reduce((v,b)=>v|bit(b),0n);hist.set(mask,(hist.get(mask)||0)+1)});return {raw,feasible,hist}}
for(const qs of [[1,1,1,1,1,1,3],[1,1,1,1,1,2,2],[1,1,1,1,1,6]]){
 const rel=count(qs,false), sm=count(qs,true);
 for(const ps of qs.at(-1)===6?[[1,1],[2]]:[[4],[1,3],[2,2],[1,1,2],[1,1,1,1]]){
 let p=count(ps,true),disjoint=0;
 for(const [a,n] of p.hist)for(const [b,m] of sm.hist)if((a&b)===0n)disjoint+=n*m;
 console.log(qs,ps,rel.raw,rel.feasible,sm.raw,sm.feasible,p.feasible,disjoint)
 }}
function inv(a,m){let [x,y,b,c]=[1n,0n,BigInt(a),m];while(c){let q=b/c;[b,c]=[c,b-q*c];[x,y]=[y,x-q*y]}return (x%m+m)%m}
// For each certificate witness (positive and negative arrays, signed q0 u):
function witness(p,n,u){
 let residue=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),v=0n;
 for(const [q,r] of p)v+=inv(13*q+r,m)**BigInt(k);
 for(const [q,r] of n)v-=inv(13*q+r,m)**BigInt(k);
 for(let i=0;i<12;i++)v+=BigInt(u[i])*inv(i+1,m)**BigInt(k);
 residue.push(Number((v%m+m)%m))}
 let ms=[mass(p),mass(n)];for(let i=0;i<12;i++)ms[u[i]>=0?0:1]+=Math.abs(u[i])*(13*(i+1)-1);
 return {residue,ms};
}
```

No Native Review/Result acceptance, formal Task DONE or mother closure. Existing author lane continues its actual frontier; no parallel duplicated campaign or owner reassignment. The q14 full-observer proof still needs genuine nonauthor review; the older RR does not include it. Next: use current eligible control route for review/association of exact new Results when available, and preserve nonauthor lattice-completeness audit obligation. No schedule change.
