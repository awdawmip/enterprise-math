# JT2 UR: automatic Legendre SIMPLE, all-order balanced Hensel root, and local curvature

Date: 2026-11-16. Scope: source-exposed author-side mathematics by the existing RESEARCH_DRIVER `EM-DVR-DEBB5E`, not an independent Native Result review. The original finite Sun/Legendre and norm-jet reduction is due to `EM-JT2-EF9380` and its historical stage review `EM-DVR-57CCCE`. This note extends the already saved [lift-sensitivity reduction](2026-11-16_jt2_ur_norm_jet_hensel_lift_sensitivity.md), rather than redoing that work.

## Exact definitions and scope

Let `p>3` be prime with `p≡13 or 19 (mod 24)`. Put `n=(p-1)/3=2m`, so `2n<p`. Let `P_n(X)` be the ordinary Legendre polynomial with `P_n(1)=1`; write `P_n(X)=Q_m(X²)` over `Z_(p)`. Define

```
J_m(Y) = sum_{r=0}^{2m} ([Y^r]Q_m(Y)^2) Y^r / (2r+1),
Phi_p(Y) = 18 Q_m(Y) Q_m'(Y) - p (2 J_m(Y)+3).
```

All these coefficients are `p`-integral: `P_n` has denominators powers of 2 and `2r+1 <= 4m+1=2n+1<p`. The original fixed CM0 hypothesis is `Q_m(1/2)≡0 (mod p)`. The original scalar is `epsilon_p = Phi_p(1/2)/p (mod p)`, when CM0 holds. We do **not** assume the previously separately stated SIMPLE hypothesis.

## Theorem 1 — automatic separability of the ordinary-Legendre squared-coordinate polynomial

For every such `p`, the polynomial `Q_m mod p` is squarefree over an algebraic closure of `F_p`. Thus any root `beta` (in particular `beta=1/2` when CM0 holds) satisfies `Q_m'(beta)≠0` modulo `p`. The previous SIMPLE premise is a consequence of CM0, not an additional all-prime hypothesis.

**Proof.** The ordinary Legendre differential equation, after `Y=X²`, is the exact identity

```
4Y(1-Y) Q_m''(Y) + (2-6Y) Q_m'(Y) + n(n+1) Q_m(Y) = 0.    (1)
```

The leading coefficient of `P_n` is `2^{-n} binom(2n,n)`, a `p`-unit because `2n<p`; hence `deg(Q_m mod p)=m<p`. The values

```
Q_m(0)=(-1)^m 4^{-m} binom(2m,m) != 0 (mod p),
Q_m(1)=P_n(1)=1
```

show that a root `beta` is neither 0 nor 1. If `beta` had multiplicity `r>=2`, then `2<=r<=m<p`. In (1), the lowest-order coefficient at `(Y-beta)^{r-2}` is `4 beta(1-beta) r(r-1) c`, where `c` is the nonzero leading Taylor coefficient of `Q_m` at `beta`. Every factor is nonzero in characteristic `p`, while the other two summands have higher vanishing order. Contradiction. QED.

This argument uses the exact Legendre differential equation and degree bound, not numerical checks or an assumed simple root.

## Theorem 2 — a unique exact p-adic balanced root to all orders

For every `beta in F_p` satisfying `Q_m(beta)=0`, there exists a unique `b_{p,beta} in Z_p` with

```
b_{p,beta} = beta (mod p),       Phi_p(b_{p,beta}) = 0 in Z_p.    (2)
```

For every `k>=1`, its reduction is the unique root of `Phi_p mod p^k` in the residue class `beta`. In particular, the balanced mod-`p²` lift from the earlier result is the order-two truncation of this exact root.

**Proof.** Modulo `p`, `Phi_p(Y) = 18 Q_m(Y)Q_m'(Y)`. At a root `beta` of `Q_m`,

```
Phi_p(beta)=0 (mod p),
Phi_p'(beta)=18 Q_m'(beta)^2 != 0 (mod p).              (3)
```

The second property is Theorem 1 and `p>3`. The ordinary simple-root Hensel lemma over `Z_p` proves (2) and uniqueness modulo every power. No claim is made about other roots arising from `Q_m'`.

For any chosen `p`-integral lift `a` of `beta`, the first Hensel correction is

```
b_{p,beta} = a - p (Phi_p(a)/p) / (18 Q_m'(beta)^2) (mod p²).      (4)
```

This is exactly the earlier balanced-lift formula, now with its required unit denominator established rather than assumed. QED.

## Theorem 3 — a universal fixed-port jet relation and local curvature

Under CM0 at `beta=1/2`, equation (1) specializes to the exact identity

```
Q_m''(1/2) - Q_m'(1/2) + n(n+1) Q_m(1/2) = 0.
```

Consequently,

```
Q_m''(1/2) = Q_m'(1/2) (mod p),
Phi_p''(1/2) = 54 Q_m'(1/2)^2 (mod p),
Phi_p''(1/2) / Phi_p'(1/2) = 3 (mod p).                (5)
```

For the middle identity, differentiate `Phi_p` twice:

```
Phi_p'' = 18(3 Q_m' Q_m'' + Q_m Q_m''') - 2p J_m''.
```

Reduce at the CM root. The denominator in (5) is a unit by Theorem 1. Thus the first two ordinary jets of the *global balancing polynomial* have a fixed curvature ratio at the frozen port, independent of `m` except through the admissible prime.

## Precise consequence for the outstanding UR target

At the specified fixed rational lift `a=1/2`, CM0 makes `Phi_p(a)/p` legal. Therefore the original uniform UR residue claim is exactly

```
epsilon_p = 0 (mod p)
 <=> Phi_p(1/2) = 0 (mod p²)
 <=> b_{p,1/2} = 1/2 (mod p²).                           (6)
```

Theorem 1 discharges SIMPLE on the actual ordinary-Legendre input; Theorem 2 upgrades the structural balanced root from a one-step artifact to a canonical all-orders `p`-adic branch, and Theorem 3 supplies a fixed local jet ratio for further arithmetic analysis. They do **not** prove the remaining coincidence in (6) for all admissible primes. The input is the full ordinary-Legendre polynomial and primitive; no ad hoc axiom replaces that arithmetic question.

### Scope and provenance

Frozen primary scientific source: `research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md` at `969846f1d451b3e086f34a19b217e333c8a90c8d` (Git blob `b400bf432162cc5d67f51a1d2963de533c786afb`). Historical accepted scope: `driver_reviews/JT2_UR_NORM_JET_STAGE_REVIEW_57CCCE_20260920.md` (Git blob `702f7ddf2816f7515d197f440c30d34f7c3cd244`). Source-exposed finite audit and previous lift lemma: `research_notes/driver/2026-11-16_jt2_ur_eps_norm_jet_exact_45_prime_audit.md` and `research_notes/driver/2026-11-16_jt2_ur_norm_jet_hensel_lift_sensitivity.md`.

Contribution of this note: separability proof / automatic SIMPLE, all-orders balancing polynomial and Hensel branch, and exact curvature relation by `EM-DVR-DEBB5E`. This is a proof written and checked from the displayed polynomial identities; independent Native review, current researcher CLAIM, Result admission and formal task/parent closure are separately governed.
