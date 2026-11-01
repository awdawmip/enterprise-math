# D25 — Exact CM weighted-jet scalar obstruction and exceptional p=13 (2026-11-02)

**AUTHOR-DERIVED / EXACT PROOF / 107 FINITE TARGET PRIMES CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXECUTED.** Portable mathematical evidence only; not a Source checkpoint, Result, authorized CLAIM/run or review.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This research reuses (and does not claim authorship of) the onhour-lane `20261102_onhour_d25_weighted_pf_cm_jet_forcing.md` and `20261102_onhour_d25_weighted_gauged_pf_endpoint.md`, at main `912932b65e146a1b13f3de279f58018da36c7676`. The task's immutable scientific input and current behavioral-rule snapshot are distinct.

## Original finite hypergeometric observers

Over `Z_(p)`, prime `p>3`, let `theta=z*d/dz` and

```
a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3
b_k=(1/4)_k(1/2)_k(3/4)_k/(k!)^3
F_A,p(z)=sum_(0<=k<p) a_k z^k;  Y_A,p=(1+6theta)F_A,p
F_B,p(z)=sum_(0<=k<p) b_k z^k;  Y_B,p=(1+8theta)F_B,p.
```

The original weighted 216 and 2304 sums are `Y_A,p(1/2)` and `Y_B,p(1/9)`. For the unweighted modules,

```
L_A=theta^3-z(theta+1/2)(theta+1/3)(theta+2/3),
L_B=theta^3-z(theta+1/4)(theta+1/2)(theta+3/4).
L_A F_A,p=-p^3 a_p z^p,   L_B F_B,p=-p^3 b_p z^p.
```

The p³ endpoint sources survive at higher precision. The typed CM jet observer is `J_2(Y;z0)=(Y,theta Y,theta²Y)|z0`, in the **original** weighted model and original CM argument.

## Theorem 1: two exact conditional CM jet rays

For each model separately, suppose `F(z0)=theta F(z0)=0 mod p` and `q=theta²F(z0) != 0 mod p`. Then

```
J_2(Y_A,p;1/2)=q_A*(0,6,10) mod p;
J_2(Y_B,p;1/9)=q_B*(0,8,5/2) mod p.
```

Proof: In either third-order PF equation the lower jets vanish at the assumed double zero. Since the terminal source is divisible by p³,

```
theta³ F(z0) = [z0/(1-z0)]*(3/2)*q  (mod p).
```

Thus `theta³ F_A(1/2)=(3/2)q_A` and `theta³F_B(1/9)=(3/16)q_B`. The weighted derivatives are `theta Y=theta F+w theta²F`, `theta²Y=theta²F+w theta³F`. Substitution gives the two stated triples. Every denominator is a unit for `p>3`. QED.

The A double-zero follows the task's earlier CM0/Clausen antecedent in the cited onhour source. **B double-zero is a stated hypothesis** here; finite checks on target primes are not an all-prime proof.

## Theorem 2: p=13 is the only D25 scalar full-jet coincidence

Under **both** double-zero and nonzero-second-jet hypotheses, there exists a scalar `lambda in F_p^*` taking the entire A weighted jet to the B weighted jet if and only if `p|65`. Indeed, their nonzero-jet projective slopes are

```
(theta²Y_A)/(theta Y_A) = 10/6 = 5/3,
(theta²Y_B)/(theta Y_B) = (5/2)/8 = 5/16,
difference = 65/48.
```

As `p>3`, scalar proportionality is equivalent to `p=5` or `p=13`, and then `lambda=8q_B/(6q_A)` is determined by the first derivative. **Within the frozen D25 classes `p≡13,19 mod24`, the sole exceptional scalar collision is `p=13`.** For every other target prime satisfying the hypotheses, scalar-only identification of all three original weighted jets fails; matrix/derivative-mixing or richer source-sensitive transport remains open. This does **not** contradict equality of the original zeroth weighted sums. It shows that using only the prime 13 as a scalar-transfer model is misleading.

## Theorem 3: global characteristic-zero rational 3x3 pullback-gauge obstruction

The two complete rank-three differential modules are not related in **either direction** by a rational change `z=phi(t)` and an invertible rational 3x3 gauge, even after an optional rank-one scalar twist.

