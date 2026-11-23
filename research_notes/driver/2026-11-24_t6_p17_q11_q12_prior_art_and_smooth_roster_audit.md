# T6 p17 q11/q12: prior-art and smooth-roster reconciliation

Date 2026-11-24 (Asia/Shanghai). Existing Driver logical continuation EM-DVR-DEBB5E, prior own checkpoint r534. Scope: nonauthor roster/count audit of EM-X6-FB6990's November 23 certificates, and correction of this Driver's own novelty/frontier assessment. No new Native review, Result or Task closure.

## Source evidence and correction

Read original author [q11 certificate](https://github.com/awdawmip/enterprise-math/blob/12659bae30760e74ad01ece1a15c6dcf789bda0a/research_checks/T6_P17_Q11_ALL_THREE_SPLITS_AUTHOR_CERT_20261123.json) (blob f0aa07fd908bf17d62f5d9f3e2cdbd71f7c4ca92), original [generator](https://github.com/awdawmip/enterprise-math/blob/12659bae30760e74ad01ece1a15c6dcf789bda0a/research_checks/T6_P17_Q9_INTERVAL_GENERATOR_20261123.py) (blob 80f212a57c57429c4a61a06d4b7f9353240aef75), [interval checker](https://github.com/awdawmip/enterprise-math/blob/12659bae30760e74ad01ece1a15c6dcf789bda0a/research_checks/T6_P17_Q8_INTERVAL_EXHAUSTIVE_CHECK_20261123.cpp) (blob a4994b5aa6f0d99f08116d811cfb1a30547a390f), and [exact q5 kernel](https://github.com/awdawmip/enterprise-math/blob/12659bae30760e74ad01ece1a15c6dcf789bda0a/research_checks/T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py) (blob 2c1aa73268aa11300a32b9923e3bdbddb6190813). Original author certificate reports q11 (3,8), (4,7), (5,6) zero relaxed sphere leaves, including **39,855,088 primitive (4,7) pairs**. It predates this Driver's q11(5,6) certificate. Original author [q12 certificate](https://github.com/awdawmip/enterprise-math/commit/8d355aa8dbb43dfa55189e7dbe36bb11261746cd) similarly covers (4,8), (5,7), (6,6) with zero leaves; [q10 author certificate](https://github.com/awdawmip/enterprise-math/commit/d5a4193e3030d356c01bc66c20618e228849186e) covers all four literal splits. All original author results are unreviewed/not admitted. The q11(4,7) family is **not unresearched**; the next action is verification/reuse, not new full enumeration or a duplicate allocation. Driver five-adic q11(5,6) and q12 results are alternative exact methods, not a second newly eliminated denominator range.

## Actual independent roster audit

In the original integer T6 model, after v17>=2 cancellation, a vertical atom is d=17(17q+r), q>=1, 1<=r<=16, mass 289q+17r-1, cap 2331 per side. Actual maximal-prime-17 atoms require cofactor 17q+r to be 17-smooth. Since r is nonzero modulo 17, test smoothness by division by 2,3,5,7,11,13. The original interval generator intentionally enumerates the **larger literal roster** without this filter. Thus its empty-search conclusion, if validated, covers the smooth subdomain; the 8697 vs 1907 q7 counts are not conflicting counts of the same domain.

Independent JS recursion enumerated nondecreasing atom indices and multiplicity exactly, enforcing q sum and cap. Results:

|q|literal roster|smooth roster|
|--:|--:|--:|
|3|1088|493|
|4|6460|2316|
|5|30040|8573|
|6|47628|11105|
|7|8697|1907|
|8|1|0|

Literal atoms=113; smooth atoms=60. q8 has only q=8,r=1, cofactor 137 (prime), cost 2328; two atoms would cost >=8*289+32=2344, and q8,r>=2 costs >=2345. Consequently actual smooth q8 is impossible. This elementary subdomain argument agrees with earlier Driver q14 unique-split mass/smoothness record; no novelty claim. Smooth q4 minimum is 1188, hence correct q0 ceiling 1143.

The independently executed (4,7) support-intersection audit found:

|carrier|raw pairs|shared named atom|primitive pairs|
|---|---:|---:|---:|
|literal|56,182,620|16,327,532|39,855,088|
|smooth|4,416,612|1,509,958|2,906,654|

Literal counts match the original certificate exactly. Smooth primitive count is a smaller verified domain for any later independent targeted check. Here shared means at least one exact equal named vertical denominator; no coordinate or factor quotient. The opposite common term can be removed in cancellation-normalized analysis.

Reproduction (JavaScript, exact integer operations in these bounds):
```js
const cap=2331, atoms=[];
const smooth=a=>{for(const p of [2,3,5,7,11,13])while(a%p===0)a/=p;return a===1};
for(let q=1;q<=8;q++)for(let r=1;r<=16;r++){
  const cost=289*q+17*r-1;
  if(cost<=cap)atoms.push({q,r,cost,smooth:smooth(17*q+r)});
}
function states(q,s){
  const out=[];
  function rec(i,left,c,m){
    if(!left){out.push({c,m});return}
    for(let j=i;j<atoms.length;j++){
      const a=atoms[j];if(a.q>left)break;
      if(c+a.cost>cap||(s&&!a.smooth))continue;
      const n=m.slice();n[j>>5]|=1<<(j&31);
      rec(j,left-a.q,c+a.cost,n);
    }
  }
  rec(0,q,0,[0,0,0,0]);return out;
}
function count(a,b){
  let shared=0;for(const x of a){const [a0,a1,a2,a3]=x.m;
    for(const y of b){const m=y.m;
      if((a0&m[0])||(a1&m[1])||(a2&m[2])||(a3&m[3]))shared++;
    }}
  const raw=a.length*b.length;return {raw,shared,primitive:raw-shared};
}
for(const s of [false,true]){
  console.log(Array.from({length:6},(_,i)=>states(i+3,s).length));
  console.log(count(states(4,s),states(7,s)));
}
```

## Partial semantic check of original interval method

The six congruences in the full global mixed problem are sum of signed reciprocal cofactor powers modulo 17^k, k=1..6. The q0 variables span Z^16. The map to the product of residue groups is onto: choose six distinct inverse residues 1/r (r=1..6); the 6x6 matrix of powers k=1..6 is a Vandermonde times nonzero column factors modulo 17. Its determinant is a unit modulo 17^6, so arbitrary targets lifted to Z/17^6 are attained and reduction to the separate moduli is surjective. The homogeneous kernel has index 17^(1+...+6)=17^21. Thus the original code's checks of determinant and all row congruences suffice for saturation, not merely membership. Signed q0 mass constraints imply weighted squared norm at most the sum of squared remaining side budgets. The original C++ source uses outward bounds, accumulates lower GS energy, and propagates original affine coefficients rather than orthogonalized centers. This turn inspected these source formulas and reproduced the roster/support counts, **not** the complete interval search or its machine-width bound. A full nonauthor computational audit still needs an independent run and verification of the outward arithmetic bounds/particular lifts. The original authors' actual finite execution is preserved without upgrading its admission state.

## Next action

Consume current T6 owner read, maintain existing owner and author history. Prior q11/q12 results should be linked for independent review; do not issue an overlapping new execution task. Check remaining p17 author q13/q14 and lower-order certificates for scope and prior art before new research. No Native review, Result admission, Task completion or mother closure.
