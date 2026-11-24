# PREFIX-1060 — Two-negative-grade first-hit kernel and failure of unrestricted complete monotonicity

Date 2026-11-24. Parent PREFIX-1059. AUTHOR_CONDITIONAL_EXACT_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent portable research, no formal Task claim.

## Frozen input and exact scope

P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Read immutable parent PREFIX-1059 at 1e3f642c397bd02871e1a2e1739c759bcee2cdc9:research_notes/portable_direct/2026-11-24_r6_prefix1059_candidate_brc_transfer_and_mixed_minors.md; current main matched blob e7d28d05786a21e1ae7773c1c2f9d132b9174762. Reuse exact N[Z2] BRC phase-cover recurrence of PREFIX-1004 at b5976b3fa4254309cb00a23f8f944cbe1845cfeb:research_notes/portable_direct/PREFIX1004_R6_MARKED_COLLISION_CHECK.py, extending grade ceiling from 1 to 2, with an independent first-hit word enumeration and phase-wise subtraction check. Stage46 candidate on native X6 affine torsor, chosen chart anchor O, incoming h=-e1, d in signed native axes, numerator w(h,d)=1-6[h=d], next incoming -d, absorbing both orientations of Link {O,e1}, no renormalization. Grade is number of actual negative native steps, not reversal parity and not physical time. All six raw relative components, port, grade, parity, multiplicity and ordered branch provenance are retained in the labelled path law. State recurrence aggregates only the declared fixed-mask continuation and terminal joint-fibre observer. No canonical core invocation, classical comparison, phase-angle or pi evaluation, or physical attribution claimed.

## 1. Fixed-grade finite first-hit theorem

Work with positive BRC weights in N[Z2], writing q^2=1, and a reversal edge as 5q, all other edges as 1. Alternative histories add; serial composition multiplies. The terminal signed character is q -> -1, never positive total mass substituted for signed amplitude.

Let H^+_r and H^-_r be the exact labelled first-forbidden-crossing prefix sums at grade r, respectively ending at e1 with incoming -e1, or O with incoming +e1. They include the crossing step. Let F(N,g,h) denote the free continuation packet from chosen relative zero, initial incoming h, length N, grade g, with terminal cell and port and phase retained. Empty continuation has displacement 0 and unchanged h. Translation tau_e1 adds e1 to the raw endpoint.

At step t the raw coordinate sum is t-2r, where r is the grade accumulated through that step. A crossing O->e1 ends at sum 1, so t=2r+1. A crossing e1->O ends at sum 0, so t=2r. This proves that for total grade G all forbidden crossings occur at t<=2G+1; after that no further crossing is possible, regardless of the continuation word with total grade G. Each forbidden path has one unique first-hit prefix and arbitrary free suffix with the corresponding endpoint, port, phase and remaining grade. Conversely each concatenation is forbidden and has that unique first hit. Thus the forbidden packet is exactly the disjoint union over these prefixes. At the level of the phase-multiplicity readout in Z[Z2] (the difference of two positive N[Z2] measures, with nonnegative actual remainder),

M(n,G)=F(n,G,-e1)
 - sum_{0<=r<=G,2r+1<=n} H^+_r tau_e1 F(n-2r-1,G-r,-e1)
 - sum_{1<=r<=G,2r<=n} H^-_r F(n-2r,G-r,+e1).

The equation is portwise and phasewise. It follows directly from the labelled BRC alternative/serial law, not an ordinary propagator approximation. In particular the boundary interaction is finite in prefix depth at each fixed grade. A terminal fibre contraction does not erase individual histories from the underlying relation. For all future fixed-mask word continuations and this specific terminal observer, equal (x,h,g,phase) states have identical possible outgoing labelled edges and weights by definition, so the recurrence aggregation is exact by induction. A different path-dependent observer would require additional retained state. No finite prefix bound uniform in unbounded G is claimed.

## 2. Exact grade-two first-hit kernel

