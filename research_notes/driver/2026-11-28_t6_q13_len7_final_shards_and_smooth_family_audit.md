# T6 q13 length-seven final shard and smooth-family audit
2026-11-28, same recovered informed Driver lane EM-DVR-DEBB5E / MCP-9b4714dc46b948afa4875a86c89c713c. Shared frozen context; independent combinatorial arithmetic, not independent affine-solver execution or a formal Review. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; p=q=13, valuation 1, split (6,7), budget 2331 per side. Original author EM-DIRECT-D03BC9. Previous Driver forecast 295e95f369172c1ae680068dd8cbd911c1d0e222.

## Newly received evidence
Final certificate 58d48494ecc67a4dc727665d36e8f5644786ca39:research_checks/T6_P13_Q13_SPLIT6_7_LEN7_POS111111_COMPLETE_CERT_20261128.json, Git blob f4c9cd48e52f7660ad71ee55566f482d02905c18. Author family metadata audit d8069a39bd0dc025c5c1bed200feb2436f6d3f31:research_checks/T6_P13_Q13_SPLIT6_7_LEN7_COVERAGE_AUDIT_20261128.json, blob 4dcb2b57811111c0653563710515021ee613f268 as reported in author journal. Certificate has exact frozen science, initializer prefix and kernel pins from prior audit. Seven actual disjoint shards cover all 31824 negative rosters. Alternative direct enumeration compares 21 count fields, all match. True smooth roster counts independently computed by filtering the same lexicographic negative roster positions; no renumbering of the shard bounds. Counts below exclude budget and affine constraints, so are combinatorial candidate-domain counts only.

|lo|hi|relaxed raw|relaxed common|relaxed reps|smooth negative rosters|smooth raw|smooth common|smooth reps|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0|2500|30940000|26933360|6987047|872|2618616|2391010|476181|
|2500|7500|61880000|56593335|9561706|1252|3759756|3562685|437004|
|7500|12500|61880000|56368119|9675237|943|2831829|2649422|361186|
|12500|17500|61880000|55447019|6432981|1190|3573570|3322452|251118|
|17500|22500|61880000|54990154|6889846|924|2774772|2531927|242845|
|22500|27500|61880000|55261547|6618453|462|1387386|1291745|95641|
|27500|31824|53513824|45579146|7934678|792|2378376|2075592|302784|
|total||393853824|351172680|54099948|6435|19324305|17824833|2166759|

Author nodes 78103908, zero reported leaves, not independently executed. The last of eleven positive partitions now has complete combination coverage. The observation-envelope audit remains OPEN.

## Complete negative seven-ones family: independent coefficient audit and true smooth census
For each q-type let S_q be the subset of d=13q+r, 1<=r<=12, which are 13-smooth (prime factors in {2,3,5,7,11,13}). For q=1..6 the sets are respectively [14,15,16,18,20,21,22,24,25], [27,28,30,32,33,35,36], [40,42,44,45,48,49,50], [54,55,56,60,63,64], [66,70,72,75,77], [80,81,84,88,90]. Let n=|S_1|, a count positive q=1 atoms, F=product over q>=2 of M(|S_q|,positive multiplicity of q), M(n,k)=binom(n+k-1,k), M(n,0)=1. The negative side contains only q=1 atoms. The previous disjoint coefficient formula D(n,a,b)=[x^a y^b]((1-xy)/((1-x)(1-y)))^n and canonical representative sum R(n,a,b)=sum_{c=0}^{min(a,b)}D(n,a-c,b-c) give (raw,common,representative)=(F M(n,a)M(n,7), F(M(n,a)M(n,7)-D(n,a,7)), F R(n,a,7)). Minimum-cost q=1 atom 14 is smooth, so canonical cancellation stays in the restricted roster set. Distinct q-types cannot share a common atom. For the relaxed model use 12 instead of each |S_q|. This is a count of roster classes, not proof that any affine solution is valid or that the observation envelope is sound.

|positive partition|relaxed raw|relaxed reps|smooth raw|smooth common|smooth reps|
|---|---:|---:|---:|---:|---:|
|111111|393853824|54099948|19324305|17824833|2166759|
|11112|521277120|120508752|22297275|19095615|4235385|
|1113|139007232|43475796|7432425|5885649|1941093|
|1122|193617216|84932640|8108100|5513508|3063060|
|114|29787264|13066560|1737450|1181466|656370|
|123|54991872|35388288|2837835|1324323|1660659|
|15|4582656|2949024|289575|135135|169455|
|222|11583936|11583936|540540|0|540540|
|24|4582656|4582656|270270|0|270270|
|33|2482272|2482272|180180|0|180180|
|6|381888|381888|32175|0|32175|
|total|1356147936|373451760|63050130|50960529|14915946|