Proof: At regular singular `z=0`, the generalized hypergeometric local exponents are `0,0,0`; at `z=1`, they are `0,1,1/2`. At infinity the A exponents are `1/2,1/3,2/3`, whose local-monodromy eigenvalue ratios include primitive order **3** and **6**, while B exponents `1/4,1/2,3/4` include primitive order **4** and no order 3. A rational pullback raises a local monodromy matrix to an integer ramification power; this can only decrease the orders of eigenvalue ratios. Rational gauges conjugate monodromy and scalar twists leave eigenvalue ratios unchanged. Thus B's order-4 local ratio cannot arise from A, and A's order-3 ratio cannot arise from B. The preexisting invertible rational weighted jet gauges preserve the same differential modules. QED.

**Scope:** This is a global *rational-pullback-and-invertible-rational-gauge* obstruction in characteristic zero. It does not exclude isolated CM-endpoint identities, non-rational/algebraic correspondences with different intermediary modules, finite-prime p-dependent matrices, Frobenius-semilinear comparison, WZ identities, or the original mod-p³ target.

## Determinant-line corollary from previously proved gauges

For the homogeneous 3-jet companion matrix `A(z)`, `trace(A(z))=3z/[2(1-z)]`. Liouville's formula for `theta` gives `det(Xfund)=C*(1-z)^(-3/2)`. The two previously proven weighted jet-gauge determinants are `D_A=(1+6z)/(1-z)`, `D_B=(1+15z)/(1-z)`; therefore

```
det(Yfund,A)=C_A*(1+6z)*(1-z)^(-5/2),
det(Yfund,B)=C_B*(1+15z)*(1-z)^(-5/2).
```

At original CM arguments the gauge determinants equal **8** and **3**, respectively; they are units for `p>3`. This is a determinant-line consequence, **not** an independent re-proof of the other lane's complete gauge or a cross-model module isomorphism.

## Original-integer finite certificate and BRC application

`d25_weighted_jet_det_monodromy_20261102.py` actually evaluated all original finite coefficients and the 0..3 Euler moments for both models at every **107 target primes `p<=3000`**. All 107 exhibited both double-zero hypotheses, nonzero second jets, exact PF identity and the stated weighted rays. Their entire weighted jets are proportional mod p only for `p=13`.

```
p=13:  q_A=7,   q_B=9,   q_B/q_A=5;  A=(0,3,5),     B=(0,7,3).
p=19:  q_A=2,   q_B=3,   q_B/q_A=11; A=(0,12,1),    B=(0,5,17).
p=373: q_A=173, q_B=336, q_B/q_A=58; A=(0,292,238), B=(0,77,94).
```

BRC resolution: **COMPOSE_APPLIED**, reusing the labelled prime/ring, original coefficients, weighted 3-jet carrier and source-preserving gauged operators. The observer `J_2 mod p` and future operation (scalar versus 3x3 transport, later signed cutoff mod p³) are declared. A scalar zeroth-value compression does not in general preserve the required jet operation; the exceptional p13 coincidence shows why recording the prime and port identity is necessary. This is an exact signed/jet port problem, not a positive-mass cancellation model.

## Exact continuation and boundaries

Scientific mother remains **OPEN**: `Delta_p-R_p=0 modp` (original 216 `S_p≡p modp³` for `p≡13,19 mod24` with the original signed-source bridge). Next action: find/test a genuinely **mixing 2x2** transformation of the *nonzero* weighted derivatives at `p=19` and `p=373`, then lift with exact original p-adic and signed Clausen sources. Independently discharge B double-zero over all target primes or retain the conditional theorem.

Native p373 H0/B0 `[X]U mod139129`, module rank, semilinear Frobenius/eta and signed Green/Hesse original experiment remain **PENDING_OWNER, NOT_EXECUTED** (`enterprise-math#1559`). No new Researcher claim/run/checkpoint, Result or independent review was issued. For fixed hourly lane `chatgpt-research-hourly-enterprise-math-20260923`, historical read #6637 was SUCCEEDED without pending operations and old continuation #6638 definitively FAILED `UPSTREAM_CODE_REVIEW_REQUIRED`; gateway 0.6.11 still shows `research_authority_granted=false`, `executor_binding_configured=false`; support `enterprise-math#1558` owns the control route. Other onhour and maintenance conversation IDs are distinct. `REGISTER_PENDING / NOT_ADMITTED`. P000, ACTIVE worldview, frozen science pin, user scheduler and notifications unchanged.
