# X6 R153 — exact Port-10 lower-D ray at B=20 (all 0<D<=528)

Date: 2026-11-24 (Asia/Shanghai). Status: **AUTHOR PROOF WITH EXACT FINITE-POPULATION CONTINUUM CERTIFICATE PASS**. Independent mathematical review: **NOT_REVIEWED**. No native physical inference or formal Result/Review is asserted.

## Inherited frozen science and type

Scientific inputs remain **R121** `8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd` and **R122** `0687aa24f5402da3b35f914dd6907967a9805b94`, unmodified. P000 V5, ACTIVE Heartbeat World and six native axes remain in force.

This is the previously declared **conditional static centered-three-axis six-pair BRC observer**, not the complete native six-axis time evolution, a final Cell address, or an attribution of native structural residual. The exact rational calculations are algebra on this fixed joint-observer score. No pi, trigonometric, matrix-exponential or classical physics computation is used. All six observation pairs remain present, and every original integer vector is checked; the finite certificate does not erase their future-relevant relational information.

For nonzero integer `v=(x,y,z)`, let
```
q(v)=max(sum(max(coord,0)),sum(max(-coord,0))) <= 10
h=(0, x+3y+6z, 3x+12y+30z, 7x+39y+126z)
g(v)=(|h1-h0|, |h2-h0|, |h3-h0|, |h2-h1|, |h3-h1|, |h3-h2|)
```
Identify only `v` and `-v`, not nonzero integer multiples: exactly **1,935** unoriented Port-10 vectors. In the previously frozen model, set `w=(136,20,176,D)`, `D>0`; the six joint capacities are `(156,312,136+D,196,20+D,176+D)`. Write `F_v(D)=max_j(g_j(v)/s_j(D))`, `eta(D)=min_v F_v(D)` and `N(D)={v:2F_v(D)<3eta(D)}`.

## R153 theorem — complete lower-D ray

For **every real 0<D<=528** the exact optimum is

```
eta(D) = 3/(136+D),   0<D<=20
       = 1/52,        20<=D<=292
       = 6/(20+D),    292<=D<=528.
```
The overlapping endpoints agree exactly.

Let
```
U=(4,-4,1)   g=(2,6,2,4,0,4)
V=(6,-1,0)   g=(3,6,3,3,0,3)
A=(1,0,0)    g=(1,3,7,2,6,4)
C=(5,-4,1)   g=(1,3,5,2,6,8)
K=(5,-1,0)   g=(2,3,4,1,6,7)
H=(9,-5,1)   g=(0,3,6,3,6,3).
```
Then the **entire** strict 3/2-near set is

```
0<D<=188:   N={U,V}                 (2)
188<D<421:  N={U,V,A,C,K,H}         (6)
421<=D<448: N={V,A,C,K,H}           (5)
448<=D<=528:N={A,C,K,H}             (4).
```

Exact equality is excluded at each strict-membership wall. At **D=188**, A/C/K/H simultaneously touch the near threshold `3/104` and enter strictly only for D>188. At **D=421**, U has `F_U=1/49=(3/2)eta` and exits. At **D=448**, V has `F_V=1/52=(3/2)eta` and exits. Thus this fixed ray has a **2 → 6 → 5 → 4** reentrant member-count profile. The D=448 wall agrees with the previous R142 unique lower-contact result at B=20; the four-member D=528 endpoint agrees with R143. The domain D<528 was not covered by R152's middle-B half-strip.

## Exact proof and exhaustive continuum certificate

**Upper witnesses.** Direct substitution gives `F_V=3/(136+D)` for `0<D<=20`, `F_V=1/52` for `20<=D<=292`, and `F_A=6/(20+D)` for `292<=D<=528`. Hence the proposed expression always bounds eta above.

**Global lower bound and strict-near membership.** The accompanying source-code certificate independently enumerates the full 1,935-vector population (all six integer gaps, exact positive denominators). For each of the three optimizer pieces, take the proposed target `e(D)=p/(kD+t)`. The truth values of `g_j/(a_j D+b_j) < e(D)` and `g_j/(a_j D+b_j) < 3e(D)/2` change only at roots of

```
g_j (kD+t) - lambda*p (a_j D+b_j) = 0,   lambda in {1,3/2}.
```

These equations are **affine in D**. Unless identically zero, each has at most one root; identically zero comparisons retain equality across a whole interval and are handled by the exact sample. The certificate generates *all* such rational roots in the three closed pieces, including their endpoints. It then checks both each critical point and the exact rational midpoint of every adjacent pair. On an open interval without these roots, the sign of every relevant affine comparison is constant. Thus each vector's `F_v>=e` predicate, its `2F_v<3e` predicate, and the existence of an optimizing equality witness are stable throughout that interval. The supplied upper witnesses plus complete lower checks prove the optimum and every strict near-membership comparison for **all real D**, not by sampling extrapolation.

The complete critical-point counts (including piece endpoints) are **[4,22,9]** for the pieces `[0,20]`, `[20,292]`, `[292,528]`; the resulting **67** rational checks each enumerate all **1,935** vectors. The endpoint D=0 is an auxiliary algebraic limit point, not part of the positive-weight theorem. No floating-point arithmetic is used.

Actual local execution on 2026-11-24:

```
R153 EXACT B=20, 0<D<=528 CONTINUUM CERTIFICATE PASS
complete_integer_directions 1935 critical_points_by_eta_piece [4, 22, 9] exact_full_population_probes 67
eta switch D=20,292; near-set changes D=188,421,448
```

Verifier: `research_notes/portable_direct/x6_r153_B20_D0_528_exact_verify.py`, exact Git blob SHA1 `184f983b8da6fb2c37818bec03ea7ba3cba57f46` (the remote published blob matched the locally executed file). Python standard library `Fraction` suffices. This is a deterministic exact proof certificate whose asserted finite loops and affine-root argument can be independently audited. Its methodological scope is fixed B=20 and the declared Port-10 static observer.

## Scientific interpretation, provenance, and next step

R152 completed `20<B<136,D>=528`. R153 establishes a new boundary-spanning slice **below D=528** at exactly B=20, and discovers one four-direction simultaneous entry at D=188 in addition to the earlier sharp D=448 single-direction exit. These are observer-specific static score relations; the original six-dimensional P000 ontology and source provenance are retained.

Suggested next scientific unit: let B vary across a neighborhood of 20 and resolve the fourfold D=188 contact into its exact two-parameter walls; then extend the lower-D atlas to an open B interval while preserving the full Port-10 population and all six pairs. Check whether the observed six-member interval persists as a two-parameter chamber or splits. This is open, not a claimed physical-rotation result.

Independent mathematical review, native six-axis dynamics and formal canonical Result/Review remain pending. Researcher Activity and the account journal are provenance operations separate from this scientific publication.
