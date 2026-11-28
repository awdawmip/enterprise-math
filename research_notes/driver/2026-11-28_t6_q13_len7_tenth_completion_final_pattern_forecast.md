# T6 q13 length-seven tenth partition completed; final partition coverage forecast
2026-11-28; informed Driver EM-DVR-DEBB5E (same recovered logical lane; shared frozen context). Alternative combinatorial check, not independent affine-solver exhaustion or formal admission. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, p=q=13, valuation=1, split (6,7), budget 2331 per side. Author EM-DIRECT-D03BC9; previous audit 1c21b88ccba49188d6f1e8894a1cd5bc81a5635d; per-roster canonical cancellation proof 6425a7e23e2ba623af5a1f1056a3e57eea241c1a.

## Actual inputs
Paths research_checks/T6_P13_Q13_SPLIT6_7_LEN7_POS11112_SHARD<tag>_CERT_20261128.json; common frozen science and initializer prefix SHA256 22d0469739581b7cac3c5bdd3064859ef77255e656618e792af53d3a1427bee8 and kernel blob 89e0f5aea7f6efcfd79dc32f29b84fa510f5d95e matched.
|tag|source commit|blob|
|---|---|---|
|5000_15000|37e1a1dc911ae743f6abd016709e359ffa909060|5f533a7f13f8ecca36c36107ca5fdd2037b98bff|
|15000_31824|33bcce087ee2b25cb848a5063fb6b49ad89a3620|8bb1050405153ab03c8a2c4f3e9fc93e3581da22|
|0_5000 (previously audited, crosscheck only)|5fd72387bf088a14d5722c27d6eba0c7e92ea0af|7687f646fc6ae370d37a4f8ec96878581f2bbf2f|

## Exact actual audit
Neg (1,1,1,1,1,1,1) has 31824 lexicographic nondecreasing rosters over 12 atom residues. Pos (1,1,1,1,2) has four q=1 atoms and one q=2 atom. q=2 supplies factor 12; no q=2 negative atoms. The previous [0,5000) and six new contiguous shards [5000,31824) now cover the full tenth partition. 18 NEW field comparisons, 0 differences (plus six old fields checked). All counts in relaxed roster model. Nodes are author evidence, not independently enumerated solver nodes.
|lo|hi|raw|common|representative|author nodes|
|---:|---:|---:|---:|---:|---:|
|5000|5500|8190000|6871284|2053080|3082751|
|5500|10000|73710000|63218244|16510980|24517124|
|10000|15000|81900000|65635524|19939668|29485319|
|15000|20000|81900000|68316864|13583136|19816093|
|20000|25000|81900000|65598420|16301580|23859515|
|25000|31824|111777120|85384764|26392356|38152932|
|new total||439377120|355025100|94780800|138913734|
|whole tenth||521277120|419943888|120508752|178155751|

The author witness in 15000_31824: pos [[1,1],[1,2],[1,5],[1,10],[2,6]], neg [[1,4],[1,4],[1,4],[1,8],[1,12],[1,12],[1,12]], u=[27,-8,0,6,5,-2,6,-3,1,-2,2,0]. Recomputed using signed integer masses and modular inverse powers: positive 3211, negative 2825, residues [0,0,0,0,0,0] mod 13^k for k=1..6. Nonsmooth d values [23,17,17,17]. Both masses exceed 2331; not a valid witness.

## Final partition prospective exact counts (not executed affine search)
Pos (1,1,1,1,1,1), same neg. Author certificate 33bcce... declares next index 0. This table establishes a future crosscheck at 2500-roster intervals, not a claim that these intervals are the actual author's future boundaries.
|lo|hi|raw|common|representatives|
|---:|---:|---:|---:|---:|
|0|2500|30940000|26933360|6987047|
|2500|5000|30940000|27703470|5759380|
|5000|7500|30940000|28889865|3802326|
|7500|10000|30940000|28551015|4370531|
|10000|12500|30940000|27817104|5304706|
|12500|15000|30940000|27194610|3745390|
|15000|17500|30940000|28252409|2687591|
|17500|20000|30940000|28252837|2687163|
|20000|22500|30940000|26737317|4202683|
|22500|25000|30940000|28250329|2689671|
|25000|27500|30940000|27011218|3928782|
|27500|30000|30940000|27007156|3932844|
|30000|31824|22573824|18571990|4001834|
|total||393853824|351172680|54099948|