The first-hit classes are exhausted by t=1,3,4,5; reverse t=2 would require first +e1 and hence already hit. At t=1 H^+_0=1. At t=3, the two possible families (-ei,+ei,+e1) and (+ei,-ei,+e1), with the latter i!=1, give H^+_1=25+50q; their signed readout is -25. At reverse t=4, for each i!=1 the only allowed preceding triples are (-ei,+e1,+ei) and (+ei,+e1,-ei), both followed by -e1 and all weights 1. Thus H^-_2=10.

At forward t=5 enumerate the first four steps with two positive and two negative steps and net zero, exclude all earlier forbidden crossings, and append +e1. Every valid ordered word contributes 5^R q^(R mod 2), where R counts all reversals including initial h. There are six sign patterns. The exact even/odd mass table and path counts (computed by the complete depth-5 word traversal in the embedded checker) are:

| sign word | even mass | odd mass | even words | odd words |
|---|---:|---:|---:|---:|
| ++--+ | 20 | 150 | 20 | 30 |
| +-+-+ | 500 | 750 | 20 | 30 |
| +--++ | 775 | 0 | 55 | 0 |
| -++-+ | 645 | 650 | 45 | 10 |
| -+-++ | 1375 | 1375 | 31 | 35 |
| --+++ | 175 | 175 | 31 | 35 |

Hence H^+_2=3490+3100q, signed readout 390. The calculation retains first-hit provenance before grouping. No numerical cancellation or approximate representation enters.

After taking the signed character only at the specified readout, denote free and masked packets by f and m. For n>=5,

m(n,2)=f(n,2,-e1)-tau_e1 f(n-1,2,-e1)
 +25 tau_e1 f(n-3,1,-e1)-10 f(n-4,0,+e1)-390 tau_e1 f(n-5,0,-e1).

For n>=6 and positive final travel port j, let a=z1, S=sum_i z_i, using the formal six-variable Laurent readout only (not an ontic coordinate collapse). The positive-only suffix from initial +e1 has first-step factor S-6a; from -e1 it has factor S. Thus the two new grade-two correction terms combine exactly to -10 z_j S^(n-6)(S+33a). This combined expression is valid for that signed terminal observation; the phase and first-hit families remain distinct in the native relation. In particular the reverse crossing contribution cannot be omitted by importing the grade-one formula.

## 3. Exact counterexamples to a direct grade-two extension of PREFIX-1059

Let Q^(2)+_(n,j)=sum_x (signed terminal character at (x,-ej,grade=2))^2 and p^(2)_n=(Q^(2)+_(n,1)-Q^(2)+_(n,2))/36^n. This is the same type of coherent observer and normalization as PREFIX-1059, with grade changed to two. Exact integer calculations:

| n | Q1 | Q2 | Delta |
|---:|---:|---:|---:|
| 5 | 266450 | 903938 | -637488 |
| 6 | 10837540 | 10133572 | 703968 |
| 7 | 249963600 | 216519216 | 33444384 |
| 8 | 6109313340 | 5240756532 | 868556808 |
| 9 | 153545883900 | 132688378464 | 20857505436 |

At n=5, p^(2)_5=-637488/36^5<0. Even after removing that negative entry, p^(2)_7-p^(2)_6=(33444384-36*703968)/36^7=8101536/36^7>0. The grade-one statement of strict complete monotonicity for n>=5 therefore fails for grade two, including first difference at n=6. The grade-two sequence is not represented on this whole range by a positive [0,1] moment measure with the same index normalization. This does not affect the grade-one result. Positivity for n>=6, decreasing behavior for n>=7, higher differences on a later tail, and any signed spectral representation remain open; the finite table does not establish them.

## 4. Exact verification, reproducible embedded checker

