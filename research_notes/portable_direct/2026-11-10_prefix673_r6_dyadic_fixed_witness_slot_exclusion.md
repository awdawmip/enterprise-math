# PREFIX-673-R6 — Two dyadic rational witnesses eliminate the BRC boundary strip down to p=10^-13

Date: 2026-11-10 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH.
Researcher-ID: EM-DIRECT-33775E. Research-Activity-ID: RA-D6D79B537C57318E98789961.
Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Evidence status: `AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Question and BRC interface

The mother question is the maximum sampling-stop variance of the frozen 189-layer two-informative-direction BRC statistical observer on `[0,1]^2`. The probability coordinates `p,z` are observer parameters, not a native two-dimensional plane or a complete native X6 slice. Retain frozen signed-path counts, binomial survival readout and Poissonized-clock moments. Reuse: `COMPOSE_APPLIED` to the exact PREFIX-660 root/curvature and PREFIX-670 normal-coercivity certificates, both at their original evidence status.

For `q in {12,24}`, set `V_q(p,z)=q^2 Var(Y(p,z))-q E[Y(p,z)]`, `I=[607/4096,609/4096]`, `R=[0,1/64] x I`, `g_q(z)=V_q(0,z)`, `M(q)=max_{z in I}g_q(z)`, and `z_*(q)` the unique edge maximum certified in PREFIX-660.

The earlier fixed witness `Q=(0,19/128)` excluded `p>=1/245197` for every real `12<=q<=24` (PREFIX-672-SC). The two actual integer-slot schemes admit distinct, much sharper fixed dyadic witnesses from the prior certified root brackets.

## Theorem 673.1 — Slot-specific rational competitor certificates

Define exact rational probabilities

```
z_12 = 19/128 - 1167/2^25 = 4979569/33554432
z_24 = 19/128 + 7365/2^25 = 4988101/33554432
Q_12 = (0,z_12), Q_24 = (0,z_24).
```

**For each `q in {12,24}`, every real `p in [1/10^13,1/64]`, and every real `z in I`:**

```
V_q(Q_q) - V_q(p,z) > 1/1000000000 > 0.
```

Consequently the two fixed rational witnesses exclude exactly `156249999999/156250000000` of the area of `R` (99.99999999936%); the remaining `p` width is `10^-13`. The old uniform-in-real-q threshold `1/245197` is over 40 million times wider. Both results remain valid under their distinct quantifiers.

## Proof

**Step 1: root enclosures.** PREFIX-660 supplies strict exact brackets:

```
z_*(12) in (19/128 - 584/2^24, 19/128 - 583/2^24)
z_*(24) in (19/128 + 3682/2^24, 19/128 + 3683/2^24).
```

Both brackets lie in `I`, have width `delta=2^-24`, and have exact midpoints `z_12,z_24` above. Hence `|z_q-z_*(q)|<delta/2`.

**Step 2: centered loss.** PREFIX-660 proves for the whole `I`:

```
-13000000 < g_12''(z) < 0,
-52000000 < g_24''(z) < 0.
```

At `z_*(q)`, `g_q'(z_*(q))=0`. Taylor's theorem along the same interval with `C_12=13000000`, `C_24=52000000` gives

```
0 <= M(q)-g_q(z_q) < (C_q/2) |z_q-z_*(q)|^2
                     < C_q delta^2/8 = D_q,
D_12 = 203125/35184372088832,
D_24 = 203125/8796093022208.
```

**Step 3: normal coercivity and fixed comparison.** PREFIX-670 supplies, over all `R`,

```
M(12)-V_12(p,z) >= 76650p + 1081326p^2 + 6400000(z-z_*(12))^2,
M(24)-V_24(p,z) >= 306490p + 4322652p^2 + 6400000(z-z_*(24))^2.
```

For `p>=1/10^13`, retain only the positive linear normal penalty and combine it with Step 2:

```
V_12(Q_12)-V_12(p,z)
 > 76650/10^13 - D_12
 = 3250156838911/1717986918400000000000 > 1/10^9;

V_24(Q_24)-V_24(p,z)
 > 306490/10^13 - D_24
 = 16227161874427/2147483648000000000000 > 1/10^9.
```

Every comparison is exact and covers the closed `p,z` rectangle, not a sample grid. QED.

## Verification, evidence strength, next unit

The companion `PREFIX673_R6_DYADIC_WITNESS_CERTIFICATE.py` checks the bracket geometry, all rational constants and strict margins with standard-library integer/`Fraction` arithmetic. `PREFIX673_R6_RESULTS.json` records its exact outputs. This is an implication certificate from two existing author-derived precursors; the 189-layer original path computation was not rerun and an independent review has not occurred.

Next: (1) exploit the positive quadratic normal term or refine the existing dyadic root brackets to reduce `10^-13`; (2) build rational `q`-adaptive witnesses to cover `12<=q<=24` with the appropriate universal quantifier; (3) reuse strict competitors for signed-Bernstein branch-and-bound over the symmetry-reduced triangle `0<=p<=z<=1/2`. The full-square global maximum is still the parent objective.

References: `research_notes/portable_direct/2026-11-10_prefix660_r6_moving_edge_maximum.md` (root and curvature); `2026-11-10_prefix670_r6_slot_resolved_normal_stability.md` (normal coercivity); `2026-11-10_prefix672_r6_slot_coupled_fixed_witness_pruning.md` (prior comparison). Scientific pin unchanged.
