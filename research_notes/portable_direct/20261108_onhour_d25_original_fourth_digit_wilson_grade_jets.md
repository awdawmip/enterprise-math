# D25 — fourth-digit Wilson/harmonic jets on the original W216 and V2304 coefficient grades

Date: 2026-11-08, Asia/Hong_Kong. Status: **AUTHOR_SIDE_PROVED_FINITE_JET_IDENTITIES / FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Frozen task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Separate existing author-side C4 candidate: `research_notes/portable_direct/20261108_onhour_d25_original216_2304_fourth_digit_transport_and_grade3_kernels.md` (not a formal Result).

## Exact theorem: lower-grade fourth-digit lifts

Let p>3 be prime, M=p^4, and perform rational computations in Z_(p), reducing at the explicitly stated precision. Define

- `omega=((p-1)!+1)/p` (Wilson quotient, taken modulo p^2 when required);
- `H_r=sum_{i=1}^r 1/i`, `E_r=sum_{1<=i<j<=r}1/(ij)=(H_r^2-H_r^(2))/2`, all denominators p-units for 0<=r<p.

Using only Wilson's theorem and the finite product `prod_{i=1}^r (1+p/i)`, prove the following *uniform*, elementary identities:

```text
(p+r)!/p       = -r! [1+p(H_r-omega)+p^2(E_r-omega H_r)]    (mod p^3)
(2p+r)!/p^2    = 2r! [1+2p(H_r-omega)]                    (mod p^2)
```

For the second formula, split the unit factors into a full nonzero block and a terminal block; `prod_{i=1}^{p-1}(1+p/i)=1 mod p^2` because `H_(p-1)=0 mod p`. Both formulas hold for every 0<=r<p (including r=0). Note that the first formula includes a true second jet `E_r-omega H_r`, previously missing from the p^4 grade-one transport.

Write the *original* weighted coefficients, without a model change,

```text
w(n)=(6n+1) (2n)! (3n)! / ((n!)^5 216^n),
v(n)=(8n+1) (4n)! / ((n!)^4 2304^n),     0<=n<p.
```

Partition indices by the original unweighted factorial p-valuation: `gW=floor(2n/p)+floor(3n/p)`, `gV=floor(4n/p)`. For grade 0, retain the original factorial sums W0,V0 exactly modulo M. For grade 1, introduce p-unit rational base coefficients

```text
bW(n)=-(6n+1)(2n)!(3n-p)!/((n!)^5 216^n)     [p<=3n, 2n<p]
bV(n)=-(8n+1)(4n-p)!/((n!)^4 2304^n)         [p<=4n<2p].
```

Their original grade-one sums satisfy, **modulo p^4**,

```text
W1 = p sum bW(n) [1+p(H_(3n-p)-omega)+p^2(E_(3n-p)-omega H_(3n-p))];
V1 = p sum bV(n) [1+p(H_(4n-p)-omega)+p^2(E_(4n-p)-omega H_(4n-p))].
```

For grade 2 use

```text
cW(n)=(6n+1)(2n-p)!(3n-p)!/((n!)^5 216^n)    [p<=2n, 3n<2p]
cV(n)=2(8n+1)(4n-2p)!/((n!)^4 2304^n)       [2p<=4n<3p].
```

The **new first-order grade-two lifts**, also modulo p^4, are

```text
W2 = p^2 sum cW(n) [1+p(H_(2n-p)+H_(3n-p)-2omega)];
V2 = p^2 sum cV(n) [1+2p(H_(4n-2p)-omega)].
```

The grade-three sums have already been proved in the earlier source and are reused unchanged: `W3=p^3 T_W3` and `V3=p^3 T_V3` modulo p^4. No positive-weight assumption is made.

## Four-grade finite reduction, proved equivalence (not a proof of C4)

Define `B_X=sum bX`, `J_X=sum bX(H-omega)`, `K_X=sum bX(E-omega H)`; let `C_X=sum cX` and `L_W=sum cW(H_a+H_b-2omega)`, `L_V=sum 2cV(H_c-omega)`. Every sum is over its *own* original model/index interval. Thus for `chi=(-3/p)`:

```text
W_p-2V_p+p*chi
 = (W0-2V0)+p*chi
 + p (B_W-2B_V)
 + p^2 (J_W-2J_V+C_W-2C_V)
 + p^3 (K_W-2K_V+L_W-2L_V+T_W3-2T_V3)    (mod p^4).   (JET4)
```

