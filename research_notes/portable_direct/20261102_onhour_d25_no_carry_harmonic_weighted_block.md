# D25: exact no-carry harmonic transport of original weighted blocks (2026-11-02)

**AUTHOR-DERIVED / EXACT GENERAL LEMMA / 7,606 FINITE EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT.**

- Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific pin `c47e13e4aba0e006366f989d6333ae3` unchanged.
- Previous source-separated exceptional-carry port: `cf1bd3565d9a3277307830de6182ee763221184c:research_notes/portable_direct/20261102_onhour_d25_source_separated_anomalous_port.md`.
- Mother target remains original `Delta_p-R_p=0 (mod p)` for **all p=13,19 (mod24)**, a true original-definition counterexample or a strict equivalent reduction. Not a closure claim.

## 1. Original valuations and no-carry unit theorem

For each prime `p>3`, `k=ap+b`, `0<=a,b<p`, retain original integer factorial coefficients
```
A_k=(2k)!(3k)!/(k!)^5; W weighted term w_k=(6k+1)A_k/216^k;
B_k=(4k)!/(k!)^4;  S weighted term s_k=(8k+1)B_k/2304^k.
```
Define p-free factorial unit `U_p(x)=x/p^{v_p(x)}`, unweighted source units `u_k=U_p(A_k)*216^(-k)`, `v_k=U_p(B_k)*2304^(-k)`, each modulo p². Define `H_t=sum_(1<=j<=t) 1/j (mod p)` and Fermat quotient `q_p(d)=(d^(p-1)-1)/p (mod p)`.

**For every 3b<p**, no new carry occurs in source W, and
```
v_p(A_(ap+b))=v_p(A_a), v_p(A_b)=0;
u_(ap+b)/(u_a*u_b) =
  1+p*a*(2H_(2b)+3H_(3b)-5H_b-q_p(216)) (mod p²).        (W)
```
**For every 4b<p**, analogously in source S,
```
v_p(B_(ap+b))=v_p(B_a), v_p(B_b)=0;
v_(ap+b)/(v_a*v_b) =
  1+p*a*(4H_(4b)-4H_b-q_p(2304)) (mod p²).              (S)
```

**Proof.** For `n=qp+r, 0<=r<p`, separate n! into multiples of p and complete/partial nonmultiple blocks:
```
U_p(n!) = U_p(q!) * prod_(0<=t<q) prod_(1<=i<p)(tp+i)
                   * prod_(1<=i<=r)(qp+i).
```
Since `H_(p-1)=0 (mod p)`, complete blocks are `(p-1)!` modulo p²; the partial block is `r!*(1+qpH_r)`. Hence
```
U_p((qp+r)!) = U_p(q!)*((p-1)!)^q*r!*(1+qpH_r) (mod p²).
```
For `3b<p`, apply this to 2(ap+b), 3(ap+b), and ap+b. The `U_p((ja)!)` and `((p-1)!)^(ja)` components cancel across factorial exponents 2+3-5=0, leaving `2H_(2b)+3H_(3b)-5H_b`. The 4-4 cancellation similarly leaves `4H_(4b)-4H_b`. Finally Fermat gives `d^(-ap)=d^(-a)*(1-pa q_p(d)) (mod p²)`. All displayed unit divisions are valid, including when the unnormalized factorial is divisible by p.

## 2. Original weighted observer: no divide-by-zero at exceptional weights

Write `F_W(b)=2H_(2b)+3H_(3b)-5H_b-q_p(216)` and `F_S(b)=4H_(4b)-4H_b-q_p(2304)` in F_p. The **p-adically normalized original weighted terms** satisfy
```
w_(ap+b)/p^{v_p(A_a)} =
 u_a*u_b * [(6b+1) + p*a*(6+(6b+1)*F_W(b))] (mod p²), for 3b<p;

s_(ap+b)/p^{v_p(B_a)} =
 v_a*v_b * [(8b+1) + p*a*(8+(8b+1)*F_S(b))] (mod p²), for 4b<p.
```
The affine form retains the original (6k+1)/(8k+1) weights and signed provenance. It is valid **even where a weight vanishes mod p**; unjustified weight inversion would have lost that jet contribution. Arithmetic indices are external auxiliary charts, not P000 native X6 coordinates.

## 3. Exact programmatic check and next obligation

A separate standard-library integer checker constructed factorial p-valuations and p-free factorial units mod p². It compared four independent expressions per selected pair: raw factorial unit ratio, harmonic formula, denominator Fermat-quotient transport, and original weighted affine lift. Exhaustive `0<=a<p, jb<p` for both original sources at p=5,7,13,19,37,43,61,67 plus boundary-sampled p=109,139,373 produced **7,606 exact pair checks, all PASS**. This is finite implementation evidence; general scope is from the factorial-block proof, not numerical extrapolation.

New information: (W)/(S) supplies the explicitly sourced next-digit harmonic correction to the **nonanomalous, no-carry blocks**, beyond the prior anomaly leading port. It does not yet give a full WZ telescope nor prove mother Delta-R. The next exact action is extend through the adjacent carry boundary at order p³/p⁴, form a signed source-preserving compensator for the anomaly from the nonanomalous blocks, check both p=13 and 19 classes, and return to original Delta-R.

Fixed373 native H0/B0 divided-power [X]U modulo139129, module rank, actual semilinear Frobenius direction/eta, odd signed Green/Hesse, kappa, and independent review remain `PENDING_OWNER / NOT_EXECUTED` (Enterprise Math #1559). An ordinary scalar checker does not substitute.

Research ordinary-control lane is solely `chatgpt-research-onhour-enterprise-math-20260923`. The failed historical `research-onhour-20261031-0205-dispatch-r15` was independently read as terminal FAILED / UPSTREAM_CODE_REVIEW_REQUIRED (kimi-query-bridge #6633); not resent. No current authenticated own Researcher session, CLAIM, run or Source checkpoint. This author-side note is neutral evidence preservation, not a Research Activity registration, Result or formal mathematical admission. No scheduler or notification change.
