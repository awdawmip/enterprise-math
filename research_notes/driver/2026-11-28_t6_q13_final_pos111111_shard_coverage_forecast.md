# T6 p13 q13 final positive partition: exact shard coverage audit and remaining combinatorial forecast
2026-11-28; EM-DVR-DEBB5E, shared frozen control context, alternative counting implementation relative to author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. No independent affine solver execution or mathematical admission.
 
## Evidence and scope
p=13, valuation=1, q=13, split (6,7), budget 2331; positive pattern (1,1,1,1,1,1), negative (1,1,1,1,1,2). Exact author certificates read at:
- bd8651911b4313c96bf9fc48df9d5a02391aa384:research_checks/T6_P13_Q13_SPLIT6_7_LEN6_POS111111_SHARD0_5000_CERT_20261128.json
- aca81e2be00a70e607f601dcb8519e2ad7c4c669:research_checks/T6_P13_Q13_SPLIT6_7_LEN6_POS111111_SHARD5000_15000_CERT_20261128.json
- 94ebb6aa3084837d4eb1961062c23e23e97e31e5:research_checks/T6_P13_Q13_SPLIT6_7_LEN6_POS111111_SHARD15000_20000_CERT_20261128.json
All share initializer prefix sha256 22d0469739581b7cac3c5bdd3064859ef77255e656618e792af53d3a1427bee8 and kernel blob 89e0f5aea7f6efcfd79dc32f29b84fa510f5d95e. Reuse proven per-roster formula 6425a7e23e2ba623af5a1f1056a3e57eea241c1a and prior audit 43c683f9a0e5cf07b6da192ab28d96bd0d8c0130. No repeated affine solving or claim.

## Exact audit
Lexicographically enumerate 4368 size-5 multisets v of 12 possible q1 residues, with q2 residue inner loop (12); total 52416 rosters. Each has M(12,6)=12376 positive candidates. Disjoint count M(12-|supp(v)|,6); canonical representative count sum over c=0..z of M(12-|supp(v-c e_min)|,6-c), z multiplicity of least residue. Common count = raw-disjoint. Minimal reinsertion preserves signed difference and minimizes both masses. This addresses combinatorial domain only, not affine completion. All 24 audited fields on [0,20000) match exact author certificates, with contiguous nonoverlapping ranges. Author reports 96184111 search nodes (32683940+41552591+21947580), zero leaves, zero valid; solver completeness remains author evidence. No witnesses to recalculate in these three certs.

| scope | raw | common | representatives |
|---|---:|---:|---:|
| audited [0,20000) |247520000|205889312|64525968|
| full relaxed roster (count only) |648700416|534570048|137025648|
| full true maximal-p13 smooth alphabet (count only) |27054027|23569623|4671009|

The full smooth-domain representative count is 96.5911% smaller than the full relaxed-domain count. The remainder [20000,52416) below is a combinatorial forecast, not an executed or verified author search; author may publish more after the observed pin. No owner interference.

Rows [lo,hi,raw,common,rep], actual alternate count; first eight are verified comparisons, rest forecast.
```json
[[0,2500,30940000,24022804,11555908],[2500,5000,30940000,25064416,9961952],[5000,7500,30940000,27569512,6002568],[7500,10000,30940000,26972476,6951516],[10000,12500,30940000,26669272,7430852],[12500,15000,30940000,26486320,7723144],[15000,17500,30940000,24218560,8845980],[17500,20000,30940000,24885952,6054048],[20000,22500,30940000,27099988,3840012],[22500,25000,30940000,26618452,4321548],[25000,27500,30940000,26585716,4354284],[27500,30000,30940000,24137248,6802752],[30000,32500,30940000,25769560,5170440],[32500,35000,30940000,26523148,4416852],[35000,37500,30940000,24791308,6148692],[37500,40000,30940000,25365508,5574492],[40000,42500,30940000,26166704,4773296],[42500,45000,30940000,24212004,6727996],[45000,47500,30940000,24843844,6096156],[47500,50000,30940000,24424480,6515520],[50000,52416,29900416,22142776,7757640]]
```
## Executed reproduction
```js
const C=(n,k)=>{if(k<0||k>n)return 0;let z=1;for(let i=1;i<=k;i++)z=z*(n-i+1)/i;return Math.round(z)},M=(n,k)=>k===0?1:C(n+k-1,k);
function multi(n,k){let out=[];function r(v,last){if(v.length===k){out.push(v);return}for(let i=last;i<n;i++)r([...v,i],i)}r([],0);return out}
const R=multi(12,5),expected=[[24022804,11555908],[25064416,9961952],[27569512,6002568],[26972476,6951516],[26669272,7430852],[26486320,7723144],[24218560,8845980],[24885952,6054048]];
let rows=[],diff=0;for(let lo=0;lo<52416;lo+=2500){let hi=Math.min(lo+2500,52416),raw=0,dis=0,rep=0;for(let i=lo;i<hi;i++){let v=R[Math.floor(i/12)],z=v.filter(x=>x===0).length;raw+=M(12,6);dis+=M(12-new Set(v).size,6);for(let c=0;c<=z;c++)rep+=M(12-new Set(v.slice(c)).size,6-c)}let row=[lo,hi,raw,raw-dis,rep];rows.push(row);if(lo<20000){let e=expected[lo/2500];diff+=Number(raw!==30940000)+Number(raw-dis!==e[0])+Number(rep!==e[1])}}
function allowed(q){return Array.from({length:12},(_,i)=>i+1).filter(r=>{let d=13*q+r;for(let p of [2,3,5,7,11,13])while(d%p===0)d/=p;return d===1})}
function D(n,a,b){if(a===0)return M(n,b);let z=0;for(let s=1;s<=Math.min(n,a);s++)z+=C(n,s)*C(a-1,s-1)*M(n-s,b);return z}
let n=allowed(1).length,m=allowed(2).length;let raw=M(n,6)*M(n,5)*m,dis=D(n,6,5)*m,rep=Array.from({length:6},(_,c)=>D(n,6-c,5-c)).reduce((a,b)=>a+b,0)*m;
console.log({rosters:R.length*12,rows,diff,partial:rows.slice(0,8).reduce((a,r)=>a.map((x,j)=>x+r[j+2]),[0,0,0]),full:rows.reduce((a,r)=>a.map((x,j)=>x+r[j+2]),[0,0,0]),smooth:{n,m,raw,common:raw-dis,rep}})
```
## Control
Current backend 0.6.11. Own managed recovery dvr-20261128-1103-own-recovery-v1 succeeded; recent 50 durable requests include original T6 synthesis SUCCEEDED and F7 exact flow SUCCEEDED, no in-flight writes in returned scope (has_more_requests true). Site recovery IDs are not durable control_result IDs; original dvr-20261128-1000-own-recovery-v1 lookup returned CONTROL_REQUEST_NOT_FOUND, metadata recovery used instead. Current capabilities read dvr-20261128-1103-contract-read-v1 confirms reference requires actual review and synthesis exact set. P12 original read dvr-20261128-0903-p12-current-owner-v1 confirmed SUCCEEDED, READY/NEEDS_DISPATCH, no owner or claim as of 01:06:33Z only. No new review/Result acceptance, Task or parent closure. F7 historical input-budget failure not replayed. No dispatch or schedule changes.
