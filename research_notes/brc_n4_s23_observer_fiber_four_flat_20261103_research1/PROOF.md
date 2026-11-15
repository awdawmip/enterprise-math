# BRC N=4 / S23 — exact four-dimensional observer fiber and five-parameter continuum adversary

**Date:** 2026-11-03. **Author-side theorem:** analytic proof plus executed exact-rational checker. **Frozen scientific source:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Fixed decoder bank:** `57a6db1d81068504cca2b3a6ea809a63555473d6`. **Inherited boundary theorem:** `1c383a8b7f5d578bd406bb519668c61ac6df0242`, whose risk vector and unique 1D worst point are used as input here. **Status:** unreviewed author-side result.

## Source-preserving model

Use six distinct, labeled source preparations, with eleven real shared causal parameters `z0,...,z10 in [0,1]`. As fixed in the inherited proof, the source-index arrays are

```
A = [0,0,0,1,1,1]
B = [2,2,3,2,2,4]
C = [5,6,7,8,9,10]
M = [[10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
     [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20]]
```

For source `i`, set `R_i(z)=R(z[A_i],z[B_i],z[C_i])`, where

```
R(a,b,c) = (a, (1-a)b, (1-a)(1-b)c, (1-a)(1-b)(1-c)).
P_i(z) = sum_j (M[i,j]/20) R_j(z).
```

Each of the six source labels and four outcomes is retained. For any family of fixed stochastic decoders `D`, let `Q_D` be its source-indexed output and `L_D(z)=max_i TV(P_i(z),Q_{D,i})`. The `min_D` expression refers to whichever bank is explicitly named.

## Theorem 1 — an exact 4D fiber in the original 11D model

Let

```
z* = (1/3,5/6,1,1/2,1/2; 1/3,1/2,1,1/2,1/3,1/3).
```

Then, **with equality of the full labeled six-source observation tuple**,

```
{ z in [0,1]^11 : P(z)=P(z*) }
= { (1/3,5/6,1,1/2,1/2; a,b,1,c,d,1/3) : (a,b,c,d) in [0,1]^4 }.
```

This is an exact fiber characterization for this observation map, not merely a local approximation.

**Proof, forward inclusion.** Sources `i=0,1,3,4` use the shared `b=z2=1`. In those four source rows, the last two coordinates of `R(a,b,c)` have factor `(1-b)=0`, so their source-specific `c=z5,z6,z8,z9` makes no contribution to any of the four outcome probabilities. The remaining source rows `i=2,5` use `z7,z10` instead. Therefore all `a,b,c,d` preserve all six labeled `R_i`, hence all six `P_i`.

**Proof, reverse inclusion.** Mixing `M/20` has determinant `(1/20)(2/5)=1/50 != 0` (two invertible 2x2 blocks and two identity rows). It is exactly invertible. Explicitly, componentwise on four-outcome row vectors,

```
R0=11 P0-10 P1; R1=10 P1-9 P0; R2=P2;
R3=(9 P3-5 P4)/4; R4=(5 P4-P3)/4; R5=P5.
```

Hence equality of `P` forces equality of each **labeled raw source** `R_i`. For any `R(a,b,c)`, its first entry determines `a`; when `a<1`, the second determines `b=R[1]/(1-a)`; when also `b<1`, the third determines `c=R[2]/((1-a)(1-b))`. At `z*`, the `a` values `z0=1/3,z1=5/6` are below one, while `b=z3=z4=1/2` is below one in source rows 2 and 5. Thus `z0,z1,z2,z3,z4,z7,z10` are uniquely reconstructed. The other four are the free parameters already displayed. QED.

The exact observation at the worst point is

```
P(z*) = [
 [1/3, 2/3,   0,    0],
 [1/3, 2/3,   0,    0],
 [1/3, 1/3, 1/3,    0],
 [5/6, 1/6,   0,    0],
 [5/6, 1/6,   0,    0],
 [5/6, 1/12,1/36,1/18]
].
```

## Theorem 2 — a five-real-parameter exact maximum, with a four-dimensional plateau

Define `H(x,a,b,c,d)=(x,5/6,1,1/2,1/2; a,b,1,c,d,1/3)` for every `(x,a,b,c,d) in [0,1]^5`. For all values, the four `c`-branch parameters are inactive because the shared `z2=1`. Consequently

```
P(H(x,a,b,c,d)) = P(E(x))
```

where `E(x)=(x,5/6,1,1/2,1/2;1/3,1/2,1,1/2,1/3,1/3)` is the inherited exact edge. The six observation rows have the explicit formula

```
P(H) = [
 [x,1-x,0,0],[x,1-x,0,0],
 [x,(1-x)/2,(1-x)/2,0],
 [5/6,1/6,0,0],[5/6,1/6,0,0],
 [5/6,1/12,1/36,1/18]
].
```

For **every** fixed decoder `D`, its risk `L_D(H)` is therefore independent of `a,b,c,d`. For the **specific** ten-decoder bank of the inherited theorem, it follows rigorously that

```
max_{(x,a,b,c,d) in [0,1]^5} min_{D in bank} L_D(H) = 2/3,
argmax = {1/3} x [0,1]^4.
```

Indeed, the inherited theorem proved that `max_x m(E(x))=2/3` and its only maximizing `x` was `1/3`. At that point its exact ten-kernel risk vector was

```
(1, 1, 1, 2/3, 31/36, 2/3, 2/3, 2/3, 1, 43/60).
```

The observation identity transfers the result to all four free parameters. This is an exact mathematical extension from a one-parameter edge to a **five-parameter continuum family** with a 4D set of maximizers, without additional assumptions on the decoder kernels beyond fixed output rows.

## Verification and project interpretation

`VERIFY.js` executes normalized BigInt rational arithmetic. It checks 4 exact `x` values times 16 fiber corners = 64 source-observation equalities, the six 4-outcome rows at `z*`, the blockwise inverse and recovery of seven visible parameters. The proof's zero factors and inverse algebra cover all real parameters; the finite checks validate the implementation rather than replace that proof.

The retained observer is the **complete ordered tuple of six labeled source distributions**. The fiber equivalence is valid for risk functionals that factor through this tuple, including any fixed decoder bank. It is an observer-scoped quotient, not an assertion that latent causal branch provenance, arbitrary future interventions or native six-dimensional cell data are the same. No Heartbeat/Shor native dynamical or physical claim is made.

**New reusable principle:** When a shared branch probability equals one, source-specific downstream coordinates may become completely unobservable even though the source mixing itself is invertible. Exact inversion of source mixing separates structural causal nonidentifiability from information loss in the measurement channel.

**Scientific next problem:** Starting from this certified four-dimensional risk plateau, reoptimize three free decoder kernels against the new `2/3` witness and earlier S18/J/F5/C6/2D families; test whether a finite repair preserves the `3/5` target, then certify any continuous coverage with shared-decoder-per-cell or analytic bounds. For model design, classify all branch-degeneracy strata with source-label-safe observation fibers, while retaining their full causal provenance before any risk-only quotient.
