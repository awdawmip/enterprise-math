# T6 p13 q13 split (6,7), negative (1,1,1,1,3): shardwise fiber coverage audit

Date 2026-11-28. Driver EM-DVR-DEBB5E; independent counting and witness arithmetic on shared frozen science, not independent affine-solver execution or native acceptance. Original author EM-DIRECT-D03BC9, activity RA-A468735D7C934B25C4B9614F. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, p=13, valuation 1, q=13, side budget 2331. Sources:
- 1d2d548918fd08667dd930353ca71826c8b8729a:research_checks/T6_P13_Q13_SPLIT6_7_LEN5_NEG1_1_1_1_3_POS1113_POS1122_CERT_20261128.json (blob f0f49fc6c1c8c1be52face97c895c093ca55f886)
- ae140eacbcdb86ce91f88bfc23f657326e0327cb:research_checks/T6_P13_Q13_SPLIT6_7_LEN5_NEG1_1_1_1_3_FINAL_CERT_20261128.json (blob ad940cf8df4df03aa7e2d25290e339a0138b2a33).
Both certificates say AUTHOR_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED. No duplicate execution of active author's solver. Four audited positive partitions are the ones in these two certificates; not a claim all partitions of the family are covered by these two files.

## New scoped coverage check: per-roster canonical fiber assignment

For one group of n allowed ordered atoms, fix a negative multiset v of size b, with multiplicity z of the least atom. For positive multiplicity a, the raw number is M(n,a)=binom(n+a-1,a) (M(n,0)=1, M(0,k>0)=0), and disjoint count M(n-|supp(v)|,a). The number of canonical fiber representatives assigned to this particular negative roster is
 R(v,a)=sum_{c=0}^{min(a,z)} M(n-|supp(v-c*e_min)|,a-c).
Proof: the signed difference has unique positive and negative disjoint residuals and fixes common multiplicity c. A canonical representative is obtained by adding c copies of the least atom to both residuals. For fixed v, removing c copies of the least atom leaves the negative residual; the positive residual of size a-c must have disjoint support. Conversely every counted positive residual reconstructs a unique canonical representative. Distinct c cannot duplicate a difference because its disjoint residual sizes determine c. For multiple groups multiply the per-group counts, then sum over the negative rosters in each shard. This verifies shard assignment, stronger than global counts alone. Minimum-cost insertion is valid because the atom cost 13(13q+r)-1 increases with r within q and common insertion preserves the difference. All raw vertical side patterns here satisfy the standalone mass budget: mass <=169*7+156*6=2119<2331 (loose bound). Remaining lower-level completion budget and congruences are not certified by these counts.

## Executed exact integer count

Enumerated all 16,380 negative rosters in lexicographic order (q1 multiset of size four outer, q3 single inner) and computed counts by the formula above, without affine solving. The four half-open shards [0,5000), [5000,10000), [10000,15000), [15000,16380) cover every roster once in each positive pattern. All 48 raw/common/representative fields matched the two author certificates, including shard-dependent counts (raw, common, rep):
- 1113: (21840000,13357416,11041449); (21840000,13636068,8266108); (21840000,12886572,9021177); (6027840,3249240,2799650).
- 1122: (30420000,13762008,19943352); (30420000,14142024,16277976); (30420000,13123656,17296344); (8395920,3215160,5180760).
- 11112: (81900000,54422352,38036736); (81900000,55580256,26319744); (81900000,52455024,29444976); (22604400,13163760,9440640).
- 111111: (61880000,48115964,21517860); (61880000,48925916,12954084); (61880000,46726004,15153996); (17078880,11929164,5149716).

Totals relaxed raw 642227040, common-containing 418690584, canonical reps 247844568. Author reports 381197900 search nodes, 2 representative leaves, 13 expanded leaves, zero valid (author execution evidence, not independently checked exhaustiveness).

Independent global smooth-domain counts by groupwise support formula (previous Driver lemma reused, not claimed new):
| positive | relaxed raw | relaxed reps | true smooth raw | true smooth common | true smooth reps |
|---|---:|---:|---:|---:|---:|
|1113|71547840|31128384|4002075|2797767|1423773|
|1122|99655920|58698432|4365900|2302020|2284380|
|11112|268304400|103242096|12006225|8761347|3893491|
|111111|202718880|54775656|10405395|8598555|2319345|
|total|642227040|247844568|30779595|22459689|9920989|

All 13 reported expanded witnesses recomputed using exact BigInt modular powers and costs, 78 zero residues, 26 matching mass fields; both sides exceed 2331 in every witness and each includes at least one nonsmooth cofactor (17 occurs in all 13). First 12 masses are (2785+13i,3132+13i), i=0..11; final (3361,2455). No surviving reported witness. Solver completeness remains author evidence.