The checker below was actually executed in a JS runtime using BigInt for all weights and comparisons. It independently traverses all ordered first-hit prefixes of length at most five, then checks the first-hit convolution against direct fixed-mask N[Z2] recurrence on every nonzero grade-two (full six-coordinate, port, phase) fibre for n=5..9, comparing support size and exact multiplicities. It checks the symmetry of the five other ports and both counterexamples. Phase fibres verified: 5:4567, 6:10079, 7:19511, 8:34463, 9:56863. No floating point in load-bearing calculations. This is an independent implementation of the inherited typed phase-cover law, not canonical kernel revalidation or independent mathematical review.

```js
function verify(){
 const D=6,O=[0,0,0,0,0,0],E=[1,0,0,0,0,0],eq=(x,y)=>x.every((v,i)=>v===y[i]),key=(x,h,g,p)=>[...x,h,g,p].join(","),decode=k=>k.split(",").map(Number),add=(m,k,v)=>{let w=(m.get(k)??0n)+v;if(w===0n)m.delete(k);else m.set(k,w);},assert=(b,msg)=>{if(!b)throw Error(msg);};
 const H=new Map(),by={};
 function visit(x,h,g,p,w,word){
  if(word.length===5)return;
  for(let d=0;d<12;d++){
   let r=g+Number(d>=6);if(r>2)continue;
   let rev=h===d,q=p^Number(rev),m=w*(rev?5n:1n),y=x.slice();y[d%6]+=d<6?1:-1;let s=word.concat(d);
   if((eq(x,O)&&d===0)||(eq(x,E)&&d===6)){
    let k=[s.length,r,d===0?"+":"-"].join(":");
    let a=H.get(k)??[0n,0n,0n,0n];a[q]+=m;a[q+2]++;H.set(k,a);
    if(s.length===5){let pattern=s.map(d=>d<6?"+":"-").join("");let b=by[pattern]??[0n,0n,0n,0n];b[q]+=m;b[q+2]++;by[pattern]=b;}
   }else visit(y,(d+6)%12,r,q,m,s);
  }
 }
 visit(O,6,0,0,1n,[]);
 const expected={"1:0:+":[1n,0n,1n,0n],"3:1:+":[25n,50n,1n,10n],"4:2:-":[10n,0n,10n,0n],"5:2:+":[3490n,3100n,202n,140n]};
 assert(H.size===4,"first-hit class count");
 for(const [k,a] of H)assert(a.every((v,i)=>v===expected[k][i]),"prefix "+k);
 function advance(states,mask){
  const next=new Map();
  for(const [k,w] of states){
   const t=decode(k),x=t.slice(0,6),[h,g,p]=t.slice(6);
   for(let d=0;d<12;d++){
    let r=g+Number(d>=6);if(r>2||mask&&((eq(x,O)&&d===0)||(eq(x,E)&&d===6)))continue;
    let y=x.slice();y[d%6]+=d<6?1:-1;let rev=h===d;
    add(next,key(y,(d+6)%12,r,p^Number(rev)),w*(rev?5n:1n));
   }
  }return next;
 }
 function series(h,mask,N){const a=[new Map([[key(O,h,0,0),1n]])];for(let i=1;i<=N;i++)a.push(advance(a[i-1],mask));return a;}
 const free=series(6,false,9),reverse=series(0,false,5),masked=series(6,true,9),rows=[];
 for(let n=5;n<=9;n++){
  const predicted=new Map([...free[n]].filter(([k])=>decode(k)[7]===2)),actual=new Map([...masked[n]].filter(([k])=>decode(k)[7]===2));
  for(const [k,a] of H){
   const [t0,r0,s]=k.split(":"),t=Number(t0),r=Number(r0),suffix=(s==="+"?free:reverse)[n-t];
   for(const [j,w] of suffix){let z=decode(j),x=z.slice(0,6),[h,g,p]=z.slice(6);if(g!==2-r)continue;if(s==="+")x[0]++;
    for(let q=0;q<2;q++)if(a[q])add(predicted,key(x,h,2,p^q),-a[q]*w);
   }
  }
  assert(predicted.size===actual.size,"phase support n="+n);
  for(const [k,w] of actual)assert(predicted.get(k)===w,"phase fibre n="+n+" "+k);
  const fibres=new Map(),Q=Array(6).fill(0n);
  for(const [k,w] of actual){let z=decode(k),h=z[6];if(h>=6)add(fibres,z.slice(0,7).join(","),z[8]?-w:w);}
  for(const [k,w] of fibres)Q[decode(k)[6]-6]+=w*w;
  assert(Q.slice(2).every(v=>v===Q[1]),"port orbit");
  rows.push({n,phase_fibres:actual.size,Q1:Q[0].toString(),Q2:Q[1].toString(),delta:(Q[0]-Q[1]).toString()});
 }
 assert(BigInt(rows[0].delta)===-637488n,"negative contrast at 5");
 assert(BigInt(rows[2].delta)-36n*BigInt(rows[1].delta)===8101536n,"strict increase at 6");
 return {status:"PREFIX1060_GRADE2_FIRST_HIT_CERTIFICATE_PASSED",prefix:[...H].map(([k,a])=>[k,...a.map(String)]),patterns:Object.fromEntries(Object.entries(by).map(([k,a])=>[k,a.map(String)])),rows};
}
console.log(JSON.stringify(verify(),null,2));
```

