# T6 p13 q13: negative (1,1,1,2,2), six positive-pattern shard coverage audit

2026-11-28; original Driver lane EM-DVR-DEBB5E, shared frozen context, alternative counting implementation relative to author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. No independent affine-solver execution or admission. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; p=13, valuation 1, q=13, split (6,7), side budget 2331. Exact author cert e3a52d5d589632c52c9170f8c2b002c451788196:research_checks/T6_P13_Q13_SPLIT6_7_LEN5_NEG1_1_1_2_2_POS15_TO222_CERT_20261128.json, blob d409edad4de44ea0d72c122bbf5ca89027bf1797.

## Scope and method
Reuse proved per-roster canonical representative formula from 6425a7e23e2ba623af5a1f1056a3e57eea241c1a:research_notes/driver/2026-11-28_t6_q13_len5_shardwise_fiber_coverage_audit.md. This is a new certificate/family audit, not a new general theorem. For fixed negative multiset v and positive multiplicity a in one group, raw M(n,a), disjoint M(n-|supp(v)|,a), representative sum_{c=0}^{min(a,z)} M(n-|supp(v-c e_min)|,a-c), where z is least-atom multiplicity. Common-containing count equals raw minus disjoint. Multiply groupwise and sum within each half-open shard. All 28,392 negative rosters (lexicographic q1 triple outer, q2 pair inner, 364*78) enumerated once per positive pattern. Six shards [0,5000),...,[25000,28392) cover the family without gap/overlap. Minimum common insertion preserves the signed difference and minimizes both masses, under same allowed group alphabet. Smooth alphabet requires 13*q+r to be 13-smooth. Standalone vertical budget is automatic: at most 169*7+156*6=2119<2331, not the completed affine mass. Use prior D(n,a,b) support formula for the true smooth model. No claim that these counts prove solver exhaustiveness.

## Exact executed result
36 shard rows, 108 independent raw/common/representative comparisons, zero mismatches. Counts:
| pos | relaxed raw | relaxed common | relaxed rep | smooth raw | smooth common | smooth rep |
|---|---:|---:|---:|---:|---:|---:|
|1,5|4088448|876096|3285360|207900|56700|157500|
|2,4|4088448|628992|3511872|194040|48510|152460|
|3,3|2214576|0|2214576|129360|0|129360|
|1,1,4|26574912|9771840|17555616|1247400|557928|745416|
|1,2,3|49061376|16443648|33864480|2037420|926100|1212750|
|2,2,2|10334688|3800160|6827184|388080|202125|211365|
|total|96362448|31520736|67259088|4204200|1791363|2608851|

Author reports 109035200 search nodes and 2 leaves, zero valid; solver completeness remains author evidence. Both witnesses independently checked by exact modular powers and mass summation: (2364,3491), nonsmooth cofactor 31; (2813,3091), nonsmooth cofactors 29,51,17,17,31. All 12 modular residues zero; both sides over budget in both witnesses. The two witness checks are not exhaustive solving. Six positive patterns only; author has further patterns in progress.