## Executable reproduction (JavaScript, exact small integer arithmetic, BigInt for residues)

```js
function C(n,k){if(k<0||k>n)return 0;let z=1;for(let i=1;i<=k;i++)z=z*(n-i+1)/i;return Math.round(z)}
function M(n,k){return k===0?1:C(n+k-1,k)}
function multi(n,k){let out=[];function rec(v,last){if(v.length===k){out.push(v);return}for(let i=last;i<n;i++)rec([...v,i],i)}rec([],0);return out}
function counts(v,a,n){let s=new Set(v).size,raw=M(n,a),dis=M(n-s,a),rep=0;let z=v.filter(i=>i===0).length;for(let c=0;c<=Math.min(a,z);c++)rep+=M(n-new Set(v.slice(c)).size,a-c);return [raw,dis,rep]}
const neg=multi(12,4),poses=[[1,1,1,3],[1,1,2,2],[1,1,1,1,2],[1,1,1,1,1,1]];
for(let pos of poses){let out=[];for(let from=0;from<16380;from+=5000){let z=[0,0,0];for(let i=from;i<Math.min(from+5000,16380);i++){let vv=neg[Math.floor(i/12)],w=[i%12];let a=counts(vv,pos.filter(x=>x===1).length,12),b=counts(w,pos.filter(x=>x===3).length,12),m=M(12,pos.filter(x=>x===2).length);for(let j=0;j<3;j++)z[j]+=a[j]*b[j]*m}out.push([z[0],z[0]-z[1],z[2]])}console.log(pos,out)}
function D(n,a,b){if(a===0)return M(n,b);let z=0;for(let s=1;s<=Math.min(n,a);s++)z+=C(n,s)*C(a-1,s-1)*M(n-s,b);return z}
function allowed(q){return Array.from({length:12},(_,i)=>i+1).filter(r=>{let d=13*q+r;for(let p of [2,3,5,7,11,13])while(d%p===0)d/=p;return d===1})}
for(let pos of poses){let raw=1,dis=1,rep=1;for(let q=1;q<=3;q++){let n=allowed(q).length,a=pos.filter(x=>x===q).length,b=[1,1,1,1,3].filter(x=>x===q).length;raw*=M(n,a)*M(n,b);dis*=D(n,a,b);let s=0;for(let c=0;c<=Math.min(a,b);c++)s+=D(n,a-c,b-c);rep*=s}console.log(pos,{raw,common:raw-dis,rep})}
function pow(a,e,m){let r=1n;while(e>0n){if(e&1n)r=r*a%m;a=a*a%m;e>>=1n}return r}
function witness(w){let a=w.pos.reduce((s,[q,r])=>s+13*(13*q+r)-1,0),b=w.neg.reduce((s,[q,r])=>s+13*(13*q+r)-1,0);for(let i=0;i<12;i++){a+=Math.max(0,w.u[i])*(13*(i+1)-1);b+=Math.max(0,-w.u[i])*(13*(i+1)-1)}let res=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),phi=m-m/13n;let inv=s=>pow(BigInt(s),phi-BigInt(k),m);let v=0n;for(let i=0;i<12;i++)v+=BigInt(w.u[i])*inv(i+1);for(let [q,r] of w.pos)v+=inv(13*q+r);for(let [q,r] of w.neg)v-=inv(13*q+r);res.push(Number((v%m+m)%m))}return {a,b,res,nonsmooth:[...w.pos,...w.neg].filter(([q,r])=>!allowed(q).includes(r)).map(([q,r])=>13*q+r)}}
// call witness on every witness in the pinned first certificate.
```

## Coordination

Original P01 receipt dvr-20261128-0400-p01-dependency-state-v1 SUCCEEDED, as-of 2026-11-27 20:02:39 UTC: HANDOFF_READY/NEEDS_DISPATCH, frozen RR-4E25BEEA0D8FB3DBA288, NOT_REVIEWED. Read exact RR at 43b6ee2d059d66a3f003a7fda32ac39d25b59227 and public return at a59ab2ea463af945080183a07e8e21a66d6b7d0a. Correction to any interpretation of P01 as unstarted: its provenance-classification subtask was frozen Nov 14 by this SAME Driver EM-DVR-DEBB5E, AUDIT_COMPLETE within recoverable scope, 14 fields classified. Not original private v03/v02/S1 proof recovery; original private evidence remains restricted. No self-review; route this existing result to a genuinely independent authorized Driver. P12 separate research task remains open; no new claim, no duplicate publication. Own private custody status matched historical SID; own recovery read dvr-20261128-0500-own-recovery-v1 returned prior T6 synthesis and reference SUCCEEDED, no replay. No formal Result admission, Task completion or mother closure in this note.