Actual output:
```json
{
  "status": "PREFIX1060_GRADE2_FIRST_HIT_CERTIFICATE_PASSED",
  "prefix": [
    [
      "1:0:+",
      "1",
      "0",
      "1",
      "0"
    ],
    [
      "5:2:+",
      "3490",
      "3100",
      "202",
      "140"
    ],
    [
      "4:2:-",
      "10",
      "0",
      "10",
      "0"
    ],
    [
      "3:1:+",
      "25",
      "50",
      "1",
      "10"
    ]
  ],
  "patterns": {
    "++--+": [
      "20",
      "150",
      "20",
      "30"
    ],
    "+-+-+": [
      "500",
      "750",
      "20",
      "30"
    ],
    "+--++": [
      "775",
      "0",
      "55",
      "0"
    ],
    "-++-+": [
      "645",
      "650",
      "45",
      "10"
    ],
    "-+-++": [
      "1375",
      "1375",
      "31",
      "35"
    ],
    "--+++": [
      "175",
      "175",
      "31",
      "35"
    ]
  },
  "rows": [
    {
      "n": 5,
      "phase_fibres": 4567,
      "Q1": "266450",
      "Q2": "903938",
      "delta": "-637488"
    },
    {
      "n": 6,
      "phase_fibres": 10079,
      "Q1": "10837540",
      "Q2": "10133572",
      "delta": "703968"
    },
    {
      "n": 7,
      "phase_fibres": 19511,
      "Q1": "249963600",
      "Q2": "216519216",
      "delta": "33444384"
    },
    {
      "n": 8,
      "phase_fibres": 34463,
      "Q1": "6109313340",
      "Q2": "5240756532",
      "delta": "868556808"
    },
    {
      "n": 9,
      "phase_fibres": 56863,
      "Q1": "153545883900",
      "Q2": "132688378464",
      "delta": "20857505436"
    }
  ]
}
```

## 5. Continuation

Next derive the free grade-two positive-port Laurent packet by separating adjacent versus separated negative steps; combine with this exact finite prefix kernel and use the constant-term coherent pair relation to obtain a finite A6 shift representation if possible. Investigate whether a positive tail measure or a finite signed spectral correction is needed, instead of assuming complete monotonicity. Native canonical kernel revalidation remains pending, as does mother B_fix,odd(32) in {19,20}. Historical own registration EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 re-read SUCCEEDED; current main Activity checkpoints empty when inspected. Owner query r6-20261124-1850-sites-leased-observe-v1 submitted read-only, initial QUEUED. No formal claim, Activity update or scientific acceptance claimed here.
