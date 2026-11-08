# PREFIX-577 R6: exact balancing hyperplane for arbitrary native initial distributions

Date: 2026-11-08 UTC. Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_PROVED / EXACT_INTEGER_POLYNOMIAL_VERIFIED / UNREVIEWED / NOT_ADMITTED**. Source CLAIM, native writer checkpoint, Result and independent review remain separate.

## New full-probability-family theorem

Retain all 96 native ports and 576 distinct native action labels. At original root zero, draw each native labelled action uniformly. The **declared passive observer** retains the complete first-gate time plus accumulated fifth- and sixth-axis rewards (both reward variables x,y). It does not erase the native six-axis/labelled carrier for other operations.

Let `C(x,y)` be the inherited exact 37-class nongate passive weighted transition, `g(x,y)` the gate-exit vector, `v_n=C^n g`. The proven degree-28 denominator polynomial is `Q(t,x,y)=sum_{k=0}^{28}q_k(x,y)t^k`. Its scalar recurrence residual at index n=28 is `h=sum_{k=0}^{28}q_k C^(28-k)g`. The preceding integral proof (commit `d7e56a1821bfcef28e22a6701980474955247b0c`) explicitly verifies over `Z[x,y]` that `C h=0`, with exactly three positive and three negative quotient classes sharing an identical nonzero polynomial `H(x,y)`.

Pulling those classes back to the original 96 labelled native ports yields for each initial distribution `alpha=(alpha_0,...,alpha_95)`:

```text
sum_{k=0}^{28} q_k(x,y) * s_(28-k)(alpha,x,y)
 = H(x,y) * [ alpha_6+alpha_28+alpha_30 - alpha_7-alpha_29-alpha_31 ],
```

where `s_n(alpha,x,y)=sum_p alpha_p [C_native(x,y)^n g_native(x,y)]_p`.

**Theorem (necessary and sufficient).** For every real initial probability distribution alpha, the exact degree-28 scalar recurrence already holds at n=28 and at every n>=28 **if and only if**

```text
alpha_6+alpha_28+alpha_30 = alpha_7+alpha_29+alpha_31 .
```

For all initial distributions, it holds from n>=29. The family of satisfying probability distributions is the intersection of the 95-dimensional native 96-port probability simplex with one independent balanced linear hyperplane, hence is a 94-dimensional convex polytope. This explicitly preserves joint port influence rather than incorrectly treating six individually exceptional ports as individually indispensable sources of a 29th observer state.

**Constructive example of strictly nontrivial cancellation.** The initial distribution

```text
alpha_6=alpha_7=1/2, all other alpha_p=0
```

uses only two native ports which each individually have minimal generic `Q(x,y)`-linear first-gate dimension29. Their balanced mixture has minimal dimension exactly28: the symbolic annihilator gives the upper bound28, and an independent 28-by-28 Hankel minor at `(x,y)=(2,3)` modulo `1000000007` equals `270293921`, which is nonzero. Two further balanced mixed examples `(6+29)/2`, `(28+31)/2` have nonzero determinants `130554443`, `123513705`, respectively.

## Exact proof and observer semantics

The sufficiency and necessity of the equation follow from the full exact integer polynomial identity, `H != 0`, and independence of the initial distribution coefficients. The identity `Ch=0` makes every n>=29 recurrence hold. Rank lower bounds rely on a single **nonzero exact finite-field determinant**, which is a valid certificate that its underlying integer polynomial determinant is not identically zero. This is a complete argument for the algebraic family (not an extrapolation from sampling a finite time window).

Reproducible author-side verification: `prove_balanced_exceptional_starts.py` independently enumerates original native 576 labelled edges, checks the exact previous polynomial class-sign certificate at the declared zero root, then certifies nonzero modular 28x28 minors of the three paired examples. Certificate `BALANCED_EXCEPTIONAL_STARTS_CERTIFICATE.json` SHA256 `2c0bacb9539494b57ef678d6667b70fed7d6a409831b541d77a5966f5c27b3ce`. This proof inherits the previous exact, fully polynomial `UNIVERSAL29_CERTIFICATE.json` (SHA256 `60d2f6e5365a98ddb9615a064ce82cbcf7ae931871479ff7d329837ec80b9893`).

This is new mathematical progress in the **BRC observer interaction** `COMPOSE_APPLIED`: initial port fibres that are separately information-bearing may yield a shorter signed linear observer through a proven balanced mixture; retain labels for future active operations. The exact frozen native source is unchanged.

**Source duties:** Original D25/TP2-B6F4FC938FF94941C1B7 real original-class H0/B0, `[X]U mod p^2`, Frobenius direction/eta and native CM remain unfinished; no valid current Source CLAIM. UR V2 original four-file bundle expected 94687 bytes with SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains unresolved. No earlier work was re-proved as new source-native progress.

**Next mathematical question:** Classify all intersections of the balanced hyperplane with additional six-axis/labelled observer constraints and determine when higher-order active choices restore the 29th direction. A signed passive factor is not a positive Markov state aggregation for arbitrary operations.
