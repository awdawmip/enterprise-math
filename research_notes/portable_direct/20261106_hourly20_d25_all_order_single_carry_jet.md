# D25: all-order single-carry source jets and finite-difference p-adic observer

2026-11-06 (Asia/Hong_Kong). TASK_RESEARCH author-side portable evidence; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).
Configured logical lane label `chatgpt-research-hourly-enterprise-math-20260923` is not an attestation of the current service session.

## Theorem 1 — one-carry formula for **every** radial source jet

For any integer m>=1 let a=2m, b=3m, c=4m and
`P_m(z)=sum_{j=0}^{b}(6j+1)(-1/2)^j binom(b,j)binom(a+z,j)binom(c+z,j)` over Q[z].
Write `C_r=[z^r]P_m(z)` for r>=0, `omega_j=(6j+1)(-1/2)^j binom(b,j)`, and `e_r(S)` for the degree-r elementary symmetric function of a finite multiset, with `e_0=1` and `e_{-1}=0`.

For 0<=j<=a set
`S_head(j)={1/(a-h),1/(c-h) : 0<=h<j}` (multiset).
For a<j<=b set
`S_carry(j)={1/(a-h):0<=h<j,h!=a} UNION {1/(c-h):0<=h<j}` (multiset)
and `E_{a,j}=(-1)^(j-a-1)a!(j-a-1)!/j!`.

**Exact rational identity for all r>=0**:
```
C_r = HEAD_r + CARRY_r,
HEAD_r  = sum_{j=0}^{a} omega_j binom(a,j)binom(c,j)e_r(S_head(j)),
CARRY_r = sum_{j=a+1}^{b} omega_j E_{a,j}binom(c,j)e_{r-1}(S_carry(j)).
```
Proof: expand each binomial into factors `(n-h+z)/(h+1)`. For j<=a neither varying outer factor has a zero at z=0, hence the coefficient is its constant product times `e_r` of the reciprocal nonzero roots. For a<j<=b the a-source has exactly the single zero factor z, with remaining constant product E_{a,j}; the coefficient shifts by one to `e_{r-1}`. The fixed b-source vanishes identically for j>b. Sum over the three-source signed observer. QED.

For primes p=6m+1, all denominators of both formulas are p-units (j<=3m<p). For 0<=r<p the Newton recursion `e_r=(sum_{k=1}^r (-1)^(k-1)e_(r-k) power_sum_k)/r` is valid modulo p, providing a separate exact algorithm. This is a provenance-preserving BRC carrier: HEAD and CARRY are distinct labelled index populations, not interchangeable contributions to a scalar.

## Theorem 2 — full-jet readout from unexpanded original sums

For the same prime p and any polynomial P_m above, fix 0<=R<p. Let `V_t=P_m(pt) mod p^(R+1)`, t=0..R, evaluated by the original binomial finite sum (not by a source-jet expansion). Then, for each 0<=r<=R,
```
[z^r]P_m(z) = (1/r!)* ( sum_{t=0}^r (-1)^(r-t) binom(r,t) V_t / p^r ) (mod p).
```
The numerator is divisible by p^r, so the quotient is well-defined modulo p. Proof: P_m is p-integral; after substitution z=pt, monomials of degree below r have zero r-th forward difference, degree r contributes r!p^r C_r, and higher degrees contribute multiples of p^(r+1). Since r<p, r! is a unit. QED.

Thus R+1 **full original-sum observations** modulo p^(R+1) recover the entire radius-R jet modulo p, with no claim of recovering the underlying individual source terms from the total alone. This finite-difference observer has a stated input carrier, precision and allowed operation.

## New exact p=5113 certificate through order six

For p=5113, m=852, a=1704, b=2556, c=3408, the source-labelled coefficients for r=0,1,2,3,4,5,6 are:

| r | HEAD_r mod p | CARRY_r mod p | C_r mod p |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 1973 | 3140 | 0 |
| 2 | 3519 | 1594 | 0 |
| 3 | 4774 | 4122 | 3783 |
| 4 | 29 | 2656 | **2685** |
| 5 | 4198 | 643 | **4841** |
| 6 | 1289 | 2666 | **3955** |

The order-1 and order-2 cancellations each involve two nonzero independent source populations; at order 3 they no longer cancel. The root multiplicity three and the order-3 coefficient 3783 were established previously and are only reused here. **New** is the full general-r formula, recovered 4th/5th/6th coefficients and all-jet independent p-adic readout.

The actually executed standalone checker `d25_all_order_carry_jet_research_verified_20261106.py` passed three independent methods: (A) polynomial coefficient recurrences for each outer binomial, (B) separate Newton power-sum head/carry expansions at **all 2557 indices**, and (C) **seven evaluations of the original 2557-term finite sum** at z=p*t, t=0..6, modulo p^7. All seven recovered coefficients equal the table. In particular `Delta^4 P_m(pt)|_{t=0}/p^4 = 3084 mod 5113 = 4!*2685 mod 5113` (previously computed via a separate p^5 direct check). Integer modular arithmetic; no floating approximation.

## Source/authority and next scientific action

This is a scoped auxiliary source-jet result. The mother target remains `Delta_p-R_p=0 mod p` for p mod24 in {13,19}. The original H0/B0 at p=373, Frobenius, eta/kappa and independent review remain open. Another D25 lane has already published q/g anti-diagonal and 216-shell results; those are neither repeated nor claimed here.

Prior author-side radial third-jet report: `20261106_hourly20_d25_radial_third_jet_triple_zero.md`. Native original read request IDs `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` were reconciled by the same IDs this run; most recent status QUEUED with prior EVENT_COLLECTION_IO recorded. Own service session, protected staging, winning claim and authorized run remain unverified; no role-bound Source checkpoint, CLAIM/OPEN, freeze or admission was asserted. Control support: #1558.

**Next smallest differentiated task:** use the all-order recurrence to test a proposed source-preserving telescoper for the open all-prime first radial derivative `T_1+T_3=0`, preserving the head/carry boundary. Independently exploit the original 216-shell/qg anti-diagonal result for the fixed mother objective when a lawful owner routes that work; no duplicate claim of that lane's result.
