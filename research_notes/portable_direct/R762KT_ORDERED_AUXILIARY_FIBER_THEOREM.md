# R762KT — Ordered auxiliary Port–Euler provenance: exact counts and exponential mixing

2026-11-24 · AUTHOR_PROVED / EXACT_JS_CHECKED / NOT_REVIEWED
Researcher: EM-DIRECT-82A007 (registration receipt r3-20261124-0124-own-research-registration-v1; recovery metadata, no execution authorization).
Continuation: R762KS@3a9ade48b57dbac10307513acb35051b6f7e3014; R762KN@2ca3fe1ff671a44a1ec4ed4cb90653870a7ddaf7. Frozen P000 a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json and joint-relation companion. This is a combinatorial extension of the *unsigned auxiliary* M3 model, not a physical heartbeat evolution. No native sign, phase, Cell location, slice common depth or BRC dynamics is assumed to factor through these words. No native calculation or classical reference simulation is undertaken.

## KT.1 — Time-order lift with a specified schedule

Use the same eight labeled supports (i,j,k) in {0,1}^3 and active Port vertices A_ij, B_ik, C_jk. The three edge colors AB, AC, BC have XOR boundary vectors e_s,c. Forced edges connect the three four-vertex components internally; F consists of the 512 boundaries even on each component. Fix positive stock m_s, N=sum m_s. A source is now a word of m_s edge colors at each support, not an unordered triple. Equivalently fix any schedule of support occurrences and preserve the order of colors at its occurrences. No extra Euler-traversal-order requirement is imposed; connectivity and parity are the inherited static tests. The local branch family has one unit-weight labeled branch per color, composition is concatenation, and the boundary observation is XOR. This is an explicit finite positive-count branch carrier consistent with the BRC typed distinction; Walsh character signs below are only coefficient extraction, not amplitude cancellation.

Write R_m(b) for the number of ordered sources with boundary b in F and connected quotient. In the integer group algebra let J_s=X^{e_s,1}+X^{e_s,2}+X^{e_s,3}; then
```
R_m(b) = [X^b] product_s J_s^{m_s} - sum_{c=1}^3 1_{b=v_c}
v_c = XOR_{s:m_s odd} e_s,c.
```
Proof: each word contributes one branch to the group algebra product; nonconnected quotient means precisely one color is used throughout, giving three words with the stated boundaries. This is an exact refinement of KN.1 (unordered multisets). In particular each old triple tuple n_{s,c} has exactly product_s (m_s! / product_c n_{s,c}!) refinements. Summing these weights over the old fiber gives R_m(b), not Q_m(b) times a universal factor.

The quotient parity character average (four characters of the even component-parity plane) gives the total over F:
```
sum_b R_m(b) = (3^N+3*(-1)^N)/4 - 3*1_{N even}.
```
The trivial character gives 3 per event, each other character gives -1. If the support schedule itself is also a freely ordered word of the prescribed inventory, multiply every fiber by N!/product_s m_s!: each such support word admits the same independent within-support color words. This counts labeled support/color event words, not physical time trajectories.

## KT.2 — Closed maximum and uniform boundary mixing for all m>=2

Take uniform m_s=m and T=3^m. For character x in F_2^12 define k(x) as the number of support triangles on which the three vertex bits are not all equal. A character has local sum 3 for a constant triangle and -1 otherwise (a triangle has zero or two crossing edges). Thus
```
R_m(b) = (1/4096) sum_x (-1)^{x dot b + m*k(x)} T^{8-k(x)}
         - 3*1_{b=0}.
```
Here v_c=0 for all three colors because each Port appears twice across all supports. The exact distribution h_k=#x with k(x)=k is
(2,0,24,64,396,768,1432,960,450).
It follows by enumerating the 4096 binary assignments to the 12 edges of the cube (each Port is the shared vertex of two support triangles); the complete construction and verification code below generates every assignment once.

In particular k=0 gives the two constant assignments. The k=2 characters are the 12 singleton Port flips and their complements: every other vertex in the support cube is constant; deleting two cube vertices leaves a connected graph, and only adjacent deleted vertices have a shared Port not forced by that connected complement. Alternatively the 24-character count, together with these 24 explicitly distinct witnesses, proves completeness. Therefore for b in F nonzero, exactly 2*wt(b) characters with k=2 have x dot b=1. There is no k=1 term.

Let c_k(b)=#x with k(x)=k and x dot b=1. Subtract:
```
R_m(0)-R_m(b) = (1/2048) sum_k c_k(b)(-1)^{m*k} T^{8-k} -3.
```
For even m>=2 this is at least 4*T^6/2048-3>0 since wt(b)>=2. For odd m>=3, discard the positive k>=4 terms and bound the negative terms using h_3,h_5,h_7:
```
2048*(R_m(0)-R_m(b)+3)
 >= 4*T^6 -64*T^5 -768*T^3 -960*T.
```
For T>=27, the right side exceeds 6144: divide by T^5 and use 4*T-64-768/T^2-960/T^4 > 42. Hence zero is the unique maximizer for every integer m>=2. No extrapolation from sample m is used.

The exact maximum is
```
R_m(0) = (2*T^8+24*T^6+64*(-1)^m*T^5+396*T^4
           +768*(-1)^m*T^3+1432*T^2+960*(-1)^m*T+450)/4096 -3.
```
For each fixed nonzero b in F (uniform over this finite set), the leading difference is 2*wt(b)*T^6/2048, giving
```
(R_m(0)-R_m(b))/R_m(0) = 2*wt(b)*3^(-2m)+O(3^(-3m)).
```
Thus *ordering changes the relative mixing scale from the unordered polynomial regime to exponential*. This is a combinatorial statement about declared observer fibers, not a physical rate or time law.