22 relaxed raw/representative aggregate fields agree with the newly received author family audit, zero differences. Overlap with earlier shard checking is explicitly an algebraic crosscheck, not additional execution coverage. Relaxed common total 1029828840. Author family reports 561346627 affine nodes, two relaxed witnesses both already recomputed/excluded in prior Driver notes, zero valid leaves. Exact partition DP p(0..13)=[1,1,2,3,5,7,11,15,22,30,42,56,77,101] confirms symmetry-reduced expected global universe split 0..6: negative families [101,77,56,42,30,22,15], pairs [101,77,112,126,150,154,165], totals 343 and 885. This is an expected universe, not certification of coverage of all earlier families.

## Reproduction (executed JS; fetch exact two JSON inputs above as cert and audit)
```js
const C=(n,k)=>{if(k<0||k>n)return 0;let z=1;for(let i=1;i<=k;i++)z=z*(n-k+i)/i;return z},M=(n,k)=>k===0?1:C(n+k-1,k);
function D(n,a,b){let z=0;for(let j=0;j<=Math.min(n,a,b);j++)z+=(j%2?-1:1)*C(n,j)*M(n,a-j)*M(n,b-j);return z}
function R(n,a,b){let z=0;for(let c=0;c<=Math.min(a,b);c++)z+=D(n,a-c,b-c);return z}
const S=Array.from({length:7},(_,q)=>Array.from({length:12},(_,i)=>13*q+i+1).filter(x=>{for(const p of [2,3,5,7,11,13])while(x%p===0)x/=p;return x===1}));
const v=[];function rec(a,last){if(a.length===7){v.push(a);return}for(let i=last;i<12;i++)rec([...a,i],i)}rec([],0);
function row(lo,hi,real){let raw=0,dis=0,rep=0,rosters=0,n=real?S[1].length:12;for(let i=lo;i<hi;i++){const a=v[i];if(real&&a.some(x=>!S[1].includes(14+x)))continue;rosters++;const z=a.filter(x=>x===0).length;raw+=M(n,6);dis+=M(n-new Set(a).size,6);for(let c=0;c<=Math.min(6,z);c++)rep+=M(n-new Set(a.slice(c)).size,6-c)}return [rosters,raw,raw-dis,rep]}
for(const s of cert.shards){const a=row(s[0],s[1],false);if(a[1]!==s[2]||a[2]!==s[8]||a[3]!==s[3])throw Error('shard mismatch');console.log(s.slice(0,2),a,row(s[0],s[1],true))}
function counts(pos,real){let n=real?S[1].length:12,k=pos.filter(x=>x===1).length,f=1;for(let q=2;q<=6;q++)f*=M(real?S[q].length:12,pos.filter(x=>x===q).length);return [M(n,k)*M(n,7)*f,(M(n,k)*M(n,7)-D(n,k,7))*f,R(n,k,7)*f]}
for(const s of audit.summary){const a=counts(s.pos,false);if(a[0]!==s.search_domain||a[2]!==s.representative_search)throw Error('aggregate mismatch');console.log(s.pos,a,counts(s.pos,true))}
const p=Array(14).fill(0);p[0]=1;for(let k=1;k<=13;k++)for(let i=k;i<=13;i++)p[i]+=p[i-k];console.log(p);
```

## Control disposition
Original managed lane recovery dvr-20261128-1456-recovery-v1 successful; latest 50 own-session requests terminal (more historical requests exist). Original ready inventory dvr-20261128-1402-ready-queue-v1 SUCCEEDED, as-of 06:04:10Z (not live claim authority), counts NEEDS_DISPATCH 344, COMPLETE 145, BLOCKED 38, DORMANT 20; first page contains governance and researcher tasks including already performed handoffs. Do not infer 344 tasks are fresh unresearched. Prior T6 synthesis RETURN_TO_OWNER remains the existing disposition; no duplicate publication, no protected write, no Result acceptance or Task closure. P12 and P01 outstanding handoff/independent review; F7 formal review unresolved. Current advertised backend has no agent_launch. Next: reconcile exact earlier-family certificates and observation envelope, preserving author ownership.