## Independent aggregate algebraic check
For n atom types, a positive and b negative atoms of one q-type, let M(n,k)=binom(n+k-1,k) for k>=0, M(n,0)=1. Disjoint multiset pairs have generating series per atom 1/(1-x)+1/(1-y)-1=(1-xy)/((1-x)(1-y)). Thus D(n,a,b)=sum_{j=0}^{min(n,a,b)} (-1)^j binom(n,j) M(n,a-j) M(n,b-j). All raw pairs = M(n,a)M(n,b), all common pairs = raw-D. Canonical representatives place all c common atoms at the least-cost residue; deleting those c gives a unique disjoint pair of sizes a-c,b-c, and reinsertion recovers the representative. Distinct c are disjoint classes because total common multiplicity is intrinsic to the pair. Therefore R(n,a,b)=sum_{c=0}^{min(a,b)}D(n,a-c,b-c). Independent aggregate computation using integer coefficients exactly agrees with both roster sums. Tenth per-c counts (including q=2 factor 12): 101333232,17008992,2018016,144144,4368. Final: 42681144,9510864,1673892,215292,17952,792,12. This is a crosscheck of established counting, not a new affine exhaustion.

## Reproduction (executed JS, compacted)
```js
const C=(n,k)=>{if(k<0||k>n)return 0n;let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n-k+i)/BigInt(i);return z},M=(n,k)=>k===0?1n:C(n+k-1,k);
const v=[];function rec(a,last){if(a.length===7){v.push(a);return}for(let i=last;i<12;i++)rec([...a,i],i)}rec([],0);
function row(lo,hi,k,f){let raw=0n,dis=0n,rep=0n;for(let i=lo;i<hi;i++){const a=v[i],z=a.filter(x=>x===0).length;raw+=M(12,k)*BigInt(f);dis+=M(12-new Set(a).size,k)*BigInt(f);for(let c=0;c<=Math.min(k,z);c++)rep+=M(12-new Set(a.slice(c)).size,k-c)*BigInt(f)}return [raw,raw-dis,rep]}
function D(n,a,b){let z=0n;for(let j=0;j<=Math.min(n,a,b);j++)z+=(j%2?-1n:1n)*C(n,j)*M(n,a-j)*M(n,b-j);return z}
function R(n,a,b){let z=0n;for(let c=0;c<=Math.min(a,b);c++)z+=D(n,a-c,b-c);return z}
// for each pinned cert j: each row s, compare row(s[0],s[1],4,12)
// to fields search_domain, common_feasible, representative_search in j.columns.
// for lo=0;lo<v.length;lo+=2500: row(lo,Math.min(lo+2500,v.length),6,1).
// compare aggregates to M(12,a)*M(12,7)*f, (M(12,a)*M(12,7)-D(12,a,7))*f, R(12,a,7)*f for (a,f)=(4,12),(6,1).
function pow(a,e,m){let r=1n;while(e>0n){if(e&1n)r=r*a%m;a=a*a%m;e>>=1n}return r}
function witness(w){let mass=L=>L.reduce((s,[q,r])=>s+13*(13*q+r)-1,0),a=mass(w.pos),b=mass(w.neg);for(let i=0;i<12;i++){a+=Math.max(w.u[i],0)*(13*(i+1)-1);b+=Math.max(-w.u[i],0)*(13*(i+1)-1)}let residues=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),phi=m-m/13n,inv=s=>pow(BigInt(s),phi-BigInt(k),m),r=0n;for(let i=0;i<12;i++)r+=BigInt(w.u[i])*inv(i+1);for(const [q,t] of w.pos)r+=inv(13*q+t);for(const [q,t] of w.neg)r-=inv(13*q+t);residues.push(Number((r%m+m)%m))}return {a,b,residues,nonsmooth:[...w.pos,...w.neg].map(([q,r])=>13*q+r).filter(d=>{for(const p of [2,3,5,7,11,13])while(d%p===0)d/=p;return d!==1})}}
```

## Control and boundaries
Own managed recovery dvr-20261128-1402-recovery-v1 succeeded; recent 50 requests all terminal; same lane SID, no replay. P12 original dvr-20261128-1306-p12-current-owner-v1 SUCCEEDED; observation 05:06:49Z, READY/NEEDS_DISPATCH no owner or claim, not a current write authorization. Fresh bounded backlog read dvr-20261128-1402-ready-queue-v1 queued; consume exact receipt. Original T6 synthesis RETURN_TO_OWNER remains closed as operation, nonterminal scientific scope. No native Review/Result admission/new Task closure/parent closure. F7 and P01 existing nonauthor review needs retained; no new agent launch/claim or schedule change. Next: actual author final partition certificates and observation-envelope audit; keep mathematical scope separate from author execution.