## KT.3 — Information and observation scope

For known stock, boundary and connectedness, recovering a fixed-schedule ordered source has exact worst-case fixed-width cost ceil(log2(max_b R_m(b))) bits. The lower bound is counting; an enumerative code attains it by lexicographically ranking the finite words. A practical prefix coder can replace KS local unordered multiplicities by unit color transitions and use remaining-stock, boundary and the five-state connectivity automaton; exact implementation is the next unit. For uniform m the bit budget is 8*m*log2(3)-11+O(1), compared with KN's 16*log2(m)+O(1) for unordered triples. If support schedule is also unknown, add its log-multinomial to the log fiber size before taking the ceiling. By Stirling, for uniform m this yields 8*m*log2(24)-3.5*log2(m)+O(1). These bounds concern exact recoverability, not an assertion that every physical observer needs the entire history.

Explicit collision: choose one support with counts (1,1,0), and all other support stocks and choices so the full boundary is in F (for example every support uses one AB and one AC, so every Port is even and the quotient connected). Swapping AB,AC to AC,AB at that first support leaves even the complete KS unordered source tuple fixed, but changes the first color readout on that support. The per-support prefix observer distinguishes them. Thus the old code is not sufficient for this declared ordered observer. A native signed lift still requires a typed source-to-BRC operation law, signs, time, the third slice coordinate/common-depth repair, and proof that the allowed native observations distinguish or factor through the proposed carrier. Retain source data until that law is verified.

## Exact evidence

Executed JavaScript BigInt independent event-by-event XOR recurrence versus full character sum for all 512 boundaries and m=1..6 (3072 count comparisons); checked leading coefficients for all 511 nonzero boundaries; exact totals, histogram and maxima. Result:
```json
{
  "h": [
    2,
    0,
    24,
    64,
    396,
    768,
    1432,
    960,
    450
  ],
  "rows": [
    {
      "m": 1,
      "q0": "6",
      "max": "8",
      "total": "1638",
      "gap": "-2",
      "bits": 3
    },
    {
      "m": 2,
      "q0": "25854",
      "max": "25854",
      "total": "10761678",
      "gap": "2454",
      "bits": 15
    },
    {
      "m": 3,
      "q0": "139998822",
      "max": "139998822",
      "total": "70607384118",
      "gap": "629592",
      "bits": 28
    },
    {
      "m": 4,
      "q0": "906508619358",
      "max": "906508619358",
      "total": "463255047212958",
      "gap": "596202558",
      "bits": 40
    },
    {
      "m": 5,
      "q0": "5937553576329126",
      "max": "5937553576329126",
      "total": "3039416364764232198",
      "gap": "392492009760",
      "bits": 53
    },
    {
      "m": 6,
      "q0": "38949341238809814174",
      "max": "38949341238809814174",
      "total": "19941610769218127465838",
      "gap": "295590166811574",
      "bits": 66
    }
  ],
  "checks": 3072,
  "leadingChecks": 511
}
```

Reproduction (standalone JavaScript, e.g. Node):
```javascript
function verify(){
const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
const masks=[];for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let k=0;k<2;k++){const a=1<<(2*i+j),b=1<<(4+2*i+k),c=1<<(8+2*j+k);masks.push([a|b,a|c,b|c])}
const F=Array.from({length:4096},(_,b)=>b).filter(b=>[15,240,3840].every(x=>pc(x&b)%2===0));
const h=Array(9).fill(0);const ks=Array.from({length:4096},(_,x)=>{const k=masks.filter(es=>es.some(e=>pc(x&e)%2)).length;h[k]++;return k});
if(h.join(",")!=="2,0,24,64,396,768,1432,960,450")throw Error("histogram");
const per=F.filter(x=>x).map(b=>{const c=Array(9).fill(0);for(let x=0;x<4096;x++)if(pc(x&b)%2)c[ks[x]]++;if(c[2]!==2*pc(b))throw Error("leading coefficient");return {b,c}});
const rows=[];
for(let m=1;m<=6;m++){const t=3n**BigInt(m);let dist=Array(4096).fill(0n);dist[0]=1n;for(const es of masks)for(let j=0;j<m;j++){const n=Array(4096).fill(0n);for(let x=0;x<4096;x++)for(const e of es)n[x^e]+=dist[x];dist=n}dist[0]-=3n;let sum=0n,max=0n,gap=null;
for(const b of F){const raw=ks.reduce((a,k,x)=>a+t**BigInt(8-k)*((m*k+pc(x&b))%2?-1n:1n),0n);if(raw%4096n!==0n||raw/4096n-BigInt(b===0?3:0)!==dist[b])throw Error("mismatch");sum+=dist[b];if(dist[b]>max)max=dist[b];if(b!==0&&(gap===null||dist[0]-dist[b]<gap))gap=dist[0]-dist[b]}
if(sum!==(3n**BigInt(8*m)+3n)/4n-3n)throw Error("total");if(m>=2&&gap<=0n)throw Error("max");
rows.push({m,q0:String(dist[0]),max:String(max),total:String(sum),gap:String(gap),bits:(max-1n).toString(2).length})}
return {h,rows,checks:6*F.length,leadingChecks:per.length}
}
console.log(JSON.stringify(verify(),null,2));
```

Next: derive and implement the prefix coder for a specified support schedule and signed carrier only after its actual native operation/observer semantics are pinned. Explore whether limited future observations permit smaller order residuals, preserving the distinction between positive count and signed amplitude. No formal Task/CLAIM/PROGRESS/Result or independent Review is asserted.
