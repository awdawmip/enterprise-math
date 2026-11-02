# D25: complete first harmonic transport across every two-digit carry boundary (2026-11-02)

**AUTHOR-DERIVED / PROVED GENERAL FACTORIAL LEMMA / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.**

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6333ae3` unchanged. Consumes source-specific anomalous note `cf1bd3565d9a3277307830de6182ee763221184c` and earlier no-carry harmonic note `cc20294b3fad0b1a9474b1c4dcbe4820f2498818`. Mother target remains original `Delta_p-R_p=0 (mod p)` for every prime p=13,19 (mod24), or a genuine counterexample / strict equivalent reduction.

## Theorem: all boundaries, first next-digit unit

Let p>3 prime, 0<=a,b<p, k=ap+b. Define unweighted original source terms
`C_W(k)=((2k)!(3k)!/(k!)^5)/216^k` and `C_S(k)=((4k)!/(k!)^4)/2304^k`. Put `v_X(k)=v_p(C_X(k))`, `U_X(k)=p^{-v_X(k)}C_X(k)`. Here a p-free integer unit is `U_p(n)=n/p^{v_p(n)}`, whereas `U_p(n!)` denotes the p-free factorial. Define `H_r=sum_(t=1..r) t^{-1} mod p`, `q_p(d)=(d^{p-1}-1)/p mod p`.

For each j=2,3,4 set `c_j=floor(jb/p)`, `r_j=jb-c_j*p`, `delta_j=floor(((ja mod p)+c_j)/p)`, and the explicit small carry factor
`Gamma_j=(1/c_j!) product_(t=1..c_j) U_p(ja+t) mod p^2`.
Here 0<=c_j<=3 and all denominators are p-units.

The exact identities in Z/p^2Z are:

```
U_W(ap+b)/(U_W(a)U_W(b))
 = Gamma_2 Gamma_3 (1+pa L_W(b))  (mod p^2);
L_W(b)=2H_(r_2)+3H_(r_3)-5H_b-q_p(216)  (mod p).

U_S(ap+b)/(U_S(a)U_S(b))
 = Gamma_4 (1+pa L_S(b))          (mod p^2);
L_S(b)=4H_(r_4)-4H_b-q_p(2304)   (mod p).

v_W(ap+b)=v_W(a)+v_W(b)+delta_2+delta_3;
v_S(ap+b)=v_S(a)+v_S(b)+delta_4.
```

**Proof.** For N=qp+r, 0<=r<p, removing all p factors gives
`U_p(N!)=U_p(q!)((p-1)!)^q r! (1+pqH_r) mod p^2`.
Partition into p-multiples, complete p-free blocks (using H_(p-1)=0 mod p), and the final incomplete block. Apply this identity to j(ap+b), jb, ja, ap+b, b, a. The ratio of the j-th factorial against its j-fold base contribution is `Gamma_j(1+pja(H_(r_j)-H_b))`: complete block factors cancel. Multiply j=2,3 or j=4 and retain the original denominator `d^{-ap}/d^{-a}=1-pa q_p(d) mod p^2`. The valuation formula is the high-digit carry in Legendre's factorial formula. All divisions are p-units.

The original weighted observers are preserved without dividing by weights that can vanish mod p:

```
w_(ap+b)/p^vW(ap+b) =
 U_W(a)U_W(b)Gamma_2Gamma_3
 [(6b+1)+pa(6+(6b+1)L_W(b))]   (mod p^2);
s_(ap+b)/p^vS(ap+b) =
 U_S(a)U_S(b)Gamma_4
 [(8b+1)+pa(8+(8b+1)L_S(b))]   (mod p^2).
```

This extends the earlier `3b<p / 4b<p` no-carry formula across all low/high carry boundaries. Its source tuple (W/S, a,b, valuation, c,delta,Gamma, signed weight, modulus) is an auxiliary BRC observer, **not** a native X6 coordinate or an information-erasing statement about P000.

## Consequence: full anomaly modulo p^4 occupies only low rows

For p=6m+1 in the target classes, the complete anomalous W population modulo p^4 consists of row a=2m, with valuation 2 on 2m<b<=3m and valuation 3 on 3m<b<=4m. Remaining W anomalous terms have valuation >=4. For p=13 mod24, the complete anomalous S population mod p^4 is row a=(p-1)/4, valuation 2 on (p-1)/4<b<=(p-1)/2 and valuation 3 on (p-1)/2<b<=3(p-1)/4. For p=19 mod24, all anomalous S terms have valuation >=4. These support statements follow by Legendre valuations and the previous source-typed row classification.

The new formula computes a valuation-2 summand mod p^4 from its unit mod p^2 and a valuation-3 summand from its unit mod p. In particular the entire signed anomalous source modulo p^4 can now be evaluated from only low-index units, bounded carry factors, and harmonic sums, without high-index factorial recomputation.

## Direct exact checks and p=373 discriminator

An independent Python integer checker computed both (a) direct p-free factorial units at k=ap+b and (b) the small-carry/harmonic prediction. **3,488 exact (source, a,b) comparisons** passed: full a,b enumeration for p=5,7,13,19; selected complete relevant boundary rows and control indices for p=37,43,61,373. Anomalous row sums were separately accumulated from original weighted source terms mod p^4.

| p | W anomalous p^2,p^3 digits | S anomalous p^2,p^3 digits | signed (W-2S) digits |
|---:|---:|---:|---:|
|13|7,10|7,1|6,7|
|19|1,5|0,0|1,5|
|37|12,11|25,25|36,33|
|**373**|**87,40**|**228,53**|**4,306**|

For p=373 and p^4=19,356,878,641, the original W low anomaly row sums to **2,087,908,903**, the original S low anomaly row sums to **2,782,162,613**, and the signed anomaly is **15,880,462,318** mod p^4. The signed p^3 digit includes the borrow `40-2*53-1=-67=306 mod373`. These first two digits match the earlier full anomalous certificate `4,306,266` mod p^5; at p^4, other anomaly rows disappear by the exact valuation filter. These results preserve both provenance and sign.

## Remaining work and control scope

The smallest incomplete mathematical unit is a **nonanomalous source-preserving finite telescope modulo p^4** whose p^2 and p^3 digits cancel the present anomaly, separately in p=13 and 19 mod24 classes; then translate that certificate back to the original Delta-R target. The current derivation does not prove the all-prime mother theorem or the full W-2S coupling.

Original fixed-373 native H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius eta, signed odd Green/Hesse, kappa and independent checker remain PENDING_OWNER / NOT_EXECUTED (Enterprise Math #1559). This scalar result is not a native experiment.

Research logical lane exclusively `chatgpt-research-onhour-enterprise-math-20260923` (separate from maintenance). Original request `research-onhour-20261031-0205-dispatch-r15` has terminal FAILED / UPSTREAM_CODE_REVIEW_REQUIRED receipt at kimi-query-bridge #6633, and was not resubmitted. The 2026-11-02 gateway reported research_authority_granted=false, executor_binding_configured=false, own checkpoint ACCESS_DENIED and exact continuation CONTROL_QUOTA; no own session/CLAIM/run/Source checkpoint. This note is **neutral author evidence storage only**, not activity registration, Source publication or independent acceptance. Original schedule/notifications remain unchanged.