Every term on the right now has an explicit terminating p-unit-denominator definition; the precision needed is respectively mod p^4, p^3, p^2, p. This is a proved exact *source-preserving reduction* of the open fourth-digit C4 conjecture, not a proof that its right side vanishes. It extends the previous grade-zero quadratic / grade-one linear / grade-two leading / grade-three leading interfaces by **exactly the missing grade-one second and grade-two first jets**. The grade-zero term is deliberately retained as the unmodified original finite sum, and has not been eliminated by a transformation.

**Proof:** substitute the two factorial-complement identities into each indicated original grade interval, preserving every p-power and linear weight. A grade g>=4 cannot occur for 0<=n<p; truncate every bracket at precision p^(4-g). Grade-three identities are the earlier proven source, not recomputed here. Sum the disjoint source-indexed parts. All displayed denominators are p-units, so every congruence is well-typed.

## Reproducible finite check (not universal C4 proof)

Run `python research_notes/portable_direct/d25_fourth_digit_wilson_grade_jets_20261108.py`. Exact independent modular original-coefficient recurrence versus the factorial/Wilson/harmonic-jet evaluator matched **all 8 grade ports for each of the 301 primes 5<=p<=2000** (2408 port comparisons). The C4 residual was zero on this finite set, as in the previously saved 1227-prime probe. The new test adds an independent arithmetic decomposition, not a second independent human review.

| p | omega mod p^2 | W0,W1,W2,W3 (mod p^4) | V0,V1,V2,V3 (mod p^4) |
|---:|---:|---|---|
| 13 | 52 | 27144, 26104, 12675, 10985 | 20098, 12870, 6591, 13182 |
| 19 | 211 | 67393, 59698, 58121, 27436 | 68115, 82802, 41154, 109744 |
| 373 | 125179 | 17724329257, 8808962706, 9585709842, 14426842526 | 252649685, 6701296366, 12143457378, 6175518923 |

At p=373 the sums are `W=11832087049`, `V=5916043711` modulo `373^4=19356878641`, hence `W-2V+373=0` exactly in that residue representation. Setting the Wilson quotient to zero *within the jet formulas* (without changing the original factorial data) creates a nonzero residual at p=13,19,373: respectively 17576, 63536, 14810282050 modulo p^4. This shows why the Wilson correction cannot be omitted from this particular port-level reduction; it is not a claim that no other transformed proof could cancel it.

## Observer/BRC/authority boundary and continuation

Applied BRC interface: retain the signed tuple `(model=W/V,index=n,grade=0..3,weight,unit-factorial,Wilson/harmonic-jets)` and only apply the declared additive mod-p^4 observer *after* the p-adic precision of each source is known. A total alone erases the grade compensation. These classical auxiliary arithmetic models are not assertions about native X6 spatial embeddings or native Frobenius. P000, ACTIVE worldview and the frozen science pin remain unchanged.

The latest native support requirement #1559 is separate: same-original-class p373 H0/B0 divided-power `[X]U mod 139129`, module rank, Frobenius direction/eta, signed Green/Hesse kappa, Delta-R and independent reproduction. **NOT_EXECUTED / PENDING_OWNER**; the present code does not run or replace it.

Source request `onhour11-20261106-1400-exact-research-lane-continuation` was read and reconciled in this run: after `WAITING_RESOURCE/EVENT_COLLECTION_IO`, reconcile yielded `QUEUED`, `formal_task_created=false`. No original operation replay. Site reports `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; no native session/claim/run is asserted. Research-lane label `chatgpt-research-onhour-enterprise-math-20260923` is retained only as historical logical routing context, not an independently authenticated service identity or maintenance-lane identity.

**Next mathematical action:** derive an independent terminating Fricke/Cartier/WZ identity that makes the explicit right side of (JET4) vanish for all p>3, or find a valid counterexample; do not repeat grade jets or infer a universal proof from 301/1227 finite checks. **Next native action:** original #1559 evaluator/owner actually performs the pinned p373 H0/B0 experiment and stores a reproducer; follow the original request's Source status before any claim/dispatch.

Research status: `AUTHOR_SIDE_PROVED_JET4_REDUCTION / EXACT_301_PRIME_8_PORT_CHECK / C4_UNPROVED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE / REGISTER_PENDING`.
