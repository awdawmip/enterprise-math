# D25 — Exact rank-two transport of the ordinary valuation-one next digit (2026-11-02)

**AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / ORIGINAL INTEGER RECURRENCE VERIFIED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0_B0.**

Research lane `chatgpt-research-onhour-enterprise-math-20260923`; never uses `chatgpt-hourly-enterprise-math-20260921` authority. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen source `c47e13e4aba0e006366f989d6334d443f6333ae3`.

Inputs consumed: previous ordinary v1 leading-digit rectangular cancellation `3dd822d95da90d9ffa48a344f6c8ada46b8ffcb5`, full all-carry p^4 factorial unit carrier `c15f0e3cecada1b31d4874f72f7e9bda9e21cc65`, and S2304 universal B2 literature entailment `5ad12b69bc348227d7ea3165056aabbf886a738a`. This unit computes the **previously outstanding second digit of ordinary v=1**, rather than extending unrelated auxiliary theory.

## Statement, provenance and exact source observer

Fix any prime `p>=5`. For the original 216 and 2304 streams use:

```text
model       J           D       lambda  j*
W216        {2,3}       216      6       3
S2304       {4}         2304     8       4
alpha(k) = [prod_{j in J} (jk)!] / [(k!)^d * D^k],   d=sum J
weighted term = (lambda*k+1)*alpha(k)
V(k)=p^{-v_p(alpha(k))}alpha(k)  (p-adic unit; retain the rational unit)
h=floor((p-1)/j*), H=(p-1)/2, I0={0,...,h}, I1={h+1,...,H}.
```

Represent every `k<p²` by its unique two-digit source coordinate `(a,b)` with `k=ap+b`; preserve model, original weight, valuation and carry. The **ordinary v=1** source population is exactly the disjoint union:

```text
L = {(a,b): a in I0, b in I1, (j* a+1) not divisible by p}
R = {(a,b): a in I1, b in I0}.
```

The excluded boundary `j*a+1=p` has valuation two, and remains in its own original v2 port; this is a real carry distinction, not a dropped term.

Put `H_n=sum_{t=1}^n t^{-1} modp`, `q_p(D)=(D^(p-1)-1)/p modp`, and define the low-digit harmonic/denominator correction

```text
C(b) = sum_{j in J} j H_(jb - p*floor(jb/p)) - d H_b - q_p(D)  modp.
```

For either rectangle X define, with `A` its a-range, `B` its b-range, and `gamma(a)=j*a+1` on L, `1` on R:

```text
A0_X = sum_{a in A} gamma(a)*V(a)         (mod p²)
A1_X = sum_{a in A} a*gamma(a)*V(a)       (mod p)
B0_X = sum_{b in B} (lambda*b+1)*V(b)     (mod p²)
Bplain_X = sum_{b in B} V(b)              (mod p)
Bharm_X = sum_{b in B} (lambda*b+1)*V(b)*C(b) (mod p).
```

**Theorem (exact, all p>=5, no CM premise):** the weighted original v1 contribution `T1`, with exactly the source population `L union R`, satisfies

```text
T1/p ≡ A0_L*B0_L + A0_R*B0_R
  + p*[A1_L*(lambda*Bplain_L+Bharm_L)
       +A1_R*(lambda*Bplain_R+Bharm_R)]      (mod p²).
```

This is an `O(p)` sum of six low-digit moments per source rectangle instead of an `O(p²)` high-index original-sum evaluation.

**Proof.** The exact all-boundary p-free factorial decomposition from the preceding carrier theorem gives, *on either of the two defined rectangles*,

```text
V(ap+b)/(V(a)V(b)) = gamma(a)*(1+p*a*C(b)) (mod p²).
```

Indeed the sole low-digit carry is `c_(j*)=1` on L and `0` on R, giving `Gamma_(j*)=j*a+1` or 1. By the source-population definition none of the high-digit carry flags is present. Every complete p-block logarithm correction is divisible by p³ for p>=5; the remaining residue-block logarithm is precisely `pa*C(b)` modulo p², including Fermat quotient `q_p(D)`. Multiply the *original* weight `lambda(ap+b)+1=(lambda*b+1)+p*lambda*a`, then original valuation factor p. Collect independently in a and b. This yields the displayed formula, with no division by `lambda*k+1`, and all denominators are p-units. QED.

**CM low-moment corollary, with separately evidenced hypothesis:** If `M0=sum_{a in I0}V(a)=0` and `M1=sum_{a in I0}a V(a)=0` modulo p, then `A0_L ≡ M0+j*M1 ≡0 modp` (the excluded boundary contributes zero modulo p) and `B0_R ≡ M0+lambda*M1 ≡0 modp`. Consequently **each rectangle separately contributes zero in the first digit**, and the second digit is the mod-p reduction of the RHS divided by p. This statement does not presume CM for arbitrary p.

## New exact fixed-373 certificate

Independent original quotient-recurrence verification yielded, at `p=373`, the following values of `T1_X/p mod p²`:

```text
Source    L (integer mod139129)  L/p mod373  R (integer mod139129) R/p mod373  total /p² mod373
W216      97353                  261         83179                223         111
S2304     88774                  238         125328               336         201
Signed W-2S L: (261-2*238) mod373=158
Signed W-2S R: (223-2*336) mod373=297
Complete ordinary-v1 second digit: (158+297) mod373 = **82**.
```

The low-rank formula was computed from `k<p` unit and harmonic tables, while an **independent original p-adic quotient recurrence** computed all represented `k<p²` source terms and checked their exact membership/valuation. All comparisons matched at `p=5,7,11,13,19,23,37,43,61,67,109,139,373`, across both models, totalling **43,249 distinct original ordinary-v1 index positions**. At p373 the signed v1 digit 82 reproduces the fifth-source decomposition `143(v0)+82(v1 next)+143(v2 first)+4(anomaly)+1(baseline)=373`; the other ports retain their provenance and prior evidence. The full research script and original recurrence validator are stored at `research_notes/portable_direct/d25_ordinary_v1_second_digit_low_rank_20261102.py`, with local `d25_v1_second_digit_low_rank_20261102.check.json` as executed output.

## Research consequence and next exact action

The universal B2_S corollary has now discharged one whole previously conjectural S2304 port, while this theorem handles a second-digit v1 port from low moments. Next investigate the **W216 B2_W** contribution and remaining signed v0/anomalous ports, then construct the actual source-aligned Clausen `Delta_p-R_p` observer at the frozen input pin. Keep both p=13 and 19(mod24) classes. This scalar progress is independent from native fixed373 H0/B0 divided-power `[X]U mod139129`, semilinear Frobenius, eta, signed Green/Hesse and kappa; source support issue https://github.com/awdawmip/enterprise-math/issues/1559 is still pending a real executor.

No canonical session/CLAIM/run or Source checkpoint is asserted; mathematical author-side publication is not official Result/admission.