## Reproduction (JS, executed; integers below safe 2^53 bound, modular arithmetic BigInt)
```js
function C(n,k){if(k<0||k>n)return 0;let z=1;for(let i=1;i<=k;i++)z=z*(n-i+1)/i;return Math.round(z)}
function M(n,k){return k===0?1:C(n+k-1,k)}
function multi(n,k){let out=[];function rec(v,last){if(v.length===k){out.push(v);return}for(let i=last;i<n;i++)rec([...v,i],i)}rec([],0);return out}
function counts(v,a,n){let raw=M(n,a),dis=M(n-new Set(v).size,a),rep=0;let z=v.filter(i=>i===0).length;for(let c=0;c<=Math.min(a,z);c++)rep+=M(n-new Set(v.slice(c)).size,a-c);return [raw,dis,rep]}
function D(n,a,b){if(a===0)return M(n,b);let z=0;for(let s=1;s<=Math.min(n,a);s++)z+=C(n,s)*C(a-1,s-1)*M(n-s,b);return z}
function allowed(q){return Array.from({length:12},(_,i)=>i+1).filter(r=>{let d=13*q+r;for(let p of [2,3,5,7,11,13])while(d%p===0)d/=p;return d===1})}
function pow(a,e,m){let r=1n;while(e>0n){if(e&1n)r=r*a%m;a=a*a%m;e>>=1n}return r}
function witness(w){let a=w.pos.reduce((s,[q,r])=>s+13*(13*q+r)-1,0),b=w.neg.reduce((s,[q,r])=>s+13*(13*q+r)-1,0);for(let i=0;i<12;i++){a+=Math.max(0,w.u[i])*(13*(i+1)-1);b+=Math.max(0,-w.u[i])*(13*(i+1)-1)}let res=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),phi=m-m/13n;let inv=s=>pow(BigInt(s),phi-BigInt(k),m);let v=0n;for(let i=0;i<12;i++)v+=BigInt(w.u[i])*inv(i+1);for(let [q,r] of w.pos)v+=inv(13*q+r);for(let [q,r] of w.neg)v-=inv(13*q+r);res.push(Number((v%m+m)%m))}return {a,b,res,nonsmooth:[...w.pos,...w.neg].filter(([q,r])=>!allowed(q).includes(r)).map(([q,r])=>13*q+r)}}
// cert is the JSON parsed from pinned source above.
const n1=multi(12,3),n2=multi(12,2);let ledger=[],mismatches=[],fields=0;
for(let g of cert.groups){let pos=g.pos.split(",").map(Number),shards=[];let cnt=q=>pos.filter(x=>x===q).length;for(let sh of g.shards){let [lo,hi]=sh,z=[0,0,0];for(let i=lo;i<hi;i++){let a=counts(n1[Math.floor(i/n2.length)],cnt(1),12),b=counts(n2[i%n2.length],cnt(2),12),m=1;for(let q=3;q<=6;q++)m*=M(12,cnt(q));for(let j=0;j<3;j++)z[j]+=a[j]*b[j]*m}let row=[z[0],z[0]-z[1],z[2]];fields+=3;if(row.some((x,j)=>x!==sh[j+2]))mismatches.push({pos:g.pos,lo,row,expected:sh.slice(2,5)});shards.push(row)}
let raw=1,dis=1,rep=1;for(let q=1;q<=6;q++){let n=allowed(q).length,a=cnt(q),b=cert.neg.filter(x=>x===q).length;raw*=M(n,a)*M(n,b);dis*=D(n,a,b);let s=0;for(let c=0;c<=Math.min(a,b);c++)s+=D(n,a-c,b-c);rep*=s}ledger.push({pos:g.pos,relaxed:shards.reduce((a,r)=>a.map((v,j)=>v+r[j]),[0,0,0]),smooth:[raw,raw-dis,rep],shards})}
console.log({fields,rosters:n1.length*n2.length,mismatches,ledger,w:cert.witnesses.map(witness)});
```

## Coordination
Original P12 current-owner query dvr-20261128-0500-p12-current-owner-v2 SUCCEEDED as of 2026-11-27T21:03:14.581893Z, Source 6425a7e23e2ba623af5a1f1056a3e57eea241c1a. READY/NEEDS_DISPATCH, owner taskbook/unassigned, claim null; publication TP2-BC1A7FA0007357402667, requires RESEARCHER; read gives no execution authorization. P12 existing support lemma 2f3f5eb1e0ab9f3b4b561baae721d03f8644472b remains usable when a lawful researcher claims. P01 existing own frozen Result RR-4E25BEEA0D8FB3DBA288 requires nonauthor review, not self-review. Own synthesis original dvr-20261128-0100-t6-scoped-synthesis-v1 SUCCEEDED; own recovery dvr-20261128-0602-own-recovery-v1 confirms reference and synthesis terminal, no pending same writes among returned requests. The previous recovery request is not a durable control_result ID (CONTROL_REQUEST_NOT_FOUND); use site recovery metadata operation for recovery. No new identity/claim, no new Task, no accepted Result or mother closure.
